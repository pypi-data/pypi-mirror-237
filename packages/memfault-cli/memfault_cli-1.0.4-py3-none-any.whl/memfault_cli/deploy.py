import logging
from typing import Dict, Tuple, Union

import click
import requests
from requests import Session
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

from .authenticator import Authenticator
from .context import MemfaultCliClickContext

log = logging.getLogger(__name__)


class Deployer:
    def __init__(self, *, ctx: MemfaultCliClickContext, authenticator: Authenticator):
        self.ctx: MemfaultCliClickContext = ctx
        self.authenticator: Authenticator = authenticator
        self.session = self._create_requests_session()

    @staticmethod
    def _create_requests_session() -> Session:
        retry_strategy = Retry(
            total=5,
            backoff_factor=2,  # Sleep for 2s, 4s, 8s, 16s, 32s, Stop
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["HEAD", "GET", "POST", "PUT", "DELETE"],
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        session = requests.Session()
        session.mount("https://", adapter)
        session.mount("http://", adapter)
        return session

    @property
    def base_url(self) -> str:
        return self.ctx.api_url

    def _api_base_url(self) -> str:
        return f"{self.base_url}/api/v0"

    def _projects_base_url(self) -> str:
        return f"{self.base_url}/api/v0/organizations/{self.ctx.org}/projects/{self.ctx.project}"

    @property
    def deployment_url(self) -> str:
        """
        The upload URL for a 'prepared upload' for the configured authentication method.
        """
        return f"{self._projects_base_url()}/deployments"

    def deploy(
        self, *, release_version: Union[str, Tuple[str, str]], cohort: str, rollout_percent: int
    ) -> None:
        deployment_type = "normal" if rollout_percent == 100 else "staged_rollout"
        json_d: Dict[str, Union[str, Tuple[str, str], int]] = {
            "type": deployment_type,
            "release": release_version,
            "cohort": cohort,
        }

        if deployment_type == "staged_rollout":
            json_d["rollout_percent"] = rollout_percent

        response = self.session.post(
            self.deployment_url, json=json_d, **self.authenticator.requests_auth_params()
        )
        if response.status_code >= 400:
            raise RuntimeError(
                f"Request failed with HTTP status {response.status_code}\nResponse"
                f" body:\n{response.content.decode()}"
            )
        log.info("Release %s successfully deployed to Cohort %s", release_version, cohort)

    def deactivate(self, *, release_version: Union[str, Tuple[str, str]], cohort: str) -> None:
        """
        Deactivate the specified release for the cohort, if it is currently active.
        """
        # first query the cohort to get the active deployment id
        response = self.session.get(
            f"{self._projects_base_url()}/cohorts/{cohort}",
            **self.authenticator.requests_auth_params(),
        )
        if response.status_code >= 400:
            raise click.exceptions.UsageError(
                f"Request failed with HTTP status {response.status_code}\nResponse"
                f" body:\n{response.content.decode()}"
            )
        cohort_data = response.json()
        try:
            # retrieve the last_deployment for the cohort to check if it matches
            # the release to be deactivated. note that this will be None in the
            # case of no active deployment
            last_deployment = cohort_data["data"]["last_deployment"]

            current_release = last_deployment["release"]["version"]
            if current_release != release_version:
                raise click.exceptions.UsageError(
                    f"Current deployed release ({current_release}) for cohort {cohort} doesn't"
                    f" match the selected release for deactivation, {release_version}, performing"
                    " no action"
                )
        except (KeyError, TypeError) as e:
            raise click.exceptions.UsageError(
                f"Unable to find active deployment for cohort {cohort}"
            ) from e

        # now deactivate the deployment
        deployment_url = f"{self._projects_base_url()}/deployments/{last_deployment['id']}"
        response = self.session.delete(deployment_url, **self.authenticator.requests_auth_params())
        if response.status_code >= 400:
            raise click.exceptions.UsageError(
                f"Request failed with HTTP status {response.status_code}\nResponse"
                f" body:\n{response.content.decode()}"
            )
        log.info("Release %s successfully deactivated from Cohort %s", release_version, cohort)
