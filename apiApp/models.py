from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
class TimeStamped(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Slug(models.Model):
    slug = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Slug'

    def __str__(self):
        return self.slug

class Category(models.Model):
    category = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Category'

    def __str__(self):
        return self.category


class SubCategory(models.Model):
    sub_category = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'SubCategory'

    def __str__(self):
        return self.sub_category

class Tags(models.Model):
    tag = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.tag

class BlogImages(models.Model):
    img_url = models.URLField(max_length=300, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'BlogImages'

    def __str__(self):
        return self.img_url

class Blog(TimeStamped):
    STATUS = (
        ('DRAFT','DRAFT'),
        ('IN-REVIEW', 'IN-REVIEW'),
        ('PUBLISHED', 'PUBLISHED')
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True, blank=True)
    sub_title = models.CharField(max_length=200, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    feature_image = models.URLField(max_length=300, null=True, blank=True)
    featured = models.BooleanField(default=False, null=True, blank=True)
    reviewed = models.BooleanField(default=False, null=True, blank=True)
    published = models.BooleanField(default=False, null=True, blank=True)
    status = models.CharField(max_length=10,choices=STATUS, default=1, null=True, blank=True)
    views = models.IntegerField(null=True, blank=True)
    excert = models.CharField(max_length=200, null=True, blank=True)
    slug = models.ManyToManyField(Slug, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.ManyToManyField(SubCategory, null=True, blank=True)
    tag = models.ManyToManyField(Tags, null=True, blank=True )
    visibility = models.BooleanField(default=False, null=True, blank=True)
    images = models.ManyToManyField(BlogImages, null=True, blank=True)
    class Meta:
        verbose_name_plural = 'Blog'

    def __str__(self):
        return self.title

    def as_dict(self):
        return {
            "id": self.id,
            "author" : self.author,
            "sub_title": self.sub_title,
            "content": self.content,
            "feature_image": self.feature_image,
            "featured": self.featured,
            "reviewed": self.reviewed,
            "published": self.published,
            "status": self.status,
            "views": self.views,
            "excert": self.excert,
            "slug" : self.slug,
            "category": self.category,
            "sub_category": self.sub_category,
            "tag" : self.tag,
            "visibility": self.visibility,
            "images": self.images,
        }


class Videos(TimeStamped):
    video_name = models.CharField(max_length=200, null=True, blank=True)
    logo = models.ImageField(upload_to='video/')
    link = models.URLField(max_length=400)
    duration = models.DateTimeField(default=datetime.now())

    class Meta:
        verbose_name_plural = 'Videos'

class Testimonial(TimeStamped):
    user = models.CharField(max_length=200, null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)
    feedback = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Testimonial'

class Courses(TimeStamped):
    course_name = models.CharField(max_length=200, null=True, blank=True)
    logo = models.ImageField(upload_to='course/')
    video = models.ManyToManyField(Videos)
    description = models.TextField(null=True, blank=True)
    feedback = models.ManyToManyField(Testimonial)
    created_by = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Courses'
