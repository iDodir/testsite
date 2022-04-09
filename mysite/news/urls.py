from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('test/', views.test, name='test'),
    # path('', views.index, name='home'),
    path('', views.HomeNews.as_view(), name='home'),
    # path('category/<int:category_id>/', views.get_category, name='category'),
    path('category/<int:category_id>/', views.NewsByCategory.as_view(), name='category'),
    # path('news/<int:news_id>/', views.view_news, name='view_news'),
    path('news/<int:pk>/', views.ViewNews.as_view(), name='view_news'),
    # path('news/add-news/', views.add_news, name='add_news'),
    path('news/add-news/', views.CreateNews.as_view(), name='add_news'),
]
