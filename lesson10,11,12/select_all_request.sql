-- Запрос, выводящий данные из всех таблиц:

SELECT 
    a.first_name AS "Name", 
    a.last_name AS "Last name", 
    b.title AS "Book", 
    s.title AS "Series", 
    o.book_number AS "№" 
FROM 
    authors AS a 
INNER JOIN books_authors AS ab ON a.author_id = ab.author_id 
INNER JOIN books AS b ON b.book_id = ab.book_id 
INNER JOIN order_in_series AS o ON b.book_id = o.book_id 
INNER JOIN series AS s ON s.series_id = o.series_id;
