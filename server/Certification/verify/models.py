from django.db import models

# Create your models here.
import datetime
from Certification.settings import *
from userena.utils import user_model_label
class VerifyUsers(models.Model):
    user = models.ForeignKey(user_model_label)
    pubkey = models.TextField(default = '')
    verify_code = models.CharField(max_length = 80)
    build_time = models.DateTimeField(default = datetime.datetime.now())
#    verified_times = models.IntegerField(default = 0)
#    verify_url = models.URLField()
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