from django.contrib import admin
from .models import Post
from django.db import models
from pagedown.widgets import AdminPagedownWidget


# Register your models here.
# Steps for Benjo:
# 1) import model from the models package (line 2)
# 2) register the model with admin.site.register(class)


class AlbumAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }

admin.site.register(Post, AlbumAdmin)





