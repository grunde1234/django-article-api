from django.contrib import admin
from .models import CategoryModel, ArticleModel, JournalistModel

# Register your models here.
admin.site.register(JournalistModel)
admin.site.register(CategoryModel)
admin.site.register(ArticleModel)