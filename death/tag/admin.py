from django.contrib import admin
from .models import Tag

# Register your models here.

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',) # 어드민 페이지에서 출력하고 싶은 필드를 설정


admin.site.register(Tag, TagAdmin) 