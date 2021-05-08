from rest_framework import serializers

from .models import Beer, UserComment


class BeerListSerializer(serializers.ModelSerializer):
    # average_mark = serializers.SerializerMethodField()

    class Meta:
        model = Beer
        fields = ['id', 'name', 'price', 'mark', 'updated_at', 'image']

    # def get_averrage_mark(self):
    #     pass