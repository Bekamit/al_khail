from django_cleanup.signals import cleanup_pre_delete
from sorl.thumbnail import delete


def sorl_delete(**kwargs):

    delete(kwargs['file'])
    return f"{kwargs['file'].name}"

cleanup_pre_delete.connect(sorl_delete)


# import os
# import shutil
# from django_cleanup.signals import cleanup_pre_delete
# from django.dispatch import receiver
#
#
# # @receiver(cleanup_pre_delete)
# def sorl_delete(sender, instance, file, **kwargs):
#     # Удаляем файл
#     os.remove(file)
#     # Извлекаем путь к папке, содержащей файл, и удаляем ее
#     folder_path = os.path.dirname(file)
#     shutil.rmtree(folder_path)
# cleanup_pre_delete.connect(sorl_delete)