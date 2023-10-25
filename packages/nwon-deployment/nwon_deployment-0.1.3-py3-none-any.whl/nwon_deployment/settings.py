from enum import Enum
from typing import Callable, Dict, Generic, List, Optional, Set, TypeVar, Union

from pydantic import BaseModel

from nwon_deployment.environment_variables.env_variable_map import EnvVariableMap
from nwon_deployment.exceptions.settings_not_set import DeploymentSettingsNotSet
from nwon_deployment.typings.deployment_base_model import DeploymentBaseModel

DockerService = TypeVar("DockerService", bound=Enum)


class DeploymentSettingsGitlab(DeploymentBaseModel):
    use_gitlab_container_registry: bool
    user_name: Optional[str]
    password: Optional[str]
    api_token: Optional[str]
    gitlab_registry_url: Optional[str]


class DeploymentSettings(BaseModel, Generic[DockerService]):
    stack_name: str
    container_name: Callable[[str, int], str]
    user_for_container: Dict[DockerService, str]
    default_command_for_container: Dict[DockerService, str]
    gitlab: Optional[DeploymentSettingsGitlab]
    env_variable_map: EnvVariableMap
    compose_files: Callable[..., Union[Set[str], List[str]]]


__DEPLOYMENT_SETTINGS: Optional[DeploymentSettings[Enum]] = None


def set_deployment_settings(
    settings: DeploymentSettings[Enum],
) -> DeploymentSettings[Enum]:
    global __DEPLOYMENT_SETTINGS

    __DEPLOYMENT_SETTINGS = settings

    return __DEPLOYMENT_SETTINGS


def get_deployment_settings() -> DeploymentSettings[Enum]:
    global __DEPLOYMENT_SETTINGS

    if __DEPLOYMENT_SETTINGS is None:
        raise DeploymentSettingsNotSet("Deployment settings not set")

    return __DEPLOYMENT_SETTINGS
