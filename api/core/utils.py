from django.utils.translation import gettext_lazy as _
from rest_framework import serializers


def get_lead_id(kwargs):
    lead_id = kwargs.get('lead_pk')
    try:
        int(lead_id)
    except ValueError:
        raise serializers.ValidationError({'lead_pk': _('invalid lead ID')})
    return lead_id
