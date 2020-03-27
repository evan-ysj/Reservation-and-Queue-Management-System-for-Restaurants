# A stored procedure 
# function: change "occupied" attribute of table "Table" to "True" if the reservation date is today


drop procedure IF EXISTS occupation_update;

DELIMITER $$
CREATE PROCEDURE  occupation_update()
BEGIN
    UPDATE Table, Reservation
    SET Table.occupied = TRUE
    WHERE Table.table_id = Reservation.table_id and Reservation.rsv_time=CURDATE()  ;

END $$
DELIMITER ;
