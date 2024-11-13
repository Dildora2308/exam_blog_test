from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def str(self):
        return self.name


class Post(models.Model):

    class CategoryStatus(models.TextChoices):
        ALL= 'all', 'barchasi'
        TECHNOLOGY = 'technology', 'texnalogiya'
        LIFESTYLE ='lifestyle', 'hayot tarziga oid'
        CULTURE = 'culture', 'Madaniy'



    title= models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='project/',null=True)
    author = models.CharField(max_length=100)
    views = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)


    def str(self):
        return self.title