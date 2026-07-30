# Модель данных и обработка бизнес-конфликтов (Coworking Space)

Для автоматизации бронирования рабочих мест и переговорных комнат спроектирована реляционная структура данных и заложена логика изоляции транзакций.

## 1. ER-диаграмма сущностей (Entity-Relationship Model)

Ниже представлена логическая модель базы данных, описывающая связи между пользователями, ресурсами коворкинга, бронированиями и транзакциями.

```mermaid
erDiagram
    USER ||--o{ BOOKING : "создает"
    ROOM ||--o{ BOOKING : "бронируется в"
    BOOKING ||--|| PAYMENT : "оплачивается через"

    USER {
        int user_id PK
        string full_name
        string email UK
        string phone
        timestamp created_at
    }

    ROOM {
        int room_id PK
        string name "Название/Номер места"
        string type "hot-desk / meeting-room"
        int capacity "Вместимость"
        decimal price_per_hour
        boolean is_active
    }

    BOOKING {
        int booking_id PK
        int user_id FK
        int room_id FK
        timestamp start_time
        timestamp end_time
        string status "pending / confirmed / cancelled"
        timestamp created_at
    }

    PAYMENT {
        int payment_id PK
        int booking_id FK UK
        decimal amount
        string status "paid / refunded / failed"
        string payment_gateway_id
        timestamp processed_at
    }
```

---

## 2. Спецификация API: Обработка конфликта бронирования (409 Conflict)

При одновременной попытке забронировать один и тот же временной слот (слот пересекается по `room_id`, `start_time` и `end_time`), бэкенд блокирует транзакцию на уровне БД (`SELECT ... FOR UPDATE`) и возвращает ошибку `409 Conflict`.

### Request (POST /api/v1/bookings)
```json
{
  "room_id": 42,
  "start_time": "2026-07-05T12:00:00Z",
  "end_time": "2026-07-05T14:00:00Z"
}
```

### Response (409 Conflict)
```json
{
  "error_code": "RESOURCE_ALREADY_BOOKED",
  "message": "Выбранное время для данной переговорной комнаты уже занято другим пользователем.",
  "timestamp": "2026-07-01T10:15:30Z",
  "details": {
    "conflicting_booking_id": 99482,
    "suggested_available_slots": [
      {
        "start_time": "2026-07-05T14:00:00Z",
        "end_time": "2026-07-05T16:00:00Z"
      },
      {
        "start_time": "2026-07-05T10:00:00Z",
        "end_time": "2026-07-05T12:00:00Z"
      }
    ]
  }
}
```

Кейс: Коворкинг — Модель данных
ER-диаграмма (Mermaid)
erDiagram
    Сотрудник {
        int id PK "уникальный идентификатор"
        string полное_имя "ФИО"
        string email "почта"
        string отдел "департамент"
    }

    Место {
        int id PK "уникальный идентификатор"
        int зал_id FK "ссылка на зал"
        string номер "номер места (A12)"
        string статус "active/blocked"
        string описание "розетка, монитор"
    }

    Бронь {
        int id PK "уникальный идентификатор"
        int сотрудник_id FK "ссылка на сотрудника"
        int место_id FK "ссылка на место"
        date дата_брони "дата бронирования"
        date создано "время создания записи"
        string статус "active/cancelled/used/no_show"
    }

    Зал {
        int id PK "уникальный идентификатор"
        string название "название зала"
        string этаж "этаж"
    }

    Сотрудник ||--o{ Бронь : "делает"
    Место ||--o{ Бронь : "бронируется"
    Зал ||--o{ Место : "содержит"
