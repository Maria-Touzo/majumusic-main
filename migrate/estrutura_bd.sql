CREATE DATABASE IF NOT EXISTS LogonMusic;

USE LogonMusic;

CREATE TABLE IF NOT EXISTS genero (
 nome VARCHAR(30) NOT NULL PRIMARY KEY,
 icone VARCHAR(100),
 cor VARCHAR(10)
);

CREATE TABLE IF NOT EXISTS musica (
 codigo INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
 cantor VARCHAR(50),
 duracao TIME,
 nome VARCHAR(50),
 url_imagem VARCHAR(255),
 nome_genero VARCHAR(30),
 ativo bool default 0,
 CONSTRAINT fk_musica FOREIGN KEY (nome_genero) REFERENCES genero (nome)
);

CREATE TABLE IF NOT EXISTS usuario (
nome_usuario VARCHAR(50),
senha VARCHAR(200)
);


INSERT INTO `logonmusic`.`usuario`
(`nome_usuario`,
`senha`
)
VALUES
("lorena",
"1234");



select * from musica;


drop database LogonMusic;









