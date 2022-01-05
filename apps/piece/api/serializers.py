from rest_framework import serializers

from apps.piece.models import PieceColor, Piece


class PieceColorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PieceColor
        fields = ['id', 'name', 'abbreviation']


class PieceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Piece
        fields = ['id', 'description', 'notation', 'color', ]