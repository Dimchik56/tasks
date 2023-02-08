"""tasks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from task import views
from task import views as task

urlpatterns = [
    #admin
    path('admin/', admin.site.urls),

    #Auth
    path('signup/', views.signupuser, name='signupuser'),
    

    #tasks manager
    path('', views.home, name='home'),
    path('current/', views.currenttasks, name='currenttasks'),
    path('task/<int:task_id>', views.viewtask, name='viewtask'),
    path('current/gettasks/<int:num_posts>/', views.gettasks, name='gettasks'),
]
