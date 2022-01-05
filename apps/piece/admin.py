from django.contrib import admin

from apps.piece.models import PieceColor, Piece


@admin.register(PieceColor)
class PieceColordAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Piece)
class PieceAdmin(admin.ModelAdmin):
    list_display = ('description', )
