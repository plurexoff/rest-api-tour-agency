# Быстрый старт

## 1️⃣ Установка

```bash
# Клонирование
git clone https://github.com/plurexoff/rest-api-tour-agency.git
cd rest-api-tour-agency

# Виртуальное окружение
python -m venv venv
source venv/bin/activate  # на Windows: venv\Scripts\activate

# Установка зависимостей
pip install -r requirements.txt
```

## 2️⃣ Запуск

```bash
python app.py
```

Сервер стартует на `http://localhost:5000`

## 3️⃣ Проверка

```bash
# Получить все туры
curl http://localhost:5000/api/tours

# Получить инфо об API
curl http://localhost:5000/api
```

## 💳 Примеры curl

### GET все туры

```bash
curl -X GET http://localhost:5000/api/tours
```

### POST новый тур

```bash
curl -X POST http://localhost:5000/api/tours \
  -H "Content-Type: application/json" \
  -d '{
    "destination": "Тайланд",
    "description": "Топичные пляжи и храмы",
    "price": 1500,
    "duration_days": 5,
    "available_slots": 20
  }'
```

### GET тон тур

```bash
curl -X GET http://localhost:5000/api/tours/1
```

### PUT обновление тура

```bash
curl -X PUT http://localhost:5000/api/tours/1 \
  -H "Content-Type: application/json" \
  -d '{
    "price": 1800,
    "available_slots": 15
  }'
```

### DELETE тур

```bash
curl -X DELETE http://localhost:5000/api/tours/1
```

### POST новый пользователь

```bash
curl -X POST http://localhost:5000/api/users \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Василиса Василевский",
    "email": "vasily@example.com",
    "phone": "+7 999 888 77 66"
  }'
```

### POST новое бронирование

```bash
curl -X POST http://localhost:5000/api/bookings \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": 1,
    "tour_id": 1,
    "booking_date": "2026-02-15T10:00:00",
    "status": "confirmed"
  }'
```

## Postman

1. Перейти в Postman
2. **Import** → выбрать `examples/postman_collection.json`
3. Запустить реквесты
