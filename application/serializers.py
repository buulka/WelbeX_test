from rest_framework import serializers
from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'date', 'name', 'count', 'distance')


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('sort_value', 'selected_clause', 'selected_column')