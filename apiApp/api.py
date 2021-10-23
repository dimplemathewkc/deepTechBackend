from .serializer import FeaturedArticlesSerializer, CoursesSerializer
from rest_framework import routers, serializers, viewsets
from .models import Blog, Courses, Videos

class FeatureAPI(viewsets.ModelViewSet):
    queryset = Blog.objects.filter(featured=True)
    serializer_class = FeaturedArticlesSerializer

class CoursesAPI(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
