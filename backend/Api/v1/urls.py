from django.urls import path
from backend.Api.v1 import views
from django.conf.urls import url

urlpatterns = [
    path('login/', views.LoginView.as_view(), name = 'login_view'), 
    path('signup/', views.SignupView.as_view(), name = 'signup_view'),
    path('profiles/', views.ProfileView.as_view(), name = 'profile_view'),
    path('interests/', views.InterestView.as_view(), name = 'interest_view'),
    path('inner_circle/', views.InnerCircleView.as_view(), name = 'inner_circle'),
    path('level/', views.LevelView.as_view(), name = 'level_view'),
    path('communities/', views.CommunityView.as_view(), name = 'communities'),
    path('projects/', views.ProjectView.as_view(), name = 'projects'),
    path('comments/', views.CommentView.as_view(), name = 'comments'),
    path('sub_comments/', views.SubCommentView.as_view(), name = 'sub_comments'),

    # catch-all pattern for compatibility with the Angular routes
    # url(r'^(?P<path>.*)/$', views.index),
]