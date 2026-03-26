CREATE DATABASE IF NOT EXISTS Logonmusic;

USE Logonmusic;

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

INSERT INTO `logonmusic`.`genero`
(`nome`,
`icone`,
`cor`)
VALUES
("Rock","","dark blue"),
("Pagode","","yellow"),
("MPB","","red"),
("Samba","","orange"),
("Rock Nacional", "", "green"),
("Infantil", "", "pink");

INSERT INTO `logonmusic`.`musica`
(`cantor`,
`duracao`,
`nome`,
`url_imagem`,
`nome_genero`)
VALUES
("Soweto",
"00:04:24",
"Tudo Fica Blue",
"https://m.media-amazon.com/images/I/51lcOOXdeWL._UF1000,1000_QL80_.jpg",
"Pagode"),

("Djavan",
"00:03:46",
"Avião",
"https://djavan.com.br/content/uploads/2018/11/oceano.jpg",
"MPB"),

("Fundo de Quintal",
"00:04:15",
"Fada",
"https://i.scdn.co/image/ab67616d0000b2730d02093a44e1fbb3a6e5cb26",
"Samba"),

("Dire Straits",
"00:06:10",
"Sultans of Swing",
"https://i.scdn.co/image/ab67616d0000b2737ceb12d9f0e789a92d24d76e",
"Rock"),

("Martinho da Vila",
"00:03:16",
"Mulheres",
"https://cdn-images.dzcdn.net/images/cover/67de21c6d02eaa7e949366cf0316ad20/1900x1900-000000-80-0-0.jpg",
"Samba"),

("Titãs",
"00:02:55",
"O Pulso",
"https://i.scdn.co/image/ab67616d00001e02045690076ce93482d65973a5",
"Rock Nacional"),

("Trem da Alegria",
"00:03:58",
"Uni, duni, tê",
"https://upload.wikimedia.org/wikipedia/pt/4/47/Trem_da_Alegria_%281986%29.jpg",
"Infantil"),

("Elis Regina",
"00:03:01",
"Fascinação",
"https://i.scdn.co/image/ab67616d0000b2731615ee10eb3871db80e84848",
"Infantil")
;












select * from musica;












