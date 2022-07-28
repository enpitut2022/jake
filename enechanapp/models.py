from django.db import models
from django.utils import timezone
import uuid

# Create your models here.
class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable = False)
    date = date = models.DateField(verbose_name='日付', default=timezone.now)
    text = models.CharField(verbose_name='本文', max_length=10)