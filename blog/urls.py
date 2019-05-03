from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', PostListView.as_view(template_name =  'blog/home.html'), name = "blog-home"),
    path('post/<int:pk>/', PostDetailView.as_view(), name = "post-detail"),
    path('about', views.about, name = "blog-about"),
    path('contactform', ContactSubmissionView, name = "blog-contactform"),
    path('success', PostListView.as_view(template_name =  'blog/contactsuccess.html'), {"template" : "contactsuccess"}, name = "blog-success")
    

]
