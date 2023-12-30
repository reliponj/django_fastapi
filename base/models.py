from django.db import models

from core.models import BaseClass


class Setting(BaseClass):
    copyright = models.CharField('Copyright', max_length=100)

    class Meta:
        verbose_name = 'Settings'
        verbose_name_plural = 'Settings'

    def __str__(self):
        return 'Settings'

    @staticmethod
    def get_settings():
        settings = Setting.objects.filter()
        if settings:
            return settings[0]
        else:
            settings = Setting()
            settings.save()
            return settings
