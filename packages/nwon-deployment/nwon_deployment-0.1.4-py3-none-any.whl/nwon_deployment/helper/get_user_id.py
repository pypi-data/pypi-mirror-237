import pwd
from os import getuid

from nwon_deployment.helper.running_on_gitlab_ci import running_on_gitlab_ci


def get_user_id():
    if running_on_gitlab_ci():
        try:
            return pwd.getpwnam("gitlab-runner").pw_uid
        except KeyError:
            pass

    return getuid()
