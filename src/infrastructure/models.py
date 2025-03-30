from tortoise import fields
from tortoise.models import Model
import uuid


class Users(Model):
    id = fields.UUIDField(pk=True, default=uuid.uuid4)
    name = fields.CharField(unique=True, max_length=100, null=False)
    password = fields.TextField(null=False)
    connected_users = fields.ManyToManyField("models.Users", related_name="connections")
