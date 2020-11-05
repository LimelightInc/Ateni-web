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
        fields = ('id', 'name')


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = Profile
            fields = ('user', 'image', 'twitter', 'linkedin', 'interest')


class InnerCircleSerializer(serializers.HyperlinkedModelSerializer):
    # user = UserSerializer()
    # contacts = UserProfileSerializer(many=True)

    class Meta:
        model = InnerCircle
        fields = ('user', 'contacts')


class LevelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Level
        fields = ('id', 'name')


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
        fields = ('post', 'user', 'content', 'created')


class SubCommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SubComment
        fields = ('comment', 'user', 'content', 'created')