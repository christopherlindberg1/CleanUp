use cudb;


-- Denna fil är en representation över de tabeller som finns i vår databas.


-- Innehåller information om användare
CREATE TABLE user_password (
 	username VARCHAR(100),
	email VARCHAR(100) PRIMARY KEY,
 	password VARCHAR(100)
);


-- Innehåller information om vilka rum varje användare har
CREATE TABLE room (
	room_name VARCHAR(50) PRIMARY KEY,
	email VARCHAR(100) FOREIGN KEY
);


-- Innehåller information om vilka möbler som finns i olika användares rum
CREATE TABLE object (
	object_name VARCHAR(50),
	room_name VARCHAR(50) FOREIGN KEY,
	email VARCHAR(100) FOREIGN KEY
);


-- Lagrar artiklar
CREATE TABLE article (
	id INT(11) AUTO INCREMENT PRIMARY KEY,
	title VARCHAR(100),
	author VARCHAR(100),
	body TEXT,
	create_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);