import pwd
from os import getgid

from nwon_deployment.helper.running_on_gitlab_ci import running_on_gitlab_ci


def get_group_id():
    if running_on_gitlab_ci():
        try:
            return pwd.getpwnam("gitlab-runner").pw_gid
        except KeyError:
            pass

    return getgid()
