import os
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError


def validate_pdf_ext(value):
    """Validate if file extension is .pdf. Value is expected to be file"""
    ext = os.path.splitext(value.name)[1]
    if ext.lower() != '.pdf':
        raise ValidationError(_('PDF only is acceptable here.'))


def validate_csv_ext(value):
    """Validate if file extension is .csv. Value is expected to be file"""
    ext = os.path.splitext(value.name)[1]
    if ext.lower() != '.csv':
        raise ValidationError(_('CSV only is acceptable here.'))
