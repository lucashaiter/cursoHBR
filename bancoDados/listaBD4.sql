DROP SCHEMA Lista4BD;
CREATE SCHEMA Lista4BD;
USE Lista4BD;

CREATE TABLE clientes (
    id INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cidade VARCHAR(50)
);

CREATE TABLE pedidos (
    id INT PRIMARY KEY,
    cliente_id INT,
    produto VARCHAR(100),
    valor DECIMAL(10, 2),
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);

INSERT INTO clientes (id, nome, cidade) VALUES
(1, 'João Silva', 'São Paulo'),
(2, 'Maria Santos', 'Rio de Janeiro'),
(3, 'Carlos Souza', 'São Paulo'),
(4, 'Ana Costa', 'Belo Horizonte'); 

INSERT INTO pedidos (id, cliente_id, produto, valor) VALUES
(101, 1, 'Notebook', 3500.00),
(102, 2, 'Smartphone', 1800.00),
(103, 1, 'Mouse', 150.00),
(104, 3, 'Teclado', 300.00),
(105, 2, 'Carregador', 120.00);



# Exercicio 1
SELECT c.nome, p.produto FROM clientes AS c INNER JOIN pedidos AS p ON c.id = p.cliente_id;

# Exercicio 2
SELECT c.cidade, c.nome, p.valor FROM clientes AS c INNER JOIN pedidos AS p ON c.id = p.cliente_id WHERE c.cidade = "São Paulo";

# Exercicio 3
SELECT c.nome, sum(p.valor) FROM clientes AS c INNER JOIN pedidos AS p ON c.id = p.cliente_id GROUP BY c.nome;

# Exercicio 4
SELECT c.nome, p.produto FROM clientes AS c LEFT JOIN pedidos AS p ON c.id = p.cliente_id;

# Exercicio 5
SELECT c.nome, p.produto FROM clientes AS c LEFT JOIN pedidos AS p ON c.id = p.cliente_id WHERE p.produto IS NULL;

# Exercicio 6
SELECT c.nome, p.produto FROM clientes AS c RIGHT JOIN pedidos AS p ON c.id = p.cliente_id;

# Exercicio 7
SELECT c.nome, p.produto FROM clientes AS c CROSS JOIN pedidos AS p;

# Exercicio 8
SELECT c.nome, count(p.produto) FROM clientes AS c LEFT JOIN pedidos AS p ON c.id = p.cliente_id GROUP BY c.nome;

# Exercicio 9
SELECT c.nome, p.produto FROM clientes AS c INNER JOIN pedidos AS p ON c.id = p.cliente_id WHERE p.produto = "Notebook";

# Exercicio 10
SELECT c.nome, p.produto, p.valor FROM clientes AS c INNER JOIN pedidos AS p ON c.id = p.cliente_id WHERE p.valor = (SELECT max(valor) FROM pedidos);
