show databases;
use mysql;
create table data(
    id int primary key auto_increment,
	name varchar(30),
    age int,
    address varchar(30),
    contact varchar(10),
     mail  varchar(50));
alter table data modify contact varchar(10);
drop table data;
select * from data;

create table data(
    id int primary key auto_increment,
	name varchar(30),
    age int,
    address varchar(30),
    contact varchar(10),
     mail  varchar(50));