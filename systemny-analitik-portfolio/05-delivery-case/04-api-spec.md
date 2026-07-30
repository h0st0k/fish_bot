# Спецификация API: Создание заказа на доставку

**Method:** `POST`  
**URL:** `/api/v1/deliveries`  
**Description:** Создание новой заявки на доставку из информационной системы партнера (интернет-магазина).

### Request Headers

| Key | Value | Description |
| :--- | :--- | :--- |
| `Authorization` | `Bearer <token>` | Токен аутентификации партнера |
| `Content-Type` | `application/json` | Формат тела запроса |

### Request Body (JSON)
```json
{
  "partner_order_id": "ORD-2026-99482",
  "delivery_type": "express",
  "sender": {
    "company_name": "ООО Мега Стор",
    "phone": "+79991112233",
    "address": "г. Санкт-Петербург, Невский пр-кт, д. 1"
  },
  "recipient": {
    "full_name": "Иванов Иван Иванович",
    "phone": "+79995556677",
    "address": "г. Санкт-Петербург, ул. Пушкина, д. 10, кв. 25"
  },
  "cargo": {
    "weight_kg": 2.5,
    "dimensions": {
      "width_cm": 30,
      "height_cm": 20,
      "depth_cm": 15
    },
    "declared_value_rub": 5000.00
  }
}
```

### Response (201 Created)
```json
{
  "delivery_id": "DEL-88301-XYZ",
  "status": "created",
  "estimated_delivery_time": "2026-07-01T15:30:00Z",
  "delivery_cost_rub": 450.00,
  "tracking_url": "https://delivery-service.ru"
}
```

### Error Responses
* **400 Bad Request**: Неверный формат адреса или превышены лимиты по весу/габаритам.
* **401 Unauthorized**: Отсутствует или невалиден токен партнера.
