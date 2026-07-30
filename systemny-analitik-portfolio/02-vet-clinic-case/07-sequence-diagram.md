# Кейс: Ветклиника — Sequence

```mermaid
sequenceDiagram
    participant Client as Клиент
    participant App as Приложение
    participant DB as База данных
    participant SMS as SMS-сервис

    Client->>App: 1. Записаться
    App->>DB: 2. Проверить слот
    DB-->>App: 3. Свободно
    App->>DB: 4. Создать запись
    App->>SMS: 5. Отправить уведомление
    App-->>Client: 6. Подтверждение
