DROP SCHEMA Lista3BD;
CREATE SCHEMA Lista3BD;
USE Lista3BD;

CREATE TABLE autores (
    id int PRIMARY KEY auto_increment,  
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE posts (
    id int PRIMARY KEY AUTO_INCREMENT, 
    titulo VARCHAR(200) NOT NULL,
    conteudo TEXT,
    publicado BOOLEAN DEFAULT FALSE,
    data_publicacao DATE,
    autor_id INT,
    FOREIGN KEY (autor_id) REFERENCES autores(id)
);

INSERT INTO autores (id, nome, email) VALUES
(1, 'Ana Silva', 'ana.silva@email.com'),
(2, 'Bruno Costa', 'bruno.c@email.com'),
(3, 'Carlos Dias', 'carlos.dias@exemplo.com'),
(4, 'Diana Moreira', 'diana.m@email.com'),
(5, 'Eduardo Faria', 'edu.faria@exemplo.com'),
(6, 'Fernanda Lima', 'f.lima@outroemail.com'),
(7, 'Gabriel Souza', 'g.souza@email.com');

INSERT INTO posts (titulo, conteudo, publicado, data_publicacao, autor_id) VALUES
('Introdução ao SQL', 'Neste post, vamos aprender o básico do SQL...', TRUE, '2024-01-10', 1),
('Modelagem de Dados', 'Um guia completo sobre modelagem de bancos de dados relacionais.', TRUE, '2024-01-15', 2),
('Avançando com Python', 'Dicas e truques para programadores Python intermediários.', TRUE, '2024-02-01', 1),
('O que há de novo em tecnologia?', 'Análise das principais tendências de tecnologia para este ano.', TRUE, '2024-02-20', 4),
('Rascunho do post sobre nuvem', 'Explorando os serviços de AWS, Azure e GCP...', FALSE, '2024-03-05', 3),
('SQL para Análise de Dados', 'Como usar SQL para extrair insights valiosos.', TRUE, '2024-03-12', 2),
('Gerenciamento de Projetos Ágeis', 'Scrum e Kanban na prática.', TRUE, '2024-04-01', 5),
('A importância da segurança digital', 'Proteja seus dados contra ameaças.', TRUE, '2024-04-25', 4),
('Revisão do novo framework JS', 'Este post ainda precisa ser revisado.', FALSE, '2024-05-10', 1),
('Carreira em tecnologia: por onde começar?', 'Um guia para iniciantes na área de TI.', TRUE, '2024-05-18', 7),
('Receitas com poucos ingredientes', 'Cozinhando de forma fácil e rápida.', TRUE, '2024-06-02', 6),
('Como otimizar queries SQL', 'Melhorando a performance do seu banco de dados.', TRUE, '2024-06-15', 2),
('Guia de Viagem para a Patagônia', 'Dicas de roteiro, hospedagem e passeios.', TRUE, '2024-07-01', 5),
('Entendendo Machine Learning', 'Conceitos fundamentais para quem quer iniciar na área.', TRUE, '2024-07-22', 4),
('Post de teste (não publicar)', 'Apenas um teste de sistema.', FALSE, '2024-08-01', 3),
('Desenvolvimento Web Moderno', 'Construindo aplicações com React e Node.js.', TRUE, '2023-11-20', 1),
('Finanças Pessoais para Iniciantes', 'Como organizar seu orçamento e começar a investir.', TRUE, '2023-12-05', 7),
('A História da Computação', 'Dos primeiros computadores à era da internet.', TRUE, '2023-10-15', 2),
('Dicas de Produtividade', 'Como ser mais produtivo no trabalho remoto.', TRUE, '2023-09-01', 5),
('Introdução à jardinagem', 'Como cuidar das suas primeiras plantas.', TRUE, '2023-08-10', 6),
('Análise de Mercado Financeiro', 'Tendências para o segundo semestre.', TRUE, '2024-08-15', 4);

# Exercicio 1
SELECT nome, email FROM autores;

# Exercicio 2
SELECT * FROM posts WHERE publicado = FALSE;

# Exercicio 3
SELECT titulo FROM posts WHERE autor_id = 1;

# Exercicio 4
SELECT nome FROM autores WHERE nome LIKE "A%";

# Exercicio 5 
SELECT * FROM posts WHERE autor_id = 2 AND publicado = TRUE;

# Exercicio 6
SELECT * FROM posts ORDER BY data_publicacao;

# Exercicio 7
SELECT * FROM posts ORDER BY data_publicacao DESC LIMIT 5;

# Exercicio 8
SELECT * FROM autores WHERE id IN(2, 4, 7);

# Exercicio 9
SELECT * FROM posts WHERE titulo LIKE "%tecnologia%";

# Exercicio 10
SELECT * FROM posts ORDER BY titulo LIMIT 10 OFFSET 10;

