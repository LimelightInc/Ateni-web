from rest_framework import serializers
from backend.models import *

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')


class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password', 'username')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username','email', 'date_joined')

class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        fields = ('id', 'name')

class UserProfileSerializer(serializers.ModelSerializer):
        user = UserSerializer()
        interest = InterestSerializer(many=True)

        class Meta:
            model = Profile
            fields = ('user', 'image', 'twitter', 'linkedin', 'interest')

class InnerCircleSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    contacts = UserProfileSerializer(many=True)

    class Meta:
        model = InnerCircle
        fields = ('user', 'contacts')


# class MowikiSerializer(serializers.ModelSerializer):
#     user = UserSerializer()
#     editor = UserSerializer()

#     class Meta:
#         model = InnerCircle
#         fields = ('user', 'editor', 'content', 'date_uploaded')


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ('id', 'name')


class CommunityDetailSerializer(serializers.ModelSerializer):
    admin = UserProfileSerializer()
    interest = InterestSerializer(many=True)
    level = LevelSerializer()

    class Meta:
        model = Community
        fields = ('admin', 'logo', 'cover_photo', 'name', 'description', 'interest', 'level')


class CommunityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = ('id','name')


class ProjectDetailSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer()
    community = CommunityListSerializer()

    class Meta:
        model = Project
        fields = ('user', 'community', 'image', 'live_link', 'repo_link', 'name', 'description', 'deadline', 'created', 'is_open_source', 'is_paid', 'needs_contrib')


class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id','name')


class CommentDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    post = ProjectListSerializer()

    class Meta:
        model = Comment
        fields = ('post', 'user', 'content', 'created')


class CommentListSerializer(serializers.ModelSerializer):
    post = ProjectListSerializer()

    class Meta:
        model = Comment
        fields = ('id', 'post')


class SubCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    comment = CommentListSerializer()

    class Meta:
        model = SubComment
        fields = ('comment', 'user', 'content', 'created')
