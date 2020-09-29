from django.test import TestCase
from datetime import datetime
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import *


class TestUser(TestCase):
    '''test class for User model'''
    def setUp(self):
        ''' method called before each test case'''
        self.user = User.objects.create_user(username='Linda', password='LindaMaina123')

    def tearDown(self):
        ''' method to clear all setup instances after each test run '''
        self.user.delete()

    def test_user_creation(self):
        ''' method to test creation of user'''
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
        self.image = SimpleUploadedFile("file.jpg", b"file_content", content_type="image/jpg")
        self.profile = Profile(user=self.user, image=self.image, twitter='https://twitter.com/jamboNgala') #not adding linkedin to test that null field works
        self.profile.save()
        self.interest = self.profile.interest.create(name='IT')

        self.assertIsInstance(self.user.profile, Profile)
        self.assertEqual(self.user.profile, self.profile)
        self.assertEqual(Profile.objects.filter(interest=self.interest).count(), 1)


class TestInterest(TestCase):
    ''' test class for Interest model '''
    def setUp(self):
        ''' method called before each test case'''
        self.interest = Interest(name='IT')

    def tearDown(self):
        ''' method to clear all setup instances after each test run '''
        self.interest.delete()

    def test_interest_creation(self):
        ''' method to test correct creation of interest instances '''
        self.assertEqual(len(Interest.objects.all()), 0)
        self.interest.save()
        self.assertIsInstance(self.interest, Interest)


class TestInnerCircle(TestCase):
    ''' test class for InnerCircle model '''
    def setUp(self):
        ''' method called before each test case'''
        self.user = User.objects.create_user(username='Walter', password='white-af')
        self.user.save()

        self.another_user = User.objects.create_user(username='Alejandro', password='chief-in-spector')
        self.another_user.save()
        self.another_profile = Profile(user=self.another_user)
        self.another_profile.save()

        self.third_user = User.objects.create_user(username='Rio', password='bazenga254')
        self.third_user.save()
        self.third_profile = Profile(user=self.third_user)
        self.third_profile.save()

    def tearDown(self):
        ''' method to clear all setup instances after each test run '''
        self.user.delete()
        self.another_user.delete()
        self.third_user.delete()

    def test_circle_creation(self):
        ''' method to test innercircle instances '''
        self.follower1 = InnerCircle(user=self.user, contacts=self.another_profile)
        self.follower1.save()
        self.follower2 = InnerCircle(user=self.user, contacts=self.third_profile)
        self.follower2.save()

        self.assertEqual(len(InnerCircle.objects.filter(user=self.user).all()), 2)


class TestMowiki(TestCase):
    ''' test class for Mowiki model '''
    def setUp(self):
        ''' method called before each test case '''
        self.user = User.objects.create_user(username='David', password='Goliathhh')
        self.user.save()

        self.another_user = User.objects.create_user(username='Alejandro', password='chief-in-spector')
        self.user.save()
        self.another_profile = Profile(user=self.another_user)
        self.another_profile.save()

        self.someone_else = User.objects.create_user(username='SashaSloan', password='house-with-no-mirrors')
        self.someone_else.save()
        self.some_other_profile = Profile(user=self.someone_else)
        self.some_other_profile.save()

        self.follower1 = InnerCircle(user=self.user, contacts=self.another_profile)
        self.follower1.save()
        self.follower2 = InnerCircle(user=self.user, contacts=self.some_other_profile)
        self.follower2.save()

    def tearDown(self):
        ''' method to clear all setup instances after each test run '''
        self.user.delete()
        self.another_user.delete()
        self.someone_else.delete()

    def test_wiki_creation(self):
        ''' method to test wiki instances '''
        self.old_wiki = Mowiki(user=self.user, editor=self.follower1, content='I have opinions about you', date_uploaded=datetime.now())
        self.old_wiki.save()

        self.new_wiki = Mowiki(user=self.user, editor=self.follower2, content='I have more opinions about you', date_uploaded=datetime.now())
        self.new_wiki.save()

        self.assertIsInstance(self.old_wiki, Mowiki)
        self.assertEqual(len(Mowiki.objects.filter(user=self.user).all()), 2)


class TestLevel(TestCase):
    ''' test class for Level model '''
    def setUp(self):
        ''' method called before each test case '''
        self.level = Level(name='expert')

    def tearDown(self):
        ''' method to clear all setup instances after each test run '''
        self.level.delete()

    def test_level_creation(self):
        ''' method to test level instances '''
        self.assertEqual(len(Level.objects.all()), 0)
        self.level.save()
        self.assertIsInstance(self.level, Level)
        self.assertEqual(len(Level.objects.all()), 1)


