from django.urls import path
from . import views
from .views import *



urlpatterns = [
    path('', PostListView.as_view(), name = "blog-home"),
    path('post/<int:pk>/', PostDetailView.as_view(), name = "post-detail"),
    path('about', views.about, name = "blog-about"),
    path('contactform', ContactSubmissionView, name = "blog-contactform"),
    path('success', views.ContactSuccessView, name = "blog-success"),
    path('antara', views.EasterEgg)
    
]

handler404 = 'beniamino_org.views.handler404'

