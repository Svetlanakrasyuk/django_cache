from django.urls import path
from django.views.decorators.cache import cache_page

from .views import ShowHome

urlpatterns = [
    path("", ShowHome.as_view(), name="home"),
    # path("", cache_page(60 * 1)(ShowHome.as_view()), name="home"),
]
