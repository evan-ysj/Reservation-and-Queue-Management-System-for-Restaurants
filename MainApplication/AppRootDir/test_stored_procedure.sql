create database if not exists ece651_project;
use ece651_project;
drop table if exists Table1,Reservation;

create table Table1(
  table_id int ,
  occupied boolean,
  cap int default 10,
  primary key (table_id)

);

insert into Table1(table_id, occupied) values (11,false);
insert into Table1(table_id, occupied) values (12,false);
insert into Table1(table_id, occupied) values (13,false);
insert into Table1(table_id, occupied) values (14,false);


select * from table1;


create table Reservation(
    table_id int,
    rsv_time date,
    no_of_guests int


);
insert into Reservation(table_id, rsv_time,no_of_guests) values (11,"2020-03-27",5);
insert into Reservation(table_id, rsv_time,no_of_guests) values (12,curdate(),4);
insert into Reservation(table_id, rsv_time,no_of_guests) values (13,"2000-01-01",6);
insert into Reservation(table_id, rsv_time,no_of_guests) values (14,"2020-03-27",6);
select * from Reservation;



# A stored procedure
# function: change "occupied" attribute of table "Table" to "True" if the reservation date is today
drop procedure IF EXISTS occupation_update;

DELIMITER $$
CREATE PROCEDURE  occupation_update()
BEGIN
    UPDATE Table1, Reservation
    SET Table1.occupied = TRUE
    WHERE Table1.table_id = Reservation.table_id and Reservation.rsv_time=CURDATE()  ;

END $$
DELIMITER ;

call occupation_update();