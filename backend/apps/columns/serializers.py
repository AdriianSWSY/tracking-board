from rest_framework import serializers

from apps.columns.models import Column


class ColumnSerializer(serializers.ModelSerializer):
    """
    Serializer for Column model.

    This serializer converts Column instances to JSON and vice versa.
    """

    class Meta:
        model = Column
        fields = '__all__'

        # `created` and `updated` fields are inherited from the TimeStampedModel base class and should not be modified.
        read_only_fields = ["created", "updated", "creator"]
