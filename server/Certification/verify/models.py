from django.db import models

# Create your models here.
import datetime,userena
from Certification.settings import *
class VerifyUsers(models.Model):
    user = models.ForeignKey(userena)
    pubkey = models.TextField(default='')
    verify_code = models.CharField()
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