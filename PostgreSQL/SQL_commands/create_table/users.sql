CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    fullname VARCHAR(100),
    email VARCHAR(100) UNIQUE
);

-- id|fullname        |email                    |
-- --+----------------+-------------------------+
--  1|Susan Alexander |bryantteresa@example.org |
--  2|Laurie Perez    |bobby21@example.org      |
--  3|Steven Jacobs   |robertcruz@example.net   |
--  4|Brad Burton     |davidtaylor@example.com  |
--  5|Gabriel Kent    |tracymorgan@example.com  |
--  6|Jimmy Cross     |thompsonbrian@example.net|
--  7|Blake Miller DDS|lewiseric@example.net    |
--  8|Jeffrey Fisher  |mathew72@example.net     |
--  9|John Downs      |matthew53@example.org    |
-- 10|Joanne Williams |juliehoward@example.net  |