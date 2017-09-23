from rest_framework import serializers
from .models import Company, Dock
import datetime


class CompanySerializer(serializers.ModelSerializer):
    """Serializer to map the Product Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Company
        fields = ('pk', 'name', 'initials')


class DockSerializer(serializers.ModelSerializer):
    """Serializer to map the Product Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Dock
        fields = ('pk', 'initials', 'value', 'date', 'company')
