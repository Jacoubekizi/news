from django.db import models

# Create your models here.
class News(models.Model):
    descripton = models.TextField(max_length=500, null=True, blank=True)
    photo = models.ImageField(verbose_name="Photo", upload_to='images/News')


    def __str__(self):
        return str(self.id)

class Category(models.Model):
    name = models.CharField(verbose_name='Category', max_length=50)

    def __str__(self):
        return self.name
    
    # @property
    # def get_article_related(self):
    #     articles = self.article_set.all()
    #     return articles

class Article(models.Model):
    name = models.CharField(verbose_name='Article_Name', max_length=100)
    photo = models.ImageField(verbose_name='Photo', upload_to='images/Article')
    description = models.TextField(max_length=1000000)
    category = models.ForeignKey(Category, related_name='article_cat', on_delete=models.CASCADE)

    def __str__(self):
        return self.name