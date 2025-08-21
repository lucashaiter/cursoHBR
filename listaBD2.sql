/* DROP SCHEMA Aula2;
CREATE SCHEMA Aula2;
USE Aula2;

CREATE TABLE `autor` (
  `idAutor` int NOT NULL,
  `nomeAutor` varchar(50) NOT NULL,
  `emailAutor` varchar(50) NOT NULL,
  PRIMARY KEY (`idAutor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `post` (
  `idPost` int NOT NULL,
  `conteudo` varchar(45) NOT NULL,
  `dataPost` date NOT NULL,
  `titulo` varchar(45) NOT NULL,
  `idAutor` int NOT NULL,
  PRIMARY KEY (`idPost`),
  KEY `fkIdAutor_idx` (`idAutor`),
  CONSTRAINT `fkIdAutor` FOREIGN KEY (`idAutor`) REFERENCES `autor` (`idAutor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `comentario` (
  `idComentario` int NOT NULL,
  `texto` varchar(45) NOT NULL,
  `dataComentario` date NOT NULL,
  `autorComentario` varchar(45) NOT NULL,
  `idPost` int NOT NULL,
  PRIMARY KEY (`idComentario`),
  KEY `fkIdPost_idx` (`idPost`),
  CONSTRAINT `fkIdPost` FOREIGN KEY (`idPost`) REFERENCES `post` (`idPost`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO Autor(idAutor, nomeAutor, emailAutor) VALUES
(1, "Pedro", "pedro@email.com"),
(2, "Joao", "joao@gmail.com"),
(3, "Lucas", "lucas@gmail.com"),
(4, "Danilo", "danilo@gmail.com");

INSERT INTO Post(idPost, conteudo, dataPost, titulo, idAutor) VALUES
(1, "Faça dois mil paes por hora", "2025-08-10", "Pao", 2),
(2, "Correr eh bom", "2025-09-30", "Corrida", 1),
(3, "Nutrição é bom", "2025-02-18", "Nutricional", 1),
(4, "Natal eh bom dimaize", "2025-12-25", "Natal", 4);

INSERT INTO Comentario(idComentario, texto, dataComentario, autorComentario, idPost) VALUES
(1, "Eh mentira!!", "2025-08-11", "Talita", 1),
(2, "Jogar eh melhor", "2025-09-30", "Vitor", 2),
(3, "Muito!", "2025-10-01", "Emerson", 2),
(4, "Doce :)", "2025-02-20", "Mileni", 3);

SELECT * FROM Autor;
SELECT * FROM Post;
SELECT * FROM Comentario;

UPDATE Autor SET nomeAutor = "Joana", emailAutor = "joana@gmail.com" WHERE idAutor = 1;
UPDATE Post SET conteudo = "Lapada seca do carai", titulo = "Tapa" WHERE  idPost = 2;
UPDATE Comentario SET autorComentario = "Fabricio", texto = "Junin muito bom!" WHERE autorComentario = "Mileni";

DELETE FROM Comentario WHERE idComentario = 4;
DELETE FROM Comentario WHERE autorComentario = "Talita";
DELETE FROM Post WHERE idPost = 3;
DELETE FROM Post WHERE titulo = "Natal";
DELETE FROM Autor WHERE idAutor = 3; 
DELETE FROM Autor WHERE nomeAutor = "Danilo"; */



