from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from apps import piece
from apps.piece.api.serializers import PieceColorSerializer, PieceSerializer
from apps.piece.models import PieceColor, Piece


class PieceColorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows pieces color to be viewed or edited.
    """
    queryset = PieceColor.objects.all()
    serializer_class = PieceColorSerializer


class PieceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows pieces to be viewed or edited.
    """
    queryset = Piece.objects.all()
    serializer_class = PieceSerializer

    @action(detail=False, methods=['get'])
    def get_piece_id(self, request):
        piece = Piece.objects.filter()
        serializer = self.serializer_class(piece, many=True)
        return Response(serializer.data)

