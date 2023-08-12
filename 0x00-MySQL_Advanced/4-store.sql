-- SQL script that creates a trigger
-- Trigger decreases the quantity of an item after adding a new order.
CREATE 
TRIGGER decrease
AFTER INSERT
ON user FOR EACH ROW
BEGIN
	SET new.quantity = quantity - 1
	WHERE new.quantity >= 0;
END
