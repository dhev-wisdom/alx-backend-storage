-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers
-- Procedure computes and store the average weighted score for all students
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	DECLARE users_id INT;
	DECLARE weighted_avg FLOAT;

	DECLARE cur CURSOR FROM SELECT id from users;
	DECLARE CONTINUE HANDLER FOR NOT FOUND SET users_id = NULL;

	OPEN cur;

	read_loop: LOOP
		FETCH cur INTO users_id;

		IF users_id IS NULL THEN
			LEAVE read_loop;
		END IF;

		SET weighted_avg = (SELECT SUM(C.score * P.weight)
			FROM corrections AS C
			JOIN projects AS P ON C.project_id = P.id
			WHERE C.user_id = users_id
		);

		UPDATE users
		SET average_score = weighted_avg WHERE id = users_id;

	END LOOP;

	CLOSE cur;

END;
$$
DELIMITER ;
