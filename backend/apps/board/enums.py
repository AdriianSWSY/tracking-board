from django.db import models


class BoardStatus(models.TextChoices):
    """Options for status fields for the Board entity"""
    active = "ACTIVE"
    archived = "ARCHIVED"
    deleted = "DELETED"