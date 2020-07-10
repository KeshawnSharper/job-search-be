"""jobsearchbe URL Configuration

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
from django.urls import path,include
from core.views import TestView
from core.views import ExperienceView
from core.views import JobView
from core.views import ProjectView
from core.views import MessagesView
from core.views import PostsView
from core.views import RequestsView
from core.views import FriendsView
from core.views import SkillsView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # path('restauth/', include('rest_auth.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', TestView.as_view(),name='test'),
    path('experience', ExperienceView.as_view(),name='experience'),
    path('experience/<str:id>', ExperienceView.as_view(),name='experience'),
    path('jobs', JobView.as_view(),name='delete_experience'),
    path('messages', MessagesView.as_view(),name='messages'),
    path('posts', PostsView.as_view(),name='posts'),
    path('messages/<str:id>', MessagesView.as_view(),name='message'),
    path('requests', RequestsView.as_view(),name='requests'),
    path('requests/<str:id>', RequestsView.as_view(),name='requests'),
    path('requests/<str:users_id>/<str:request_id>', RequestsView.as_view(),name='requests'),
    path('skills', SkillsView.as_view(),name='requests'),
    path('skills/<str:id>', SkillsView.as_view(),name='requests'),
    path('friends/<str:id>', FriendsView.as_view(),name='Friends'),
    path('friends', FriendsView.as_view(),name='Friends'),

    # path('experience/<str:id>', ExperienceView.as_view(),name='experience'),

    path('projects', ProjectView.as_view(),name='project'),
    path('projects/<str:id>', ProjectView.as_view(),name='project'),
    path('api/token', obtain_auth_token,name='obtain_token'),
    # path('register', registration_view, name="register"),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
