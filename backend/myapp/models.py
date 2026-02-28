from django.db import models, transaction
import uuid
from django.conf import settings
from django.utils import timezone
# Create your models here.


class Tenant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    industry = models.CharField(max_length=100)
    size = models.CharField(max_length=50)  # SME, Enterprise
    country = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return f'{self.name}'