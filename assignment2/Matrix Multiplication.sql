CREATE TABLE TestA (
row_num INT,
col_num INT,
value INT,
PRIMARY KEY(row_num, col_num)
)

CREATE TABLE TestB (
row_num INT,
col_num INT,
value INT,
PRIMARY KEY(row_num, col_num)
)

INSERT INTO TestA VALUES
(0, 0, 1),
(0, 1, 9),
(1, 0, 3),
(1, 1, 2)

INSERT INTO TestB VALUES
(0, 0, 2),
(0, 1, 1),
(1, 0, 4),
(1, 1, 3)

SELECT a.row_num, b.col_num, SUM(a.value*b.value)
FROM TestA as a, TestB as b
WHERE a.col_num = b.row_num 
GROUP BY a.row_num, b.col_num;