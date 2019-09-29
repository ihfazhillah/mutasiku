from django.db import models

# Create your models here.


class Bank(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Credential(models.Model):
    userid = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)


class Statement(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    keterangan = models.TextField()
    keluar = models.FloatField()
    masuk = models.FloatField()
    ballance = models.FloatField()
    hash_id = models.CharField(max_length=255)
    tanggal = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
