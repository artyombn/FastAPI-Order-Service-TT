# FastAPI-Order-Service-TT
FastAPI Order Service (Technical Task)

Таблица "products":  
id   
name  
quantity  
price  
category_id (foreign key -> categories.id)  


Таблица "categories":  
id  
name  
parent_id (foreign -> categories.id)  


Таблица "clients" ->  
id  
first_name  
last_name  
email  
address  


Таблица "orders"  
id  
created_at  
status  
client_id (foreign key -> clients.id)  

**Many To Many relationship (order -> products and product -> orders)**  
Таблица "orders_products”

order_id (foreign key -> orders.id)  
product_id (foreign key -> products.id)  
product_quantity  
product_price_at_order  