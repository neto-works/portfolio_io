## Tabela de Usuários:

user_id (chave primária)
username
email
senha

## Tabela de Posts do Blog:

post_id (chave primária)
título
conteúdo
data_publicação
user_id (chave estrangeira referenciando a tabela de usuários para identificar o autor do post)

## Tabela de Categorias do Blog:

category_id (chave primária)
nome_categoria
Tabela de Relacionamento entre Posts e Categorias:

post_id (chave estrangeira referenciando a tabela de posts do blog)
category_id (chave estrangeira referenciando a tabela de categorias do blog)

## Tabela de Projetos do Portfólio:

project_id (chave primária)
título
descrição
imagem (caminho para a imagem do projeto)
user_id (chave estrangeira referenciando a tabela de usuários para identificar o autor do projeto)

Com esse esquema de banco de dados, você pode armazenar informações sobre usuários, 
posts do blog, categorias do blog, projetos do portfólio e os relacionamentos entre eles.
Por exemplo, cada post do blog pode estar associado a um autor específico (usuário), e pode pertencer a 
uma ou mais categorias. Da mesma forma, cada projeto do portfólio está associado a um usuário específico.