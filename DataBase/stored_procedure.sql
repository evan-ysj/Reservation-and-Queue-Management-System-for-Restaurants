# A stored procedure 
# function: change "occupied" attribute of table "Table" to "True" if the reservation date is today

USE django;
drop procedure IF EXISTS occupation_update;

DELIMITER $$
CREATE PROCEDURE  occupation_update()
BEGIN

    UPDATE reservation_table SET reservation_table.occupied = FALSE  ;
    
    UPDATE reservation_table, reservation_reservation
    SET reservation_table.occupied = TRUE
    WHERE reservation_table.table_id = reservation_reservation.table_id_id and reservation_reservation.date=CURDATE()  ;
    
    UPDATE reservation_reservation
    SET reservation_reservation.expired = TRUE
    WHERE reservation_reservation.date < CURDATE()  ;

END $$
DELIMITER ;

call occupation_update();
