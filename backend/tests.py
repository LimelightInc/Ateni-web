from django.test import TestCase
from datetime import datetime
import os
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import *

class TestUser(TestCase):
    '''test class for AbstractUser model'''
    def setUp(self):
        self.user = User.objects.create_user(username='Linda', password='LindaMaina123', authorization_token="1008719970978-hb24n2dstb40o45d4feuo2ukqmcc6381.apps.googleusercontent.com", refresh_token='client_id')

    def tearDown(self):
        self.user.delete()

    def test_user_creation(self):
        self.assertIsInstance(self.user, User)
        self.user.save()
        self.assertIsInstance(self.user, User)


class ProfileTest(TestCase):
    ''' test class for Profile model'''
    def setUp(self):
        ''' method called before each test case'''
        self.user = User.objects.create_user(username='Walter', password='white-af', authorization_token="1008719970978-hb24n2dstb40o45d4feuo2ukqmcc6381.apps.googleusercontent.com", refresh_token='client_id')
        self.interest = Interest(name='IT')
        self.interest.save()

    def tearDown(self):
        ''' method to clear all setup instances after each test run '''
        self.user.delete()
        self.interest.delete()

    def test_profile_creation(self):
        ''' method to test profile instance is created only once for each user '''
        self.assertIsInstance(self.user.profile, Profile)
        self.user.save()
        self.assertIsInstance(self.user.profile, Profile)
