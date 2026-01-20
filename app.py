"""
REST API для Тур-Агентства на Flask
"""
import json
from datetime import datetime
from flask import Flask, request, jsonify
from flask_cors import CORS
from models import Tour, User, Booking

app = Flask(__name__)
CORS(app)

# В оперативная память (в реальных приложениях используйте базу данных)
tours = [
    Tour(1, 'Мальдивы', 'Рай на земле с кристальным морем', 2500.00, 7, 10),
    Tour(2, 'Таиланд', 'Экзотика и релакс', 1500.00, 5, 15),
    Tour(3, 'Египет', 'Пирамиды и история', 1800.00, 6, 8),
]

users = [
    User(1, 'Олег Петров', 'oleg@example.com', '+7 900 111 22 33'),
    User(2, 'Мария Сидорова', 'maria@example.com', '+7 900 444 55 66'),
]

bookings = [
    Booking(1, 1, 1, '2026-02-01T10:00:00', 'confirmed'),
    Booking(2, 2, 2, '2026-03-15T14:00:00', 'pending'),
]

# Генераторы ID
next_tour_id = 4
next_user_id = 3
next_booking_id = 3


# ======== Основные эндпоинты ========

@app.route('/api/tours', methods=['GET'])
def get_all_tours():
    """Получить все туры"""
    return jsonify([tour.to_dict() for tour in tours]), 200


@app.route('/api/tours/<int:tour_id>', methods=['GET'])
def get_tour(tour_id):
    """Получить тур по ID"""
    tour = next((t for t in tours if t.id == tour_id), None)
    if not tour:
        return jsonify({'error': 'Тур не найден'}), 404
    return jsonify(tour.to_dict()), 200


@app.route('/api/tours', methods=['POST'])
def create_tour():
    """Составление нового тура"""
    global next_tour_id
    
    data = request.get_json()
    
    # Проверка полей
    required_fields = ['destination', 'price', 'duration_days', 'available_slots']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Нехватает обязательные поля'}), 400
    
    try:
        new_tour = Tour(
            id=next_tour_id,
            destination=data['destination'],
            description=data.get('description', ''),
            price=float(data['price']),
            duration_days=int(data['duration_days']),
            available_slots=int(data['available_slots'])
        )
        tours.append(new_tour)
        next_tour_id += 1
        return jsonify(new_tour.to_dict()), 201
    except (ValueError, TypeError) as e:
        return jsonify({'error': f'Невалидные данные: {str(e)}'}), 400


@app.route('/api/tours/<int:tour_id>', methods=['PUT'])
def update_tour(tour_id):
    """Обновление тура"""
    tour = next((t for t in tours if t.id == tour_id), None)
    if not tour:
        return jsonify({'error': 'Тур не найден'}), 404
    
    data = request.get_json()
    
    # Обновление полей
    if 'destination' in data:
        tour.destination = data['destination']
    if 'description' in data:
        tour.description = data['description']
    if 'price' in data:
        tour.price = float(data['price'])
    if 'duration_days' in data:
        tour.duration_days = int(data['duration_days'])
    if 'available_slots' in data:
        tour.available_slots = int(data['available_slots'])
    
    return jsonify(tour.to_dict()), 200


@app.route('/api/tours/<int:tour_id>', methods=['DELETE'])
def delete_tour(tour_id):
    """Удаление тура"""
    global tours
    tour = next((t for t in tours if t.id == tour_id), None)
    if not tour:
        return jsonify({'error': 'Тур не найден'}), 404
    
    tours = [t for t in tours if t.id != tour_id]
    return '', 204


# ======== Пользователи ========

@app.route('/api/users', methods=['GET'])
def get_all_users():
    """Получить всех пользователей"""
    return jsonify([user.to_dict() for user in users]), 200


