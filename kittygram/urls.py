from django.urls import include, path

from rest_framework.routers import SimpleRouter

from cats.views import CatViewSet

router = SimpleRouter()
router.register('cats', CatViewSet)

urlpatterns = [
   path('', include(router.urls)),
]
