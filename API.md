# REST API Документация

## Base URL

```
http://localhost:5000/api
```

## Ответы

```json
{
  "status": 200,
  "data": {}
}
```

## ТУРЫ

### GET /tours

Получить все туры.

**Ответ:**

```json
[
  {
    "id": 1,
    "destination": "Мальдивы",
    "description": "Пляжи и кораллы",
    "price": 2500,
    "duration_days": 7,
    "available_slots": 10,
    "created_at": "2026-01-21T00:00:00"
  }
]
```

### GET /tours/:id

Получить один тур.

**Параметры:**
- `id` (integer) - Номер тура

**Ответ:**

```json
{
  "id": 1,
  "destination": "Мальдивы",
  "description": "Пляжи и кораллы",
  "price": 2500,
  "duration_days": 7,
  "available_slots": 10,
  "created_at": "2026-01-21T00:00:00"
}
```

### POST /tours

Составление нового тура.

**Тело реквеста:**

```json
{
  "destination": "Таиланд",
  "description": "Экзотика и релакс",
  "price": 1500,
  "duration_days": 5,
  "available_slots": 15
}
```

### PUT /tours/:id

Обновление тура.

**Параметры:**
- `id` (integer) - Номер тура

**Тело:**

```json
{
  "price": 1800,
  "available_slots": 12
}
```

### DELETE /tours/:id

Удаление тура.

---

## ПОЛЬЗОВАТЕЛИ

### GET /users

Получить всех пользователей.

### POST /users

Осоставление нового пользователя.

**Тело:**

```json
{
  "name": "Николай Николаев",
  "email": "nikolay@example.com",
  "phone": "+7 555 123 45 67"
}
```

### PUT /users/:id

Обновление пользователя.

### DELETE /users/:id

Удаление пользователя.

---

## БРОНИРОВАНИЯ

### GET /bookings

Получить все бронирования.

### POST /bookings

Составление бронирования.

**Тело:**

```json
{
  "user_id": 1,
  "tour_id": 1,
  "booking_date": "2026-02-20T15:00:00",
  "status": "confirmed"
}
```

### PUT /bookings/:id

Обновление бронирования.

### DELETE /bookings/:id

Отмена бронирования.
