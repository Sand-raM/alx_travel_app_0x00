from django.core.management.base import BaseCommand
from listings.models import Listing, Booking
from datetime import date

class Command(BaseCommand):
    help = "Seed the database with sample data"

    def handle(self, *args, **kwargs):
        # Clear existing data
        Listing.objects.all().delete()
        Booking.objects.all().delete()

        # Create sample listings
        listing1 = Listing.objects.create(
            name="Cozy Apartment",
            description="A cozy place to stay",
            price_per_night=75.50,
            location="Downtown",
        )
        listing2 = Listing.objects.create(
            name="Beachside Villa",
            description="Relax by the sea",
            price_per_night=150.00,
            location="Beachfront",
        )

        # Create sample bookings
        Booking.objects.create(
            listing=listing1,
            user="test_user1",
            start_date=date(2024, 12, 25),
            end_date=date(2024, 12, 30),
            total_price=377.50,
        )
        Booking.objects.create(
            listing=listing2,
            user="test_user2",
            start_date=date(2025, 1, 1),
            end_date=date(2025, 1, 7),
            total_price=900.00,
        )

        self.stdout.write("Sample data seeded successfully!")
