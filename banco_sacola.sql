CREATE DATABASE Sacola;
GO

USE Sacola;
GO

CREATE TABLE usuario (
ID int  PRIMARY KEY,
login varchar(30) NOT NULL,
senha varchar(30) NOT NULL
);
GO

CREATE TABLE sacola (
id int NOT NULL,
id_usuario int NOT NULL,
CONSTRAINT pk_id PRIMARY KEY (id),
CONSTRAINT fk_id_usurario FOREIGN KEY(id_usuario) REFERENCES usuario(ID)
);
GO

CREATE TABLE item (
id int NOT NULL,
nome varchar(30) NOT NULL,
descricao varchar(200) NOT NULL,
valor int NOT NULL,
estoque int NOT NULL,
CONSTRAINT pk_id_item PRIMARY KEY (id)
);
GO

 CREATE TABLE sacola_itens (
id_sacola int NOT NULL,
id_item int NOT NULL,
qtd int NOT NULL,
CONSTRAINT fk_id_sacola FOREIGN KEY (id_sacola) REFERENCES sacola(id),
CONSTRAINT fk_id_item FOREIGN KEY (id_item) REFERENCES item(id)
);
GO

