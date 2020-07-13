-- Write a script that creates a table second_table in the database hbtn_0c_0
-- in your MySQL server and add multiples rows.
CREATE TABLE IF NOT EXISTS second_table (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, 
name VARCHAR(256), score INT)
INSERT INTO second_table (`id`, `name`,`score`) VALUES (NULL "John", '10'), (NULL, "Alex", '3'), (NULL, "Bob", '14'), (NULL, "George", '8');