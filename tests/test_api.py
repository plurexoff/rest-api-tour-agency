"""
Примеры тестов для REST API
"""
import json
from flask import Flask
from app import app as flask_app


def test_get_all_tours():
    """Test GET /api/tours"""
    client = flask_app.test_client()
    response = client.get('/api/tours')
    
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)
    assert len(data) > 0
    assert 'id' in data[0]
    assert 'destination' in data[0]
    print("✅ GET /api/tours ок")


def test_get_single_tour():
    """Test GET /api/tours/1"""
    client = flask_app.test_client()
    response = client.get('/api/tours/1')
    
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['id'] == 1
    assert 'destination' in data
    print("✅ GET /api/tours/1 ок")


def test_create_tour():
    """Test POST /api/tours"""
    client = flask_app.test_client()
    new_tour = {
        'destination': 'Норвегия',
        'description': 'Авроры и фьюрды',
        'price': 3000,
        'duration_days': 10,
        'available_slots': 5
    }
    
    response = client.post('/api/tours',
                          data=json.dumps(new_tour),
                          content_type='application/json')
    
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['destination'] == 'Норвегия'
    print("✅ POST /api/tours ок")


def test_update_tour():
    """Test PUT /api/tours/1"""
    client = flask_app.test_client()
    updated_data = {'price': 2000}
    
    response = client.put('/api/tours/1',
                         data=json.dumps(updated_data),
                         content_type='application/json')
    
    assert response.status_code == 200
    data = json.loads(response.data)
    print("✅ PUT /api/tours/1 ок")


def test_get_all_users():
    """Test GET /api/users"""
    client = flask_app.test_client()
    response = client.get('/api/users')
    
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)
    print("✅ GET /api/users ок")


def test_create_user():
    """Test POST /api/users"""
    client = flask_app.test_client()
    new_user = {
        'name': 'Владимир Владимиров',
        'email': 'vladimir@example.com',
        'phone': '+7 921 123 45 67'
    }
    
    response = client.post('/api/users',
                          data=json.dumps(new_user),
                          content_type='application/json')
    
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['name'] == 'Владимир Владимиров'
    print("✅ POST /api/users ок")


def test_get_all_bookings():
    """Test GET /api/bookings"""
    client = flask_app.test_client()
    response = client.get('/api/bookings')
    
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)
    print("✅ GET /api/bookings ок")


def test_create_booking():
    """Test POST /api/bookings"""
    client = flask_app.test_client()
    new_booking = {
        'user_id': 1,
        'tour_id': 1,
        'booking_date': '2026-03-01T10:00:00',
        'status': 'confirmed'
    }
    
    response = client.post('/api/bookings',
                          data=json.dumps(new_booking),
                          content_type='application/json')
    
    assert response.status_code == 201
    print("✅ POST /api/bookings ок")


def test_health_check():
    """Test /health endpoint"""
    client = flask_app.test_client()
    response = client.get('/health')
    
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['status'] == 'healthy'
    print("✅ GET /health ок")


if __name__ == '__main__':
    print("\n🤋 Запускаем тесты...\n")
    
    test_health_check()
    test_get_all_tours()
    test_get_single_tour()
    test_create_tour()
    test_update_tour()
    test_get_all_users()
    test_create_user()
    test_get_all_bookings()
    test_create_booking()
    
    print("\n✅ Все тесты пройдены!\n")
