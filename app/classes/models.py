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


class Classes(models.Model):
    prof_id=models.CharField(_('prof_id'),max_length=255,blank=True,null=True)
    class_name=models.CharField(_('class_name'),max_length=255,blank=True,null=True)
    code=models.CharField(_('code'),max_length=255,blank=True,null=True)
    class Meta:
        ordering = ["-id"]
