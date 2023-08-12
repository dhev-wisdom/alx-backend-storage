-- SQL script that creates a trigger
-- Trigger decreases the quantity of an item after adding a new order.
CREATE TRIGGER decrease_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
	UPDATE items
	SET quantity = quantity - 1
	WHERE name = NEW.item_name AND quantity > 0;
END;
