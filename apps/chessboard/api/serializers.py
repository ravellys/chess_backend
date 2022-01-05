from rest_framework import serializers

from apps.chessboard.models import RowChessBoard, ColChessBoard


class RowChessBoardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RowChessBoard
        fields = ['description']


class ColChessBoardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ColChessBoard
        fields = ['description']