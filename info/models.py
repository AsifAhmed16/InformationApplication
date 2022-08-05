from django.db import models


class UserInfo(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=16)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'info_'
