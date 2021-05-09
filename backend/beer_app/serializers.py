from rest_framework import serializers

from .models import Beer, UserComment


class BeerSerializer(serializers.ModelSerializer):
    raiting = serializers.FloatField()

    class Meta:
        model = Beer
        fields = '__all__'


class BeerListSerializer(BeerSerializer):

    class Meta:
        model = Beer
        fields = ['id', 'name', 'price', 'mark', 'updated_at', 'image', 'raiting']

    # def get_averrage_mark(self):
    #     pass

