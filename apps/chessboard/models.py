from django.db import models


# Create your models here.
class RowChessBoard(models.Model):
    description = models.CharField(max_length=64)

    def __str__(self):
        return self.description


class ColChessBoard(models.Model):
    description = models.CharField(max_length=64)

    def __str__(self):
        return self.description
