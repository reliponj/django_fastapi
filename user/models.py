from django.db import models

from core.auth import password_service
from core.models import BaseClass


class AppUser(BaseClass):
    email = models.CharField('Email', max_length=100)
    password = models.CharField('Password', max_length=255, default='', blank=True)
    password_hash = models.CharField(verbose_name='Password', max_length=255, default='', blank=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if self.password:
            self.password_hash = password_service.get_password_hash(self.password)
            self.password = ''

        super(AppUser, self).save(*args, **kwargs)
