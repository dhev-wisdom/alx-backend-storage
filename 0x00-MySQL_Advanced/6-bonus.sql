-- SQL script that creates a stored procedure AddBonus
-- AddBonus adds a new correction for a student
DELIMITER $$
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
	DECLARE new_project_id INT;
	IF ((SELECT COUNT(*) FROM projects WHERE name = project_name) < 1) THEN
		INSERT INTO projects (name) VALUES(project_name);
		SET new_project_id = LAST_INSERT_ID();
	ELSE
		SET new_project_id = (SELECT id FROM projects WHERE name = project_name LIMIT 1;)
	END IF
	INSERT INTO corrections (user_id, project_id, score)
	VALUES (user_id, new_project_id, score)
END
$$
DELIMITER;
