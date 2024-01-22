from django.db import models


class DownloadCatalog(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    phone_number = models.IntegerField(blank=True, null=True)
    email = models.EmailField()
    role = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def create_analytics(data: dict):
        return DownloadCatalog.objects.create(**data)
