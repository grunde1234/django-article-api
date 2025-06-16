from django.db import models
from cloudinary_storage.storage import MediaCloudinaryStorage
from cloudinary.models import CloudinaryField

# Create your models here.
class JournalistModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} - email: {self.email}"
    

class CategoryModel(models.Model):
    cat_name = models.CharField(max_length=255, default='Uncategorized')


    def __str__(self):
        return f"{self.cat_name}"
    
class ArticleModel(models.Model):
    author = models.ForeignKey(JournalistModel, on_delete=models.CASCADE,related_name='Journalist')
    category_name = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name='cat')
    title = models.CharField(max_length=200)
    image_select = CloudinaryField('image')
    description = models.TextField()
    published_on = models.DateField()
    location = models.CharField(max_length=200)
