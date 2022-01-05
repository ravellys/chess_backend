from rest_framework.routers import SimpleRouter

from apps.piece.api.v1.views import PieceColorViewSet, PieceViewSet

router_pieces = SimpleRouter()
router_pieces.register('', PieceViewSet)
router_pieces.register('colors', PieceColorViewSet)