class TestCommunity(TestCase):
    ''' test class for Community model '''
    def setUp(self):
        ''' method called before each test case '''
        self.user = User.objects.create_user(username='MrAdmin', password='super-secretpasswd')
        self.user.save()
        self.profile = Profile(user=self.user)
        self.profile.save()
        
        self.image = SimpleUploadedFile("file.jpg", b"file_content", content_type="image/jpg")
        self.level = Level(name='beginner')
        self.level.save()
        
    def tearDown(self):
        ''' method to clear all setup instances after each test run '''
        self.user.delete()
        self.community.delete()

    def test_community_creation(self):
        ''' method to test community instances '''
        self.community = Community(admin=self.profile, image=self.image, name='Django Brains', description='We are a community of django lovers who aim at guiding new devs into te amazing world that is Django', level=self.level)
        self.community.save()
        self.interest = self.community.interest.create(name='Django')

        self.assertIsInstance(self.community, Community)
        self.assertEqual(self.community.name, 'Django Brains')
        self.assertEqual(Community.objects.filter(interest=self.interest).count(), 1)


class TestProject(TestCase):
    ''' test class for Project model '''
    def setUp(self):
        ''' method called before each test case '''
        self.user = User.objects.create_user(username='MrAdmin', password='super-secretpasswd')
        self.user.save()
        self.profile = Profile(user=self.user)
        self.profile.save()

        self.community = Community(admin=self.profile, name='Moi Uni CS', description='tbd')
        self.community.save()
        
    def tearDown(self):
        ''' method to clear all setup instances after each test run '''
        self.user.delete()
        self.community.delete()

    def test_community(self):
        ''' method to test project instances '''
        # deployed project for feedback
        self.project19 = Project(user=self.profile, community=self.community, name='Project19', live_link='https://www.google.com', repo_link='github.com/karenngala/Repo', description='Just completed. Lmk what you think', created=datetime.now())
        self.project19.save()
        # contributive project with private repo
        self.project714 = Project(user=self.profile, community=self.community,name='Project714', description='Looking for 1 Flutter web dev and 1 graphic designer to collaborate on a Social app project....', created=datetime.now(), is_paid=True, needs_contrib=True, deadline=datetime.today())
        self.project714.save()

        self.assertEqual(len(Project.objects.filter(user=self.profile).all()), 2)
        self.assertEqual(self.project19.name, 'Project19')


class TestComment(TestCase):
    ''' test class for Comment model '''
    def setUp(self):
        ''' method called before each test case '''
        self.owner = User.objects.create_user(username='MainSqueeze', password='super-secretpasswd')
        self.owner.save()
        self.profile = Profile(user=self.owner)
        self.profile.save()

        self.user = User.objects.create_user(username='CallMeByYourName', password='super-secretpasswd')
        self.user.save()

        self.community = Community(admin=self.profile, name='Moi Uni CS', description='tbd')
        self.community.save()

        self.project19 = Project(user=self.profile, community=self.community, name='Project19', live_link='https://www.google.com', repo_link='github.com/karenngala/Repo', description='Just completed. Lmk what you think', created=datetime.now())
        self.project19.save()

        self.project714 = Project(user=self.profile, community=self.community,name='Project714', description='Looking for 1 Flutter web dev and 1 graphic designer to collaborate on a Social app project....', created=datetime.now(), is_paid=True, needs_contrib=True, deadline=datetime.today())
        self.project714.save()

    def tearDown(self):
        ''' method to clear all setup instances after each test run '''
        self.user.delete()
        self.owner.delete()
        self.project19.delete()
        self.project714.delete()

    def test_comment_creation(self):
        ''' method to test comment instances '''
        self.comment = Comment(post=self.project19, user=self.user, content='I think this is absolutely brilliant', created=datetime.now())
        self.comment.save()

        self.assertEqual(len(Comment.objects.filter(post=self.project19).all()), 1)
        self.assertEqual(len(Comment.objects.filter(post=self.project714).all()), 0)

        self.community.delete()
        self.assertIsInstance(self.project19, Project) #projects still exist even when community does not


class TestSubComment(TestCase):
    ''' test class for SubComment model '''
    def setUp(self):
        ''' method called before each test case '''
        self.owner = User.objects.create_user(username='MainSqueeze', password='super-secretpasswd')
        self.owner.save()
        self.profile = Profile(user=self.owner)
        self.profile.save()

        self.user = User.objects.create_user(username='CallMeByYourName', password='super-secretpasswd')
        self.user.save()
        self.another_user = User.objects.create_user(username='Supporter', password='super-secretpasswd')
        self.another_user.save()

        self.community = Community(admin=self.profile, name='Moi Uni CS', description='tbd')
        self.community.save()

        self.project19 = Project(user=self.profile, community=self.community, name='Project19', live_link='https://www.google.com', repo_link='github.com/karenngala/Repo', description='Just completed. Lmk what you think', created=datetime.now())
        self.project19.save()

        self.comment = Comment(post=self.project19, user=self.user, content='I think this is absolutely brilliant', created=datetime.now())
        self.comment.save()

    def tearDown(self):
        ''' method to clear all setup instances after each test run '''
        self.user.delete()
        self.owner.delete()
        self.another_user.delete()
        self.community.delete()
        self.project19.delete()
        self.comment.delete()

    def test_comment_creation(self):
        ''' method to test sub-comment instances '''
        self.sub_comment = SubComment(comment=self.comment, user=self.another_user, content='I agree 100%', created=datetime.now())
        self.sub_comment.save()

        self.assertEqual(len(SubComment.objects.filter(comment=self.comment).all()), 1)