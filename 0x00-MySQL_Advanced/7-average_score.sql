-- SQL script that creates a stored procedure ComputeAverageScoreForUser
-- procedure  computes and store the average score for a student
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
	UPDATE users
	SET average_score = (SELECT AVG(score) FROM corrections AS C WHERE C.user_id = user_id);
	WHERE users.id = user_id;
END
$$
DELIMITER ;
