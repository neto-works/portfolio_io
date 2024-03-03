-- Geração de Modelo físico
-- Sql ANSI 2003 - brModelo.



CREATE TABLE Usuario (
id INTEGER PRIMARY KEY,
email VARCHAR(150),
password VARCHAR(50),
username VARCHAR(50)
)

CREATE TABLE Post (
id INTEGER PRIMARY KEY,
likes INTEGER,
titulo VARCHAR(200),
descricao VARCHAR(500),
usuario_id INTEGER,
FOREIGN KEY(usuario_id) REFERENCES Usuario (id)
)

CREATE TABLE Categoria (
id INTEGER PRIMARY KEY,
titulo VARCHAR(200)
)

CREATE TABLE Projeto (
id INTEGER PRIMARY KEY,
titulo VARCHAR(200),
descricao VARCHAR(500),
imagem VARCHAR(500),
url VARCHAR(500),
usuario_id INTEGER,
FOREIGN KEY(usuario_id) REFERENCES Usuario (id)
)

CREATE TABLE possui (
categoria_id INTEGER,
post_id INTEGER,
FOREIGN KEY(categoria_id) REFERENCES Categoria (id),
FOREIGN KEY(post_id) REFERENCES Post (id)
)

-- Erro: Nome de tabela duplicado (este erro compromete a integridade referencial)!
CREATE TABLE possui (
categoria_id INTEGER,
usuario_d INTEGER,
FOREIGN KEY(categoria_id) REFERENCES Categoria (id),
FOREIGN KEY(usuario_d) REFERENCES Projeto (id)
)

