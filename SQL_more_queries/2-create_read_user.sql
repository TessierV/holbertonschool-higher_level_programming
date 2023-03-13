-- MYSQL script that creates the MySQL server user user_0d_2: should have SELECT
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost'
IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON *.*
TO 'user_0d_2'@'localhost';