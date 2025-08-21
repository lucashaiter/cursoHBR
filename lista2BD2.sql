DROP SCHEMA Aula1;
CREATE SCHEMA Aula1;
USE Aula1;

CREATE TABLE Logg(
	codigoLog INT PRIMARY KEY NOT NULL,
    nomeLog VARCHAR(100) NOT NULL
);

CREATE TABLE Sessao(
	codigoSessao INT PRIMARY KEY NOT NULL,
    IP VARCHAR(20) NOT NULL,
    usuario VARCHAR(100) NOT NULL,
    idLog INT,
    CONSTRAINT fkLog FOREIGN KEY (idLog) REFERENCES Logg(codigoLog)
    
);

CREATE TABLE Link(
	codigoLink INT PRIMARY KEY NOT NULL,
    url VARCHAR(500) NOT NULL,
    vizinhanca VARCHAR(100) NOT NULL,
    texto VARCHAR(100) NOT NULL
);

CREATE TABLE Pagina(
	codigoPagina INT PRIMARY KEY NOT NULL,
    codigoHTML VARCHAR(5000) NOT NULL,
    tipoConteudo VARCHAR(100) NOT NULL,
    titulo VARCHAR(50) NOT NULL,
    urlPagina VARCHAR(500) NOT NULL,
    tamanhoArquivo INT NOT NULL,
    textoPuro VARCHAR(500) NOT NULL,
    idLink INT,
    CONSTRAINT fkLink FOREIGN KEY (idLink) REFERENCES Link(codigoLink)
);

CREATE TABLE Requisicao(
	codigoRequisicao INT PRIMARY KEY NOT NULL,
    codigoHTTP VARCHAR(200) NOT NULL,
    tempoTranscorrido INT NOT NULL,
    carimboTempo VARCHAR(50) NOT NULL,
    idSessao INT,
    idPagina INT,
    CONSTRAINT fkSessao FOREIGN KEY (idSessao) REFERENCES Sessao(codigoSessao),
    CONSTRAINT fkPaginaRequisicao FOREIGN KEY (idPagina) REFERENCES Pagina(codigoPagina)
);

SELECT * FROM Logg;
SELECT * FROM Sessao;
SELECT * FROM Link;
SELECT * FROM Pagina;
SELECT * FROM Requisicao;

INSERT INTO Logg (codigoLog, nomeLog) VALUES
(1, 'Log de Sistema'),
(2, 'Log de Aplicação'),
(3, 'Log de Erro');

INSERT INTO Sessao (codigoSessao, IP, usuario, idLog) VALUES
(1, '192.168.0.1', 'usuario1', 1),
(2, '192.168.0.2', 'usuario2', 2),
(3, '192.168.0.3', 'usuario3', 3);

INSERT INTO Link (codigoLink, url, vizinhanca, texto) VALUES
(1, 'https://exemplo.com', 'exemplo.com', 'Site Exemplo'),
(2, 'https://teste.com', 'teste.com', 'Site Teste'),
(3, 'https://demo.com', 'demo.com', 'Site Demo');

INSERT INTO Pagina (codigoPagina, codigoHTML, tipoConteudo, titulo, urlPagina, tamanhoArquivo, textoPuro, idLink) VALUES
(1, '<html>Conteudo 1</html>', 'text/html', 'Titulo 1', 'https://exemplo.com/pagina1', 1024, 'Texto puro 1', 1),
(2, '<html>Conteudo 2</html>', 'text/html', 'Titulo 2', 'https://teste.com/pagina2', 2048, 'Texto puro 2', 2),
(3, '<html>Conteudo 3</html>', 'text/html', 'Titulo 3', 'https://demo.com/pagina3', 512, 'Texto puro 3', 3);

INSERT INTO Requisicao (codigoRequisicao, codigoHTTP, tempoTranscorrido, carimboTempo, idSessao, idPagina) VALUES
(1, '200 OK', 150, '2025-08-21 10:00:00', 1, 1),
(2, '404 Not Found', 300, '2025-08-21 11:00:00', 2, 2),
(3, '500 Internal Server Error', 450, '2025-08-21 12:00:00', 3, 3);

UPDATE Logg SET nomeLog = 'Log Sistema Atualizado' WHERE codigoLog = 1;
UPDATE Logg SET nomeLog = 'Log Aplicação Atualizado' WHERE codigoLog = 2;
UPDATE Sessao SET IP = '10.0.0.1', usuario = 'usuario1_updated' WHERE codigoSessao = 1;
UPDATE Sessao SET IP = '10.0.0.2', usuario = 'usuario2_updated' WHERE codigoSessao = 2;
UPDATE Link SET url = 'https://exemplo-updated.com', texto = 'Site Exemplo Atualizado' WHERE codigoLink = 1;
UPDATE Link SET url = 'https://teste-updated.com', texto = 'Site Teste Atualizado' WHERE codigoLink = 2;
UPDATE Pagina SET titulo = 'Titulo Atualizado 1', tamanhoArquivo = 2048 WHERE codigoPagina = 1;
UPDATE Pagina SET titulo = 'Titulo Atualizado 2', tamanhoArquivo = 4096 WHERE codigoPagina = 2;
UPDATE Requisicao SET codigoHTTP = '201 Created', tempoTranscorrido = 100 WHERE codigoRequisicao = 1;
UPDATE Requisicao SET codigoHTTP = '403 Forbidden', tempoTranscorrido = 250 WHERE codigoRequisicao = 2;

DELETE FROM Requisicao WHERE codigoRequisicao = 1;
DELETE FROM Requisicao WHERE codigoRequisicao = 2;
DELETE FROM Pagina WHERE codigoPagina = 1;
DELETE FROM Pagina WHERE codigoPagina = 2;
DELETE FROM Link WHERE codigoLink = 1;
DELETE FROM Link WHERE codigoLink = 2;
DELETE FROM Sessao WHERE codigoSessao = 1;
DELETE FROM Sessao WHERE codigoSessao = 2;
DELETE FROM Logg WHERE codigoLog = 1;
DELETE FROM Logg WHERE codigoLog =2;

