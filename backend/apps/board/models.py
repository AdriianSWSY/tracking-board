import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django_extensions.db.models import TimeStampedModel

from apps.board.enums import BoardStatus, BoardUserRole


class Board(TimeStampedModel):
    """Board table representation to interact with code via ORM"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128, null=False, blank=False)
    description = models.CharField(max_length=256, null=True, blank=True)
    status = models.CharField(max_length=128, choices=BoardStatus.choices, default=BoardStatus.active)

    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="boards")
    members = models.ManyToManyField(get_user_model(), related_name="courses", through="BoardUser")

    class Meta:
        ordering = ['modified']


class BoardUser(TimeStampedModel):
    """BoardUser table store user per board"""
    role = models.CharField(max_length=128, choices=BoardUserRole.choices, default=BoardUserRole.user)

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="member_boards")
    board = models.ForeignKey("Board", on_delete=models.CASCADE, related_name="board_members")
