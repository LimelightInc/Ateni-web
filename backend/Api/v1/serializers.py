from django.db.models import fields
from rest_framework import serializers
from backend.models import *



#Auth 
class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')


class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password', 'username')



#Models #todo: MOWIKI
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username','email', 'date_joined')


class InterestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Interest
        fields = ('__all__')


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('__all__')


class InnerCircleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InnerCircle
        fields = ('__all__')


class LevelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Level
        fields = ('__all__')


class CommunityDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Community
        fields = ('__all__')


class ProjectDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('__all__')

class CommentDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('__all__')


class SubCommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SubComment
        fields = ('__all__')