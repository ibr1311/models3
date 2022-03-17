from django.contrib import admin

from test1.models import Post
from test1.models import Comment

admin.site.register(Post)
admin.site.register(Comment)
