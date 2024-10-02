
from django.urls import include, re_path

from apps.custom_auth.routers import router


urlpatterns = [
    re_path(r'^', include(router.urls)),
]
