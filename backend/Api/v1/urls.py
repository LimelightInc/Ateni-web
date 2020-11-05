from django.urls import path, include
from backend.Api.v1 import views
from django.conf.urls import url
from rest_framework.routers import DefaultRouter


#root api
router = DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'profile', views.ProfileViewSet)
router.register(r'interest', views.InterestViewSet)
router.register(r'innercircle', views.InnerCircleViewSet)
router.register(r'level', views.LevelViewSet)
router.register(r'community', views.CommunityViewSet)
router.register(r'project', views.ProjectViewSet)
router.register(r'comment', views.CommentViewSet)
router.register(r'subcomment', views.SubCommentViewSet)


urlpatterns = [
    path('', include(router.urls)),

    path('login/', views.LoginView.as_view(), name = 'login_view'), 
    path('signup/', views.SignupView.as_view(), name = 'signup_view'),
    
    # catch-all pattern for compatibility with the Angular routes????
    # url(r'^(?P<path>.*)/$', views.index),
]