from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path('', views.blog_list, name="list"),
    path('create', views.create_post, name="create"),
    path('<id>', views.post_detail, name="detail"),
]

