from django.urls import path,includecd

from .views import homePageView 

 

 

urlpatterns = [ 

    path("", homePageView, name='home'),
    path('', include('pages.urls')),

] 