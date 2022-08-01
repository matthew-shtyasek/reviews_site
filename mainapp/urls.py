"""test_project_6 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path

from mainapp import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('comments/', views.comments_page, name='comments_page'),
    path('comment/<int:pk>', views.comment_page, name='comment_page'),
    path('comment/<int:pk>/<int:state>', views.comment_page, name='comment_page'),
    # path('comment/<int:pk>/<str:msg>', views.comment_page, name='comment_page'),
]
