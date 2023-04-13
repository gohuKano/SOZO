CREATE TABLE accounts (
	user_id serial PRIMARY KEY,
    prenom VARCHAR ( 50 ) NOT NULL,
	nom VARCHAR ( 50 ) NOT NULL,
	email VARCHAR ( 255 ) UNIQUE NOT NULL,
    password VARCHAR ( 50 ) NOT NULL
);

CREATE TABLE products (
	product_id SERIAL PRIMARY KEY,
	name VARCHAR(255) NOT NULL,
	description TEXT,
	price_HT DECIMAL(10,2) NOT NULL,
	category VARCHAR(255),
	gender VARCHAR(255),
	size VARCHAR(255),
	color VARCHAR(255)
);

CREATE TABLE cart (
    cart_id SERIAL PRIMARY KEY,
    client_id INTEGER REFERENCES client(id),
    product_id INTEGER REFERENCES product(id)
);

CREATE TABLE newsletter_subscribers (
	newsletter_id serial PRIMARY KEY,
	prenom VARCHAR(255) NOT NULL,
	email VARCHAR(255) NOT NULL
);

