-- SQL script that creates a stored procedure ComputeAverageScoreForUser
-- procedure  computes and store the average score for a student
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
	DECLARE score INT;
	DECLARE total_scores INT;
	DECLARE sum_scores INT;
	DECLARE average FLOAT;

	DECLARE cur CURSOR FOR
		SELECT score FROM corrections WHERE user_id = user_id;
	DECLARE CONTINUE HANDLER FOR NOT FOUND SET total_scores = 0;

	SET total_scores = 0;
	SET sum_scores = 0;

	OPEN cur;
	read_loop: LOOP
		FETCH cur INTO score;
		SET sum_scores = sum_scores + score;
		SET total_scores = total_scores + 1;
	END LOOP read_loop;
	CLOSE cur;

	SET average = sum_scores / total_scores;

	UPDATE users
	SET average_score = average
	WHERE id = user_id;
END
$$
DELIMITER ;
