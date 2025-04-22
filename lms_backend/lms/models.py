from django.db import models


# Create your models here.

class BookCategory(models.Model):
    class Meta:
        db_table = 'lms_book_category'

    name = models.CharField(max_length=200, verbose_name='书籍分类')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    modify_date = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    def __str__(self):
        return self.name


class Book(models.Model):
    class Meta:
        db_table = 'lms_book'

    name = models.CharField(max_length=200, verbose_name='书籍名称')
    author = models.CharField(max_length=200, null=True, verbose_name='作者')
    publisher = models.CharField(max_length=200, null=True, verbose_name='出版社')
    pub_date = models.DateField(auto_now_add=True, null=True, verbose_name='出版日期')
    book_category = models.ForeignKey(BookCategory, on_delete=models.DO_NOTHING, verbose_name='书籍分类')
    qty = models.IntegerField(default=0, verbose_name='库存数量')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    modify_date = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    def __str__(self):
        return self.name
