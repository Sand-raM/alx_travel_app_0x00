from rest_framework import serializers
from .models import Listing, Booking, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ListingSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)  # Nested serializer for reviews

    class Meta:
        model = Listing
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    listing = serializers.StringRelatedField()  # Use __str__ representation for Listing
    listing_id = serializers.PrimaryKeyRelatedField(
        queryset=Listing.objects.all(), source="listing", write_only=True
    )  # Allow clients to specify listing ID

    class Meta:
        model = Booking
        fields = ['id', 'user', 'listing', 'listing_id', 'start_date', 'end_date', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

    def validate(self, data):
        """
        Custom validation to ensure that the booking dates are valid.
        """
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        if start_date and end_date and start_date > end_date:
            raise serializers.ValidationError("Start date cannot be later than end date.")
        return data
