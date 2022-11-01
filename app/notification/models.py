from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid


from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid
from django.utils import timezone
# Create your models here.

def nameFile(instance, filename):
    """
    Custom function for naming image before saving.
    """
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)

    return 'uploads/{filename}'.format(filename=filename)


class Notification(models.Model):
    user_id = models.IntegerField(_('user_id'),default=0.0)
    title=models.CharField(_('title'),max_length=255,blank=True,null=True)
    date_from=models.DateTimeField(_('date_from'), null=False,blank=False,default=timezone.now)
    class Meta:
        ordering = ["-id"]
