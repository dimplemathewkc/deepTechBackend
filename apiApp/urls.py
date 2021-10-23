from rest_framework import routers
from .api import FeatureAPI, CoursesAPI

router = routers.DefaultRouter()
router.register(r'featured', FeatureAPI)
router.register(r'courses', CoursesAPI)


urlpatterns = [
]
urlpatterns += router.urls
