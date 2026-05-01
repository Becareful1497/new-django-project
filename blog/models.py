from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=50, verbose_name='напишите название блога')
    description = models.TextField(verbose_name='напишите статью', blank=True)
    image = models.ImageField(upload_to='blog/', verbose_name='загрузите фото')
    blog_file = models.FileField(upload_to='blog/', verbose_name='загрузите pdf file')
    TYPE_BLOG = (
        ('Программирование', 'Программирование'),
        ('Бизнес', 'Бизнес'),
        ('Медицина', 'Медицна')
    )
    quantity = models.PositiveIntegerField(verbose_name='укажите кол-во страниц', default=20, null=True)
    type_blog = models.CharField(max_length=100, choices=TYPE_BLOG, default='Программирование')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
