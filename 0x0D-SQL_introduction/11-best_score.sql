-- Write a script that lists all records with a score >= 10 in the table second_table
-- of the database hbtn_0c_0 in your MySQL server.
SELECT score FROM second_table HAVING COUNT(score) >= 10