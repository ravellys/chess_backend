from django.db import models


class PieceColor(models.Model):
    name = models.CharField(max_length=64)
    abbreviation = models.CharField(max_length=1)

    def __str__(self):
        return self.name


class Piece(models.Model):
    color = models.ForeignKey(PieceColor, on_delete=models.DO_NOTHING)
    notation = models.CharField(max_length=1)
    description = models.CharField(max_length=64)

    def __str__(self):
        return self.description