@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Получить пользователя по ID"""
    user = next((u for u in users if u.id == user_id), None)
    if not user:
        return jsonify({'error': 'Пользователь не найден'}), 404
    return jsonify(user.to_dict()), 200


@app.route('/api/users', methods=['POST'])
def create_user():
    """Осоставление нового пользователя"""
    global next_user_id
    
    data = request.get_json()
    
    required_fields = ['name', 'email', 'phone']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Нехватает обязательные поля'}), 400
    
    new_user = User(
        id=next_user_id,
        name=data['name'],
        email=data['email'],
        phone=data['phone']
    )
    users.append(new_user)
    next_user_id += 1
    return jsonify(new_user.to_dict()), 201


@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """Обновление пользователя"""
    user = next((u for u in users if u.id == user_id), None)
    if not user:
        return jsonify({'error': 'Пользователь не найден'}), 404
    
    data = request.get_json()
    
    if 'name' in data:
        user.name = data['name']
    if 'email' in data:
        user.email = data['email']
    if 'phone' in data:
        user.phone = data['phone']
    
    return jsonify(user.to_dict()), 200


@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Удаление пользователя"""
    global users
    user = next((u for u in users if u.id == user_id), None)
    if not user:
        return jsonify({'error': 'Пользователь не найден'}), 404
    
    users = [u for u in users if u.id != user_id]
    return '', 204


# ======== Бронирования ========

@app.route('/api/bookings', methods=['GET'])
def get_all_bookings():
    """Получить все бронирования"""
    return jsonify([booking.to_dict() for booking in bookings]), 200


@app.route('/api/bookings/<int:booking_id>', methods=['GET'])
def get_booking(booking_id):
    """Получить бронирование по ID"""
    booking = next((b for b in bookings if b.id == booking_id), None)
    if not booking:
        return jsonify({'error': 'Бронирование не найдено'}), 404
    return jsonify(booking.to_dict()), 200


@app.route('/api/bookings', methods=['POST'])
def create_booking():
    """Составление нового бронирования"""
    global next_booking_id
    
    data = request.get_json()
    
    required_fields = ['user_id', 'tour_id', 'booking_date']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Нехватает обязательные поля'}), 400
    
    # Проверка существования пользователя и тура
    user_exists = any(u.id == data['user_id'] for u in users)
    tour_exists = any(t.id == data['tour_id'] for t in tours)
    
    if not user_exists or not tour_exists:
        return jsonify({'error': 'Невалидные user_id или tour_id'}), 400
    
    new_booking = Booking(
        id=next_booking_id,
        user_id=data['user_id'],
        tour_id=data['tour_id'],
        booking_date=data['booking_date'],
        status=data.get('status', 'pending')
    )
    bookings.append(new_booking)
    next_booking_id += 1
    return jsonify(new_booking.to_dict()), 201


@app.route('/api/bookings/<int:booking_id>', methods=['PUT'])
def update_booking(booking_id):
    """Обновление бронирования"""
    booking = next((b for b in bookings if b.id == booking_id), None)
    if not booking:
        return jsonify({'error': 'Бронирование не найдено'}), 404
    
    data = request.get_json()
    
    if 'status' in data:
        booking.status = data['status']
    if 'booking_date' in data:
        booking.booking_date = data['booking_date']
    
    return jsonify(booking.to_dict()), 200


@app.route('/api/bookings/<int:booking_id>', methods=['DELETE'])
def delete_booking(booking_id):
    """Удаление бронирования"""
    global bookings
    booking = next((b for b in bookings if b.id == booking_id), None)
    if not booking:
        return jsonify({'error': 'Бронирование не найдено'}), 404
    
    bookings = [b for b in bookings if b.id != booking_id]
    return '', 204


# ======== Сервисные эндпоинты ========

@app.route('/health', methods=['GET'])
def health_check():
    """Проверка статуса сервера"""
    return jsonify({
        'status': 'healthy',
        'message': 'API is running',
        'timestamp': datetime.utcnow().isoformat()
    }), 200


@app.route('/api', methods=['GET'])
def api_info():
    """Информация об API"""
    return jsonify({
        'name': 'TravelVibe Tour Agency API',
        'version': '1.0.0',
        'endpoints': {
            'tours': '/api/tours',
            'users': '/api/users',
            'bookings': '/api/bookings'
        }
    }), 200


# ======== Обработка ошибок ========

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Ресурс не найден'}), 404


@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Ошибка сервера'}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
