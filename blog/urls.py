
from django.urls import path,include

from    django.conf import  settings
from .  import  views
app_name='blog'
urlpatterns = [
    
    path('',views.blog_all, name='blog_all'),
    path("<int:blog_id>/", views.detail, name="detail")
    

]