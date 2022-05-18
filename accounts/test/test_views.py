from urllib import response
from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import User

# Testcase of UserCreateAPIview
class UserCreateAPIView(TestCase):
    def create_Account(self,phone="9841093490"):
        return User.objects.ceate(phone=phone)

    def test_Account(self):
        url = reverse('signup')
        resp = self.client.get(url)
        self.assertEqual(len(resp.data),1)

# Testcase for UserUpdateAPIView
class UserUpdateAPIView(TestCase):
    def create_Account(self,phone="9841093490"):
        return User.objects.ceate(phone=phone)

    def test_Account(self):
        url = reverse('update',args=[1])
        resp = self.client.get(url)
        self.assertEqual(len(resp.data),1)

# Testcase for UserRetrieveAPIVIew
class UserRetrieveAPIView(TestCase):
    def create_Account(self,phone="9841093490"):
        return User.objects.ceate(phone=phone)

    def test_Account(self):
        url = reverse('user-retrieve',args=[100])
        resp = self.client.get(url)
        self.assertEqual(len(resp.data),1)

# Testcase for UserPasswordResetRequestAPIView
class UserPasswordResetRequestAPIView(TestCase):
    def create_Account(self,phone="9841053490"):
        return User.objects.create(phone=phone)
    
    def test_Account(self):
        url = reverse('reset-password')
        resp = self.client.get(url)
        self.assertEqual(len(resp.data),1)
        
# Testcase for UserPasswordResetConfirmAPIView
class UserPasswordResetConfirmAPIView(TestCase):
    def create_Account(self,phone="9841093490"):
        return User.objects.create(phone=phone)

    def test_Account(self):
        url = reverse('reset-password')
        resp = self.client.get(url)
        self.assertEqual(len(resp.data),1)

# Testcase for UserProfileAPIView
class UserProfileAPIView(TestCase):
    def create_Account(self,phone="9841012490"):
        return User.objects.create(phone=phone)

    def test_Account(self):
        url = reverse('profile')
        resp = self.client.get(url)
        self.assertEqual(len(resp.data),1)

# Testcase for UserActivateAPIView
class UserActivateAPIView(TestCase):
    def create_Account(self,phone="9841021490"):
        return User.objects.create(phone=phone)
    
    def test_Account(self):
        url = reverse('opt-activate',args=[100])
        resp = self.client.get(url)
        self.assertEqual(len(resp.data),1)

# Testcase for UserResetPasswordOTPConfirmAPIView
class UserResetPasswordOTPConfirmAPIView(TestCase):
    def create_Account(self,phone="9841032490"):
        return User.objects.create(phone=phone)
    
    def test_Account(self):
        url = reverse('reset-password')
        resp = self.client.get(url)
        self.assertEqual(len(resp.data),1)
