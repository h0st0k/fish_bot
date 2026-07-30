# 🛠️ Техническая спецификация: SQL & API Контракты «Коворкинг»

---

## 🗄️ Часть 1. Сложные SQL-скрипты для DBeaver

### Скрипт 1. Поиск «конфликтных» пересечений бронирований
*   **Бизнес-цель**: Выявить ошибки логики и баги, при которых система по ошибке забронировала одно и то же рабочее место (`workspace_id`) для двух разных сотрудников на один и тот же день.
```sql
SELECT 
    b1.workspace_id,
    b1.booking_date,
    b1.id AS booking_id_first,
    b1.employee_id AS employee_id_first,
    b2.id AS booking_id_second,
    b2.employee_id AS employee_id_second
FROM bookings b1
JOIN bookings b2 ON b1.workspace_id = b2.workspace_id 
    AND b1.booking_date = b2.booking_date 
    AND b1.id < b2.id
WHERE b1.status = 'confirmed' 
  AND b2.status = 'confirmed'
ORDER BY b1.booking_date DESC;
```

---

## 🌐 Часть 2. REST API Контракт: Мягкое удаление брони (Swagger)
*   **Метод**: `DELETE`
*   **Эндпоинт**: `/api/v1/bookings/{id}`

### JSON-ответ бэкенда при успешном изменении статуса (Response 200 OK)
```json
{
  "booking_id": 8902,
  "status": "cancelled",
  "updated_at": "2026-07-16T12:00:00Z",
  "audit_log": {
    "action": "LOGICAL_DELETE",
    "deleted_by_employee_id": 451,
    "archive_retained": true
  }
}
```
