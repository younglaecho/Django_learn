from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=32, verbose_name='태그명')
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                        verbose_name='등록시간')

    def __str__(self):
        return self.name

    class Meta: # 테이블 이름 정하기
        db_table = 'death_tag'
        verbose_name = 'death 태그'
        verbose_name_plural = 'death 태그'