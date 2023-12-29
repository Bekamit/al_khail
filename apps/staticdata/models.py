from django.db import models


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)


class StaticData(SingletonModel):
    field1 = models.CharField(max_length=100)
    field2 = models.TextField()

    def __str__(self):
        return f"{self.field1}"

    class Meta:
        verbose_name = 'Static Data'
        verbose_name_plural = 'Static Data'
