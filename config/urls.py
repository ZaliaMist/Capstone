"""config URL Configuration

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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from project import views
from project.views import index, addcomment_view, addcommunity_view, addpost_view, navbar_view, UpVoteView, DownVoteView, CommunityView
from authuser.views import login_view, logout_view, signup_view, profile_view, edit_profile_view
from django.views.generic import TemplateView
# handler404 = 'project.views.handler404'
# handler500 = 'project.views.handler500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="homepage"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("signup/", signup_view, name="signup"),
    path("addcommunity/", addcommunity_view, name="addcommunity"),
    path("addcomment/", addcomment_view, name="addcomment"),
    path("addpost/", addpost_view, name="addpost"),
    path('upvote/<int:post_id>/', views.UpVoteView.as_view() , name="like"),
    path('downvote/<int:post_id>/', views.DownVoteView.as_view(), name="dislike"),
    path( '',views.handler404 ),
    path( '',views.handler500 ),
    path('editprofile/<int:user_id>/', edit_profile_view),
    path('profile/<int:user_id>/', profile_view),
    path("community_id/<int:id>/", views.CommunityView.as_view(), name="community_id"),
    path("editCommunity/<int:id>/", views.editCommunity, name='editcommunity'),
    path('', navbar_view),
    path("comment_list/<int:id>/", views.commentlist_view, name="comment_list"),
    path('accounts/', include('allauth.urls')),
    path('google/', TemplateView.as_view(template_name='google.html')),
]

urlpatterns += staticfiles_urlpatterns()