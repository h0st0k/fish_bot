# SQL-запросы для библиотеки

## 1. Найти все книги в наличии

```sql
SELECT id, title, author, year 
FROM Books 
WHERE status = 'в_наличии'
ORDER BY title;
SELECT 
    b.id AS booking_id,
    bk.title AS book_title,
    b.reserve_date,
    b.due_date,
    b.status
FROM Reservations b
JOIN Books bk ON b.book_id = bk.id
WHERE b.reader_id = 101 
  AND b.status = 'active'
ORDER BY b.due_date;
SELECT 
    r.full_name AS reader_name,
    bk.title AS book_title,
    res.due_date
FROM Reservations res
JOIN Readers r ON res.reader_id = r.id
JOIN Books bk ON res.book_id = bk.id
WHERE res.due_date = CURRENT_DATE + INTERVAL 1 DAY
  AND res.status = 'active';
SELECT 
    r.full_name,
    COUNT(res.id) AS total_bookings
FROM Readers r
JOIN Reservations res ON r.id = res.reader_id
GROUP BY r.id, r.full_name
ORDER BY total_bookings DESC
LIMIT 3;
SELECT email, COUNT(*) AS duplicate_count
FROM Readers
GROUP BY email
HAVING COUNT(*) > 1;
Автор: h0st0k
Дата: 24.06.2026
