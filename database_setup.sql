CREATE DATABASE IF NOT EXISTS sql_test_db;
USE sql_test_db;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL
);

-- Insert dummy data (using plain text passwords for this demo only)
INSERT INTO users (username, password, email) VALUES
('admin', 'admin123', 'admin@example.com'),
('alice', 'alicePass', 'alice@test.com'),
('bob', 'bobPass', 'bob@test.com'),
('charlie', '123456', 'charlie@test.com'),
('dave', 'qwerty', 'dave@test.com');