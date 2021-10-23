from django.contrib import admin
from .models import Blog, Slug, Category, Tags, BlogImages, SubCategory, Videos, Courses, Testimonial

admin.site.register(Blog)
admin.site.register(Slug)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Tags)
admin.site.register(BlogImages)
admin.site.register(Courses)
admin.site.register(Videos)
admin.site.register(Testimonial)
