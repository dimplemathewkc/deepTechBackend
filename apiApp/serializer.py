from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from .models import Blog, Courses, Videos

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class FeaturedArticlesSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    class Meta:
        model = Blog
        fields = ['author', 'feature_image', 'title']

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = ['video_name','logo','link','duration']

class CoursesSerializer(serializers.ModelSerializer):
    video = VideoSerializer(many=True)
    class Meta:
        model = Courses
        fields = ['course_name','logo','video','description','feedback','created_by']
