from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'share'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:Post_id>/', views.detail, name='detail'),
    
    
    path('create/', views.create, name="create"),
    path('cart/', views.cart, name="cart"),
    path('joined/', views.joined, name="joined"),
    path('join/<int:Post_id>/', views.join, name="join"),
    path('like/<int:Post_id>/', views.like, name="like"),
    
    path('modify/<int:Post_id>/', views.modify, name="modify"),
    path('Delete/<int:Post_id>/', views.Delete, name="Delete"),
    
    path('category/<int:category_num>/', views.category, name='category'),

]

