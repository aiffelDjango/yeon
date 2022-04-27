"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
import Landing.views # Landing 파일의 views를 import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Landing.views.index, name='index'), # 바로 index.html 실행
    path('study/', Landing.views.study, name='study'), # Landing 안 views 안 study를 실행시켜줘
    path('sticker', Landing.views.sticker, name='sticker'),
    path('stickerResult', Landing.views.stickerResult, name='stickerResult')
]

# 127.0.0.1:8000/landing => Landing.views.index를 실행시킬 거야