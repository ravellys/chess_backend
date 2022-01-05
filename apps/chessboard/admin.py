from django.contrib import admin

from apps.chessboard.models import RowChessBoard, ColChessBoard


@admin.register(RowChessBoard)
class RowChessBoardAdmin(admin.ModelAdmin):
    list_display = ('description', )


@admin.register(ColChessBoard)
class RowChessBoardAdmin(admin.ModelAdmin):
    list_display = ('description', )
