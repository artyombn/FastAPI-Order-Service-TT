CREATE TABLE categories(
	category_id BIGSERIAL PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	parent_id BIGINT,

	CONSTRAINT category_parent_id_fk
		FOREIGN KEY(parent_id)
		REFERENCES categories(category_id)
);

CREATE TABLE products(
	product_id BIGSERIAL PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	quantity INT NOT NULL
		CHECK(quantity>=0),
	price NUMERIC(10,2) NOT NULL
        CHECK(price>=0),
	category_id BIGINT NOT NULL,

	CONSTRAINT category_id_fk
		FOREIGN KEY(category_id)
		REFERENCES categories(category_id)
);

CREATE TABLE clients(
	client_id BIGSERIAL PRIMARY KEY,
	first_name VARCHAR(100) NOT NULL,
	last_name VARCHAR(100) NOT NULL,
	email VARCHAR(255) NOT NULL UNIQUE,
	address VARCHAR(255) NOT NULL
);

CREATE TABLE orders(
	order_id BIGSERIAL PRIMARY KEY,
	created_at TIMESTAMP NOT NULL DEFAULT now(),
	status VARCHAR(32) NOT NULL DEFAULT 'created',
	client_id BIGINT NOT NULL,

	CONSTRAINT client_id_fk
		FOREIGN KEY(client_id)
		REFERENCES clients(client_id)
);

CREATE TABLE orders_products(
	order_id BIGINT NOT NULL,
	product_id BIGINT NOT NULL,
	product_quantity INT NOT NULL
		CHECK(product_quantity>=1),
	product_price_at_order NUMERIC(10,2) NOT NULL
		CHECK(product_price_at_order>=0),

	PRIMARY KEY(order_id, product_id),

	CONSTRAINT order_id_fk
	    FOREIGN KEY(order_id)
	    REFERENCES orders(order_id),

	CONSTRAINT product_id_fk
	    FOREIGN KEY(product_id)
	    REFERENCES products(product_id)
);
