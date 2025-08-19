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

