from django.db import models

# Create your models here.
class Board(models.Model):
    name = models.CharField(max_length=10,verbose_name='Name')
    birthday = models.DateField(verbose_name='Birth Day')
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'board_app_board'
        verbose_name="게시판 WebApp"
        verbose_name_plural = "게시판 WebApp"