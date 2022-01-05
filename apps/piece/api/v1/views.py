from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

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
    alias_params = {
        "color__abbreviation": ['color', 'color_abreviation', 'c'],
        "notation": ['notation', 'name', 'type']
    }

    def has_parameters(self, params: dict) -> bool:
        mandatory_parameters = self.alias_params.keys()
        if mandatory_parameters - set(params.keys()):
            return False
        return True

    def convert_params(self, params: dict) -> dict:
        params_converted = {}
        for key, value in params.items():
            for name, alias_list in self.alias_params.items():
                if key in alias_list:
                    params_converted[name] = value
        return params_converted

    @action(detail=False, methods=['get'])
    def get_piece_id(self, request):
        params = request.GET.dict()
        params = self.convert_params(params)

        if not self.has_parameters(params):
            return Response(
                {"message": f"Missing Parameters. Please insert the mandatory parameters: " +
                            f"({' and '.join([ ' or '.join(alias) for alias in list(self.alias_params.values())])})"},
                status=status.HTTP_400_BAD_REQUEST)

        piece = Piece.objects.filter(**params).first()

        if not piece:
            return Response({"message": "Piece Not Founded"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"id": piece.id})
