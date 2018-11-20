from django.urls import path

from .views import AboutPageView, HomePageView, AutorPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('autor/', AutorPageView.as_view(), name='autor'),
    path('', HomePageView.as_view(), name='home'),
]
