# Commit Message

```
feat: Add models, serializers, and seeder for Listings app

- Define Listing, Booking, and Review models in `listings/models.py`.
- Implement serializers for Listing and Booking in `listings/serializers.py`.
- Create a management command `seed.py` to populate the database with sample data.
- Run migrations and seed the database successfully.
```

# README File

# ALX Travel App

## Project Overview

This project is a travel listing application built with Django. It allows users to browse, book, and review travel listings. The application includes database models, serializers, and a seeder script for managing data.

## Features

- **Listings**: Browse travel destinations with descriptions, locations, and prices.
- **Bookings**: Users can book a listing for a specific date range.
- **Reviews**: Users can leave reviews with ratings and comments.

## Models

### Listing
- **title**: Title of the listing.
- **description**: Description of the listing.
- **location**: Location of the listing.
- **price_per_night**: Price per night for the listing.
- **created_at**: Timestamp of when the listing was created.

### Booking
- **listing**: Foreign key to the Listing model.
- **user**: Foreign key to the User model.
- **start_date**: Start date of the booking.
- **end_date**: End date of the booking.
- **total_price**: Total price for the booking.
- **created_at**: Timestamp of when the booking was created.

### Review
- **listing**: Foreign key to the Listing model.
- **user**: Foreign key to the User model.
- **rating**: Rating out of 5.
- **comment**: Review comment.
- **created_at**: Timestamp of when the review was created.

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Sand-raM/alx_travel_app_0x00.git
   ```
2. Navigate to the project directory:
   ```bash
   cd alx_travel_app_0x00
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Seed the database:
   ```bash
   python manage.py seed
   ```
6. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Usage

### API Endpoints
- **Listings**: View available travel destinations.
- **Bookings**: Book a listing for a specific date range.
- **Reviews**: Leave and view reviews for listings.

### Testing the Seeder
Run the following command to populate the database with sample data:
```bash
python manage.py seed
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.
