from django.db import models


class DateTimeInterval(models.Model):

    start_datetime = models.DateTimeField(max_length=200)
    end_datetime = models.EmailField(blank=True, null=True)

    class Meta:
        ordering = ('start_datetime', 'end_datetime')
