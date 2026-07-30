# Кейс: Ветклиника — API-контракт

## GET /doctors
Получить список врачей

**Ответ (200 OK):**
```json
{
  "doctors": [
    {
      "id": 1,
      "name": "Иванова Анна",
      "specialty": "терапевт"
    }
  ]
}
```

## POST /appointments
Создать запись к врачу

**Тело запроса:**
```json
{
  "doctor_id": 1,
  "client_name": "Иван Петров",
  "phone": "+79991234567",
  "pet_name": "Барсик",
  "appointment_time": "2026-06-18T10:30:00Z"
}
```

**Успешный ответ (201 Created):**
```json
{
  "appointment_id": 1001,
  "status": "created",
  "message": "Вы записаны на 18 июня в 10:30"
}
```

## DELETE /appointments/{id}
Отменить запись

**Успешный ответ (200 OK):**
```json
{
  "status": "cancelled",
  "message": "Запись отменена"
}
```
