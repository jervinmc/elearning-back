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


class ClassRoomFiles(models.Model):
    folder_id = models.IntegerField(_('folder_id'),default=0.0)
    user_id = models.IntegerField(_('user_id'),default=0.0)
    author=models.CharField(_('author'),max_length=255,blank=True,null=True)
    file_name=models.CharField(_('file_name'),max_length=255,blank=True,null=True)
    files = models.FileField(
        _('files'), upload_to=nameFile, default="uploads/users_placeholder.png")
    class Meta:
        ordering = ["-id"]
