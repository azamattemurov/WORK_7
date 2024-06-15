from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import TeamModel
from django.contrib.auth.models import User




class BlogCategoryModel(models.Model):
    objects = None
    name = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class BlogTagModel(models.Model):
    objects = None
    name = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')


class BlogModel(models.Model):
    objects = None
    title = models.CharField(max_length=100, db_index=True)
    image = models.ImageField(upload_to='blog-images')
    short_info = models.TextField(null=True)
    content = models.TextField()
    media_url = models.URLField(null=True, blank=True)

    category = models.ManyToManyField(BlogCategoryModel, related_name='blogs')
    tags = models.ManyToManyField(BlogTagModel, related_name='tags')
    author = models.ForeignKey(TeamModel, on_delete=models.CASCADE, related_name='blogs')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = _('Blogs')


class BlogCommentModel(models.Model):
    objects = None
    blogs = models.ForeignKey(BlogModel, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')

