from django.contrib import admin
from .models import Board

# Register your models here.

class BoardAdmin(admin.ModelAdmin):
    list_display = (['title']) # 어드민 페이지에서 출력하고 싶은 필드를 설정


admin.site.register(Board, BoardAdmin)