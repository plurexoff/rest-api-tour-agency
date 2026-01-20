"""
Модели данных для REST API
"""
from datetime import datetime


class Tour:
    """Model for tours"""
    def __init__(self, id, destination, description, price, duration_days, available_slots, created_at=None):
        self.id = id
        self.destination = destination
        self.description = description
        self.price = price
        self.duration_days = duration_days
        self.available_slots = available_slots
        self.created_at = created_at or datetime.utcnow()

    def to_dict(self):
        return {
            'id': self.id,
            'destination': self.destination,
            'description': self.description,
            'price': self.price,
            'duration_days': self.duration_days,
            'available_slots': self.available_slots,
            'created_at': self.created_at.isoformat()
        }


class User:
    """Model for users"""
    def __init__(self, id, name, email, phone, created_at=None):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.created_at = created_at or datetime.utcnow()

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'created_at': self.created_at.isoformat()
        }


class Booking:
    """Model for bookings"""
    def __init__(self, id, user_id, tour_id, booking_date, status, created_at=None):
        self.id = id
        self.user_id = user_id
        self.tour_id = tour_id
        self.booking_date = booking_date
        self.status = status  # 'pending', 'confirmed', 'cancelled'
        self.created_at = created_at or datetime.utcnow()

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'tour_id': self.tour_id,
            'booking_date': self.booking_date,
            'status': self.status,
            'created_at': self.created_at.isoformat()
        }
