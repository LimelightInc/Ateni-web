from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    authorizaton_token = models.TextField()
    refresh_token = models.TextField()


class Interest(models.Model):
    name = models.CharField(max_length=255)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatars/', default='default.jpg')
    twitter = models.URLField(null=True)
    linkedin = models.URLField(null=True)
    interest = models.ManyToManyField(Interest)

    def __str__(self):
        return f'{self.user.username}'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



class InnerCircle(models.Model):
    contacts = models.ManyToManyField(Profile, related_name='contact')
    current_user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='current_user')



class Mowiki(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    editor = models.ForeignKey(InnerCircle, on_delete=models.CASCADE)
    content = models.TextField()
    date_uploaded = models.DateTimeField(auto_now_add=True)



class Community(models.Model):
    admin = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='community_profile/', default='image.jpg')
    name = models.CharField(max_length=255)
    description = models.TextField()
    interest = models.ManyToManyField(Interest)
    CHOICES = ( #level choices
        ('beginner', 'Beginner friendly'),
        ('intermediate', 'Intermediate'),
        ('expert', 'Expert'),
    )
    level = models.CharField(max_length=255 ,choices=CHOICES)


class Project(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    live_link = models.URLField(null=True)
    repo_link = models.URLField(null=True)
    description = models.TextField()
    deadline = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    is_open_source = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    needs_contrib = models.BooleanField(default=False)


class Comment(models.Model):
    post = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)


class SubComment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)