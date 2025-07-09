"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
import api.views # 导入我们新创建的视图

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include('api.urls')),
    path('', api.views.index_view, name='index'),
    path('frontendchoose/',api.views.frontendchoose_view,name='frontendchoose'),
    path('game0/',api.views.game0_view,name='game0'),
    path('game1/',api.views.game1_view,name='game1'),
    path('game2/',api.views.game2_view,name='game2'),
    path('game3/',api.views.game3_view,name='game3'),
    path('game4/',api.views.game4_view,name='game4'),
    path('game5/',api.views.game5_view,name='game5'),
    path('game6/',api.views.game6_view,name='game6'),
    path('game7/',api.views.game7_view,name='game7'),
]
