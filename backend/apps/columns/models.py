from django.contrib.auth import get_user_model
from django.db import models
from django_extensions.db.models import TimeStampedModel

from apps.columns.enums import ColumnStatus


class Column(TimeStampedModel):
    """
    Represents a column on a board.

    Each column has a name, status, board, and creator.
    """

    name = models.CharField(max_length=128, null=False, blank=False)
    status = models.CharField(max_length=128, choices=ColumnStatus.choices, default=ColumnStatus.on_working)

    # Each column belongs to a board.
    board = models.ForeignKey("board.Board", on_delete=models.CASCADE, related_name="columns")

    # Each column has a creator.
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="columns")
