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


class Enrolled(models.Model):
    student_id = models.IntegerField(_('student_id'),default=0.0)
    code=models.CharField(_('code'),max_length=255,blank=True,null=True)
    status=models.CharField(_('status'),default='Not Archived',max_length=255,blank=True,null=True)
    class Meta:
        ordering = ["-id"]
