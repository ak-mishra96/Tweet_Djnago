from . import views
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.tweet_list , name = 'tweet_list' ),
    path('create/', views.tweet_create , name = 'tweet_create'), #ye function ka naam hota hai beech mein jo views mein likhte hai
    path('<int:tweet_id>/edit/', views.tweet_edit , name = 'tweet_edit'),
    path('<int:tweet_id>/delete/', views.tweet_delete , name = 'tweet_delete'),
    path('register/', views.register , name = 'register'),

]