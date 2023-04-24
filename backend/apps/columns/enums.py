from django.db import models


class ColumnStatus(models.TextChoices):
    """Options for status fields for the Column entity"""
    on_working = "ON_WORKING"
    hold = "HOLD"
    out_date = "OUT_DATE"
    draft = "DRAFT"
