from django.contrib import admin
# 1. 1st of all include app urls 
from django.urls import include, path
from . import views    # 3 . here . is used because we are same folder for 4th go to views.py

urlpatterns = [
    path("",views.Bloghome, name="Bloghome"), #  here after 2nd step our browser come to the blog url now it will go to the view.home and its name is home whcih is simple argument     
    # path("blogpost/",views.blogpost,name="blogpost")
    path("<str:slug>",views.blogpost,name="blogpost")
 ]

#  similarly do for home app