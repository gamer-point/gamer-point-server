import uuid

from django.db.models import Model
from django.db.models import ForeignKey
from django.db.models import UUIDField
from django.db.models import DateTimeField
from django.db.models import CASCADE

class ForgetPassword(Model):
    """
    ForgetPassword id a model in order to store an uuid and the user.
    Gamer Point sends this uuid to user emails. Then the user can set a new password and the ForgetPassword entity is deleted
    The ForgetPassword lasts for 1 hour, then the row on database is deleted.
    """
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = ForeignKey('User', on_delete=CASCADE, null=False, related_name="User", default=0)
    created = DateTimeField(auto_now_add=True)
