"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from myapp.views import signup_view, login_view, welcome_view, choose_locker_view
    # get_stuff_back_view
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', login_view, name='signin'),
    path('signup/', signup_view, name="signup"),
    path('welcome/', welcome_view, name='welcome'),
    path('chooselocker/', choose_locker_view, name='choose_locker'),
    # path('getbackstuff/', get_stuff_back_view, name='get_stuff_back'),
]

urlpatterns += staticfiles_urlpatterns()