from django.db import models

from utils.models import AbstractTableMeta

class WaitlistEntry(AbstractTableMeta, models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(
        verbose_name='email_adress',
        max_length=255,
        unique=True
    )
    level = models.IntegerField(verbose_name='Class Level', default=1)
    notes = models.TextField()

    class Meta:
        verbose_name_plural = 'Waitlist Entries'

    def full_name(self):
        return f'{self.first_name} {self.last_name}'



