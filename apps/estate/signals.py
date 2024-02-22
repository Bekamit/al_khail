from django_cleanup.signals import cleanup_pre_delete
from sorl.thumbnail import delete


def sorl_delete(**kwargs):

    delete(kwargs['file'])
    return f"{kwargs['file'].name}"

cleanup_pre_delete.connect(sorl_delete)
