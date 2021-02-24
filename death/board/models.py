from django.db import models

# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length=128,
                             verbose_name='제목',
                             default='some string')
    contents = models.TextField(verbose_name='내용',
                                default='some content')
    writer = models.ForeignKey('death_user.Deathuser', on_delete=models.CASCADE,
                                 verbose_name='작성자') # on_delete= models.CASCADE : ForeignKey 에 해당하는 데이터가 삭제되면 같이 삭제
    tags = models.ManyToManyField('tag.Tag', verbose_name='태그')
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                           verbose_name='등록시간')

    def __str__(self):
        return self.title

    class Meta: # 테이블 이름 정하기
        db_table = 'death_board'
        verbose_name = 'death 게시글'
        verbose_name_plural = 'death 게시글'