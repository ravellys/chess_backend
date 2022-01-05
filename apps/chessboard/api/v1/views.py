from rest_framework import viewsets, permissions
from apps.chessboard.models import RowChessBoard, ColChessBoard
from apps.chessboard.api.serializers import RowChessBoardSerializer, ColChessBoardSerializer


class RowChessBoardViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = RowChessBoard.objects.all()
    serializer_class = RowChessBoardSerializer


class ColChessBoardViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = ColChessBoard.objects.all()
    serializer_class = ColChessBoardSerializer
