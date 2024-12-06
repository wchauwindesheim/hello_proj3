from django.urls import path

from .views import HomePageView
from .views import AboutPageView

app_name = 'pages'
urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('about/', AboutPageView.as_view(), name='about'),
]