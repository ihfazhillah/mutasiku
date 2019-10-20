from django.db import models


class Report(models.Model):
    file = models.FileField(upload_to="jenius_report")
    status = models.CharField(max_length=100, null=True, blank=True)
