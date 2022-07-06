-- Script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa)
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS `cities` (id INT PRIMARY KEY AUTO_INCREMENT, state_id INT, name VARCHAR(256) NOT NULL, FOREIGN KEY (state_id) REFERENCES states(id))
