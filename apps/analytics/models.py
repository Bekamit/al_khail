from django.db import models


class Role(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, auto_created=True)
    name = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return f'{self.name}'

    @staticmethod
    def create_role(data: dict):
        return Role.objects.create(**data)


class Analytics(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=70, blank=False, null=False)
    phone_number = models.IntegerField()
    email = models.EmailField()
    message = models.TextField(max_length=150)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def create_analytics(data: dict):
        return Analytics.objects.create(**data)
