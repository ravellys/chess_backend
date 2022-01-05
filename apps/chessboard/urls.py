from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter

from apps.chessboard.api.v1.views import RowChessBoardViewSet, ColChessBoardViewSet

router_chessboard = SimpleRouter()
router_chessboard.register('rows', RowChessBoardViewSet)
router_chessboard.register('cols', ColChessBoardViewSet)


