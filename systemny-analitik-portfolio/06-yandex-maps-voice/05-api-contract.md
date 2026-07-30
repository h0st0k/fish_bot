# API-контракт: Голосовое ведение

## GET /route
**Описание:** Получить маршрут для велосипеда/самоката

**Параметры:**
| Параметр | Тип | Обязательный | Описание |
|----------|-----|--------------|----------|
| start_lat | float | да | Широта начальной точки |
| start_lon | float | да | Долгота начальной точки |
| end_lat | float | да | Широта конечной точки |
| end_lon | float | да | Долгота конечной точки |
| type | string | да | transport (bike / scooter) |

**Ответ (200 OK):**
```json
{
  "route_id": "abc123",
  "distance_m": 3500,
  "duration_sec": 900,
  "steps": [
    {
      "action": "turn_right",
      "distance_m": 200,
      "instruction": "Поверните направо на ул. Ленина"
    }
  ]
}
{
  "user_id": "user_456",
  "instruction": "Через 200 метров поверните направо",
  "priority": "high"
}
{
  "status": "sent",
  "timestamp": "2026-06-23T15:30:00Z"
}

```
