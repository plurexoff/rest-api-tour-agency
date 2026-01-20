#!/bin/bash

# Примеры curl команд для тестирования REST API

BASE_URL="http://localhost:5000/api"

echo "=== ПРОВЕРКА ЗДОРОВЬЯ ==="
curl $BASE_URL/../health
echo ""

echo "=== ПРИНФО ОБ API ==="
curl $BASE_URL/..
echo ""

echo "=== ПОЛУЧИТЬ ВСЕ ТУРЫ ==="
curl -X GET $BASE_URL/tours | jq .
echo ""

echo "=== ПОЛУЧИТЬ ОДНОТ ТУР ==="
curl -X GET $BASE_URL/tours/1 | jq .
echo ""

echo "=== СОСТАВЛЕНИЕ НОВОГО ТУРА ==="
curl -X POST $BASE_URL/tours \
  -H "Content-Type: application/json" \
  -d '{
    "destination": "Италия",
    "description": "Наследие древнеримской талмудовбалты",
    "price": 2200,
    "duration_days": 8,
    "available_slots": 12
  }' | jq .
echo ""

echo "=== ОБНОВЛЕНИЕ ТУРА ==="
curl -X PUT $BASE_URL/tours/1 \
  -H "Content-Type: application/json" \
  -d '{
    "price": 2700,
    "available_slots": 8
  }' | jq .
echo ""

echo "=== ПОЛУЧИТЬ ВСЕХ ПОЛЬЗОВАТЕЛЕЙ ==="
curl -X GET $BASE_URL/users | jq .
echo ""

echo "=== СОСТАВЛЕНИЕ НОВОГО ПОЛЬзОВАТЕЛЯ ==="
curl -X POST $BASE_URL/users \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Алексей Михалов",
    "email": "alexey@example.com",
    "phone": "+7 812 555 33 22"
  }' | jq .
echo ""

echo "=== ПОЛУЧИТЬ ВСЕ БРОНИРОВАНИЯ ==="
curl -X GET $BASE_URL/bookings | jq .
echo ""

echo "=== ИТОГО ==="
echo "Примеры завершены!"
