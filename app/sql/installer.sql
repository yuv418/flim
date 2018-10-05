use bug_reporter_db
create table users (id INT PRIMARY KEY AUTO_INCREMENT, first_name VARCHAR(128), last_name VARCHAR(128), email TEXT, password_hashed VARCHAR(256), username VARCHAR(32));
