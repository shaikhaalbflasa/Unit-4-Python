from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='home'),
    path('cats/', views.cats_index, name='index'),
    # Cat Details Page 
    path('cats/<int:cat_id>/', views.cats_detail, name='detail'),
    # Class Based Views Below
    path('cats/create/', views.CatCreate.as_view(), name='cats_create'),
    path('cats/<int:pk>/update/', views.CatUpdate.as_view(), name='cats_update'),
    path('cats/<int:pk>/delete/', views.CatDelete.as_view(), name='cats_delete')
]

