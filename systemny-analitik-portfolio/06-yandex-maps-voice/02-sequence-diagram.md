# Sequence Diagram: Голосовое ведение маршрута

```mermaid
sequenceDiagram
    participant User as Пользователь
    participant App as Яндекс.Карты
    participant Nav as Сервер навигации
    participant Voice as Алиса (голос)
    participant GPS as GPS-модуль

    User->>App: 1. Выбирает маршрут (вело/самокат)
    App->>Nav: 2. Запрос маршрута с учётом велодорожек
    Nav-->>App: 3. Маршрут построен
    App-->>User: 4. Отображает маршрут

    User->>App: 5. Начинает движение
    App->>GPS: 6. Запрос текущего местоположения
    GPS-->>App: 7. Координаты

    loop Каждый манёвр
        App->>Nav: 8. Проверка следующего манёвра
        Nav-->>App: 9. Инструкция (поворот, расстояние)
        App->>Voice: 10. Отправить голосовое сообщение
        Voice-->>User: 11. "Через 200 метров поверните направо"
    end

    opt Фоновый режим
        User->>App: 12. Сворачивает приложение
        App->>Voice: 13. Подсказки продолжаются в фоне
    end

```

```
