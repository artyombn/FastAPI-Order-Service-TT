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
