-- SQL script that creates a trigger that resets the attribute valid_email
--  only when the email has been changed
CREATE TRIGGER reset_valid_email
AFTER UPDATE ON users
FOR EACH ROW
BEGIN
	IF NEW.email != users.email THEN
		SET NEW.valid_email = 1
	WHERE NEW.name == users.name;
END;
