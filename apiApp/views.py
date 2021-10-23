from django.views.decorators.http import require_http_methods
from .models import Courses, Videos
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from loguru import logger
import json


@require_http_methods(["GET"])
def get_videos(request):
    payload = json.loads(request.body.decode('utf-8'))
    course_id = payload.get('id')
    if Courses.objects.get(id=course_id):
        course = Courses.objects.get(id=course_id)
        print(course.video.all())
        return HttpResponse('ok')
    return HttpResponse('not ok')


# @require_http_methods(["GET"])
# def all_post(request):
#     blog = [i.as_dict() for i in Blog.objects.all()]
#     logger.debug(blog)
#     return HttpResponse(blog)
#
#
# @require_http_methods(["GET"])
# def featured_post(request):
#     blog = list(Blog.objects.filter(featured=True).values('author','feature_image','title'))
#     logger.debug(blog)
#     return HttpResponse(blog)
#
# @require_http_methods(["GET"])
# def get_post(request):
#     payload = json.loads(request.body.decode('utf-8'))
#     id = payload.get('id')
#     if Blog.object.filter(id=id):
#         blog = Blog.object.get(id=id)
#     else:
#         blog = {'Error':'Blog with is:{} not found'.format(id)}
#
#     return HttpResponse(blog)
#
# @require_http_methods(["POST"])
# def save_post(request):
#     payload = json.loads(request.body.decode('utf-8'))
#     print(payload)
#     title = payload.get('title')
#     sub_title = payload.get('sub_title')
#     author = payload.get('author')
#     content = payload.get('content')
#     feature_image = payload.get('feature_image')
#     published = payload.get('published')
#     reviewed = payload.get('reviewed')
#     featured = payload.get('featured')
#     status = payload.get('status')
#     excert = payload.get('excert')
#     slugs = payload.get('slug')
#     category = payload.get('category')
#     tags = payload.get('tag')
#     visibility = payload.get('visibility')
#     images = payload.get('images')
#
#     blog, created = Blog.objects.get_or_create(author=author, title=title)
#     if created:
#         pass
#     else:
#         obj = Blog(author=author, title=title, sub_title=sub_title, content=content,
#                    feature_image=feature_image, featured=featured, reviewed=reviewed,
#                    status=status, excert=excert, category=category, visibility=visibility, published=published)
#
#         for image in images:
#             img = BlogImages(blog_id=obj,img_url=image)
#             img.save()
#
#         for slug in slugs:
#             slug = Slug(blog_id=obj, slug=slug)
#             slug.save()
#
#         for tag in tags:
#             tag = Tags(blog_id=obj,tag=tag)
#             tag.save()
#
#         obj.save()
