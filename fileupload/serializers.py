from rest_framework import serializers
from .models import Reviews


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'

class ReviewsSerializerSerializerPatch(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'
        extra_kwargs = {
            'book_id': {'required': False},
            'review_author': {'required': False},
            'review_date': {'required': False},
            'review_comment': {'required': False},
        }


