CREATE DATABASE ria_edr;

USE ria_edr;

create table clientes(
id_cliente       int(4)      not null primary key auto_increment,
nombre_cliente   varchar(30) not null,
apellido_paterno varchar(20) not null,
apellido_materno varchar(20) not null,
telefono         varchar(10) not null);

create table productos(
id_producto  int(4)      not null primary key,
nombre       varchar(30) not null,
marca        varchar(20) not null,
modelo       varchar(20) not null,
cantidad     int(5)      not null);

insert into clientes(nombre_cliente, apellido_paterno, apellido_materno, telefono) values
('Juan', 'Peres', 'Aguirre', '7752098175'),
('Axel', 'Hernandez', 'Dominguez', '7710345671'),
('Sandra', 'Martinez', 'lopez', '7756431097);

insert into productos(id_producto, nombre, marca, modelo, cantidad) values
('5632', 'Cerveza', 'Corona', 'lata', 30),
('5678', '', 'Refreco', 'Pepsico','3lts' 10),
('5878', 'Galletas', 'Gamesa', 'chico', 12);

CREATE USER 'ria'@'localhost' IDENTIFIED BY 'ria.2019';
GRANT ALL PRIVILEGES ON ria_iniciales.* TO 'ria'@'localhost';
FLUSH PRIVILEGES;
