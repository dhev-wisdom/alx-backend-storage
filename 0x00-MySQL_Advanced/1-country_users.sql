-- Create table 'users' with attributes id, email and name
-- Script should be executable on any database
CREATE TABLE users IF NOT EXISTS (
	id INT AUTO_INCREMENT,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255),
	country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US',
	PRIMARY KEY(id),
);
