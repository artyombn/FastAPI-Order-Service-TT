-- 2.1. Получение информации о сумме товаров заказанных под каждого клиента (Наименование клиента, сумма)
SELECT
    c.id,
    c.first_name,
    c.last_name,
    c.email,
    SUM(op.product_quantity * op.product_price_at_order) as total_amount
FROM clients c
JOIN orders o ON o.client_id = c.id
JOIN orders_products op ON op.order_id = o.id
WHERE o.status IN ('shipped', 'delivered')
GROUP BY
    c.id,
    c.first_name,
    c.last_name,
    c.email;

-- 2.2. Найти количество дочерних элементов первого уровня вложенности для категорий номенклатуры.
WITH parent_child AS (
    SELECT
        parent.id as parent_id,
        parent.name as parent_name,
        COUNT(children.id) as total_children
    FROM categories parent
    LEFT JOIN categories children ON children.parent_id = parent.id
    GROUP BY parent.id, parent.name
)
SELECT * FROM parent_child
ORDER BY parent_id;

-- 2.3.1. Написать текст запроса для отчета (view) «Топ-5 самых покупаемых товаров за последний месяц» (по количеству штук в заказах). В отчете должны быть: Наименование товара, Категория 1-го уровня, Общее количество проданных штук.
CREATE VIEW top5_products_last_month AS
WITH RECURSIVE category_tree AS (
    SELECT
        id,
        name,
        name as root_name,
        id as root_id
    FROM categories
    WHERE parent_id IS NULL

    UNION ALL

    SELECT
        c.id,
        c.name,
        ct.root_name,
        ct.root_id
    FROM categories c
    JOIN category_tree ct ON c.parent_id = ct.id
)
SELECT
    n.name as product_name,
    ct.name as top_category,
    SUM(op.product_quantity) as total_quantity_sold
FROM orders_products op
JOIN orders o ON o.id = op.order_id
JOIN products n ON n.id = op.product_id
JOIN category_tree ct ON ct.id = n.category_id
WHERE EXTRACT(MONTH FROM o.created_at) = EXTRACT(MONTH FROM now()) -1
    AND o.status IN ('shipped', 'delivered')
GROUP BY n.name, ct.name
ORDER BY total_quantity_sold DESC
LIMIT 5;

SELECT * FROM top5_products_last_month;