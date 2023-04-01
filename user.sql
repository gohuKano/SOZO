CREATE TABLE accounts (
	user_id serial PRIMARY KEY,

    prenom VARCHAR ( 50 ) NOT NULL,
	nom VARCHAR ( 50 ) NOT NULL,
    
	email VARCHAR ( 255 ) UNIQUE NOT NULL,
    password VARCHAR ( 50 ) NOT NULL
);

CREATE TABLE products (
	id SERIAL PRIMARY KEY,
	name VARCHAR(255) NOT NULL,
	description TEXT,
	price DECIMAL(10,2) NOT NULL,
	image_url VARCHAR(255),
	category VARCHAR(255),
	gender VARCHAR(255),
	size VARCHAR(255),
	color VARCHAR(255),
	material VARCHAR(255),
	created_at TIMESTAMP NOT NULL DEFAULT NOW(),
	updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);
