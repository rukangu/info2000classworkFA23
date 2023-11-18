CREATE TABLE IF NOT EXISTS student( 
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
id INT PRIMARY KEY
);
CREATE INDEX name_index ON student(last_name); --this is a sql comment. Indexing speeds up look-ups