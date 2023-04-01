CREATE TABLE accounts (
	user_id serial PRIMARY KEY,

    prenom VARCHAR ( 50 ) UNIQUE NOT NULL,
	nom VARCHAR ( 50 ) UNIQUE NOT NULL,
    
	email VARCHAR ( 255 ) UNIQUE NOT NULL,
    password VARCHAR ( 50 ) NOT NULL
);