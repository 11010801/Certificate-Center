from django.db import models

# Create your models here.
import datetime
from Certification.settings import *
from profiles.models import Profile
class VerifyUsers(models.Model):
    user = models.ForeignKey(Profile)
    pubkey = models.TextField(default='')
    verify_code = models.CharField(max_length=80)
    build_time = models.DateTimeField(auto_now=False)
    def has_pubkey(self):
        if self.pubkey:
            return True
        else:
            return False
    def was_code_expired(self):
        if not self.verify_code or self.build_time + KEY_EXPIRE_TIMEDELTA < datetime.datetime.now():
            return True
        else:
            return False