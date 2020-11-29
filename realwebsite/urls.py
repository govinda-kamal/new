"""realwebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# 1. 1st of all include app urls to include the apps urls 
from django.urls import include, path

# this is the urls as the server sstarts it comes here and see the urls
urlpatterns = [                  # we include the home.urls which is an app that is seperate
    path('admin/', admin.site.urls),    
    path("",include("home.urls")),     # 2. it mean whenever the server started the go to the home app urls for 3rd go to blog.urls
    path("blog/",include("blog.urls"))   # and when write blog then go to the blog urls
 ]
