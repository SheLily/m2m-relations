from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Tag(models.Model):
    topic = models.CharField(max_length=128, unique=True)
    article = models.ManyToManyField(to=Article, through='TagModel', through_fields=('tag', 'article'), related_name='scopes')

    def is_main(self):
        return self.tagmodel_set.get(tag=self).main

class TagModel(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    main = models.BooleanField()

    
