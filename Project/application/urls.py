from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.NewsView.as_view(), name='news'),
    path('category/', views.CategoryView.as_view(), name='category'),
    path('article/', views.ArticalView.as_view(), name='article'),
    path('category/<int:category_id>/article/', views.RelatedArticleView.as_view()),
    path('article/<int:article_id>/', views.SingleArticleView.as_view(), name='single_article'),
     path('search/name_article/', views.SearchView.as_view())
]