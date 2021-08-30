"""vaper_shop URL Configuration

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
from django.urls import path, include

from clients.views import sign_up, profile, credits, add_credits
from shop.views import index, product_detail


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('', include('django.contrib.auth.urls'), name='login'),  # Sign IN
    path('signup/', sign_up, name='signup'),  # Sign UP
    path('profile/', profile, name='profile'),
    path('credits/', credits, name='credits'),
    path('credits/<int:id>/<int:credits>', add_credits, name='add_credits'),
    path('<str:fake>=<int:id>/', product_detail, name='detail'),
]
