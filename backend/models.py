from django.db import models
from django.contrib.auth.models import User


class Interest(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatars/', default='default.jpg')
    twitter = models.URLField(null=True)
    linkedin = models.URLField(null=True)
    interest = models.ManyToManyField(Interest)

    def __str__(self):
        return f'{self.user.username}'


class InnerCircle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contacts = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}'s circle"

class Mowiki(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    editor = models.ForeignKey(InnerCircle, on_delete=models.CASCADE)
    content = models.TextField()
    date_uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}'s wiki"

class Level(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'


class Community(models.Model):
    admin = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='community_profile/', default='image.jpg')
    name = models.CharField(max_length=255)
    description = models.TextField()
    interest = models.ManyToManyField(Interest)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.name}'

class Project(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    live_link = models.URLField(null=True)
    repo_link = models.URLField(null=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    is_open_source = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    needs_contrib = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'

class Comment(models.Model):
    post = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username}'


class SubComment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Sub-comment by {self.user.username}'