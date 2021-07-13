from django.contrib import admin
from .models import Post



# Register your models here.

# make model visible on admin page
admin.site.register(Post)