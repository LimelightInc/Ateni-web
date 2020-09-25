from django.test import TestCase
from datetime import datetime
import os
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import *

class TestUser(TestCase):
    '''test class for AbstractUser model'''
    def setUp(self):
        self.user = User.objects.create_user(username='Linda', password='LindaMaina123')

    def tearDown(self):
        self.user.delete()

    def test_user_creation(self):
        self.assertIsInstance(self.user, User)
        self.user.save()
        self.assertIsInstance(self.user, User)


class TestProfile(TestCase):
    ''' test class for Profile model'''
    def setUp(self):
        ''' method called before each test case'''
        self.user = User.objects.create_user(username='Walter', password='white-af')

    def tearDown(self):
        ''' method to clear all setup instances after each test run '''
        self.user.delete()

    def test_profile_creation(self):
        ''' method to test profile instance is created only once for each user '''
        self.assertIsInstance(self.user.profile, Profile)
        self.user.save()
        self.assertIsInstance(self.user.profile, Profile)

        # self.image = SimpleUploadedFile("file.jpg", b"file_content", content_type="image/jpg")
        # self.profile = Profile(user=self.user, image=self.image, twitter='https://twitter.com/jamboNgala') #not adding linkedin to test that null field works

        # self.interest = self.profile.interest.create(name='IT')
        # self.interest.save()
        # self.assertEqual(self.user.profile, self.profile)
        # self.assertEqual(self.profile.interest.get(id=self.interest.id), self.interest)


class TestInterest(TestCase):
    ''' '''
    def setUp(self):
        self.interest = Interest(name='IT')

    def tearDown(self):
        self.interest.delete()

    def test_interest_creation(self):
        self.assertEqual(len(Interest.objects.all()), 0)
        self.interest.save()
        self.assertIsInstance(self.interest, Interest)


class TestInnerCircle(TestCase):
    ''' '''
    def setUp(self):
        self.user = User.objects.create_user(username='Walter', password='white-af')
        self.another_user = User.objects.create_user(username='Alejandro', password='chief-in-spector')
        self.third_user = User.objects.create_user(username='Rio', password='bazenga254')

    def tearDown(self):
        self.user.delete()
        self.another_user.delete()

    def test_circle_creation(self):
        self.current_user = InnerCircle(current_user=self.user.profile)
        self.current_user.save()
        self.current_user.contacts.add(self.another_user.profile)
        self.assertTrue(self.current_user.contacts.exists())

        # self.current_user.contacts.add(self.third_user.profile)
        # self.assertEqual(InnerCircle.objects.count(), 2)


class TestMowiki(TestCase):
    ''' '''
    def setUp(self):
        self.user = User.objects.create_user(username='David', password='Goliathhh')
        self.another_user = User.objects.create_user(username='Alejandro', password='chief-in-spector')

        self.current_user = InnerCircle(current_user=self.user.profile)
        self.current_user.save()
        self.current_user.contacts.add(self.another_user.profile)

    def tearDown(self):
        self.user.delete()

