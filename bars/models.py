from django.db import models

from core.models import CommonInfo


class Bar(CommonInfo):
    name = models.CharField('Name', max_length=255)

    class Meta:
        verbose_name = "Bar"
        verbose_name_plural = "Bar"
        ordering = ['-name']

    def __str__(self):
        return self.name
