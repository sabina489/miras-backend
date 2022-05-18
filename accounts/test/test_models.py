# from datetime import date, datetime, timedelta
from ast import Try
from logging import exception
from django.utils import timezone
from django.test import TestCase
from django.db import models
import accounts
from accounts.models import Role,User,Profile


# Testcase for User
class UserTest(TestCase):
    def UserNew(self,phone="9821053490"):
        return User.objects.create(phone=phone)
    # self.otp_reset_expiry
    def test_is_otp_time_valid(self):
        time_now = timezone.datetime.now()
        time_now = timezone.make_aware(time_now, timezone.utc)
        time_1_min_after_now = time_now+timezone.timedelta(minutes=1)
        usernew = self.UserNew()
        usernew.otp_reset_expiry = time_1_min_after_now
        # print('******', usernew.is_otp_reset_time_valid)
        self.assertTrue(usernew.is_otp_reset_time_valid)

    # before_now
    def test_is_otp_time_invalid(self):
        time_recent = timezone.datetime.now()
        time_recent = timezone.make_aware(time_recent, timezone.utc)
        time_1_min_before_now = time_recent-timezone.timedelta(minutes=1)
        userrecent = self.UserNew()
        userrecent.otp_reset_expiry = time_1_min_before_now
        # print('***', userrecent.is_otp_reset_time_valid)
        self.assertFalse(userrecent.is_otp_reset_time_valid)

    # validate_otp
    def test_validate_otp_valid(self):
        value = 1234
        usernew = self.UserNew()
        usernew.otp = '1234'
        self.assertTrue(usernew.validate_otp(value))
    
   
    # invalid_otp
    def test_validate_otp_invalid(self):
        value = 5987
        usernew = self.UserNew()
        usernew.otp = '0998'
        self.assertFalse(usernew.validate_otp(value))

    # valid_otp_reset
    def test_validate_otp_reset_valid(self):
        value = 5987
        usernew = self.UserNew()
        usernew.otp_reset = '5987'
        self.assertTrue(usernew.validate_otp_reset(value))
    
     # invalid_otp_reset
    def test_validate_otp_reset_invalid(self):
        value = 5987
        usernew = self.UserNew()
        usernew.otp_reset = '5987'
        self.assertTrue(usernew.validate_otp_reset(value))

    # self.otp_expiry
    def test_is_otp_time_valid(self):
        time_now = timezone.datetime.now()
        time_now = timezone.make_aware(time_now, timezone.utc)
        time_1_min_after_now = time_now + timezone.timedelta(minutes=1)
        usernew1 = self.UserNew()
        usernew1.otp_expiry = time_1_min_after_now
        # print('##', usernew1.is_otp_time_valid)
        self.assertTrue(usernew1.is_otp_time_valid)
    
    # before_now()
    def test_is_otp_time_invalid(self):
        time_recent = timezone.datetime.now()
        time_recent = timezone.make_aware(time_recent, timezone.utc)
        time_1_min_before_now = time_recent - timezone.timedelta(minutes=1)
        usernew2 = self.UserNew()
        usernew2.otp_expiry = time_1_min_before_now
        # print('!!',usernew2.is_otp_time_valid)
        self.assertFalse(usernew2.is_otp_time_valid)

        #test for invalid users
    def test_phone_invalid(self):
        invalid_phone = '98123490'
        try:
            User.objects.create(phone=invalid_phone)
        except Exception as e:
            self.assertRaisesMessage(e, "Enter a valid phonenumber 9XXXXXXXXX")
    

