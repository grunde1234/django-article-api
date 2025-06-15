from django.urls import path
from .views import CategoryView, ArticleViewCreate, JournalistView, ArticleViewDetail, ArticleViewUpdate, ArticleViewDelete, ArticleViewAll


urlpatterns=[
    path('category/', CategoryView.as_view()),
    path('articles/',  ArticleViewAll.as_view()),
    path('articles/add',  ArticleViewCreate.as_view()),
    path('journalist/', JournalistView.as_view()),
    path('articles/<int:Article_id>/', ArticleViewDetail.as_view()),
    path('articles/<int:pk>/update/', ArticleViewUpdate.as_view()),
    path('articles/<int:pk>/delete/', ArticleViewDelete.as_view()),
]