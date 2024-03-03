<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=3498db&height=120&section=header"/>
<div align="center">
  <img src="https://github.com/oficina-do-brito/gym_io/blob/main/archive/modelagem/logo.png" width="70" height="70">
</div>

<h4 align="center">A portfolio to demonstrate what I do, projects, code sales, blog etc :call_me_hand:</h4>

<p align="center">
  [Project's badges]
</p>

<p align="center">
  <a href="https://github.com/oficina-do-brito/gym_io/blob/main/archive/modelagem/nomenclatura.md">Nomenclatura de banco de Dados</a> •
  <a href="#Modelo_Conceitual">Modelo Conceitual</a> •
   <a href="https://github.com/oficina-do-brito/gym_io/blob/main/archive/modelagem/breakpoints.md">Recursos</a> •
  <a href="https://github.com/oficina-do-brito/gym_io/blob/main/archive/modelagem/modelo_logico.jpg">Modelo Logico</a> •
  <a href="#Tecnologias_usadas">Tecnologias Usadas</a> •
  <a href="#Rodando_aplicação">Rodando aplicação</a> •
</p>

## Explicações

- Nesse projeto eu utilizo [Task](https://taskfile.dev/) para automatizar digitação no terminal então, se quizer voçê pode usar ele instalando via npm:

    ```
    npm install -g @go-task/cli
    ```
    - Uma coisa importante a se fazer é reiniciar o vscode depois de instalar o task, pelo menos no meu não apareceu as tasks de primeira :sweat_smile: tive que reiniciar.

## Modelo_Conceitual

<img src="https://github.com/oficina-do-brito/gym_io/blob/main/archive/modelagem/conceitual.jpg" />

## Tecnologias_usadas

IDE:

<img src="https://user-images.githubusercontent.com/25181517/192108891-d86b6220-e232-423a-bf5f-90903e6887c3.png" width="50" height="50">

Backend:

<img src="https://github.com/marwin1991/profile-technology-icons/assets/136815194/519bfaf3-c242-431e-a269-876979f05574" width="50" height="50"><img src="https://user-images.githubusercontent.com/25181517/117208740-bfb78400-adf5-11eb-97bb-09072b6bedfc.png" width="50" height="50">

Frontend:

<img src="https://user-images.githubusercontent.com/25181517/183897015-94a058a6-b86e-4e42-a37f-bf92061753e5.png" width="50" height="50"><img src="https://github.com/marwin1991/profile-technology-icons/assets/136815194/5f8c622c-c217-4649-b0a9-7e0ee24bd704" width="50" height="50"><img src="https://user-images.githubusercontent.com/25181517/202896760-337261ed-ee92-4979-84c4-d4b829c7355d.png" width="50" height="50"><img src="https://user-images.githubusercontent.com/25181517/183898054-b3d693d4-dafb-4808-a509-bab54cf5de34.png" width="50" height="50">

## Rodando_aplicação

### Pré Requisitos

- Se quiser rodar o projeto com banco já de database criado, é aconselhável ter o docker e docker-compose na sua máquina. Minha pessoa usa linux mint e ele esta na minhas ferramentas de developer e é muito fácil instalar [veja aqui](https://github.com/oficina-do-brito/p1_manutencao/blob/main/my_programs/programs.md).

> [!IMPORTANT]
> Renomear o arquivo ".env.example" para ".env" e colocar suas variaveis de ambiente antes de executar o projeto, ou qualquer task relacionada. Caso contrario ocorrerá erros na execução. A seguir o padrão para preenchimento:

- [ ] DB_HOST=localhost
- [ ] DB_TYPE= o tipo do seu banco de dados mysql, postgres etc... sugest:postgres
- [ ] DB_PORT= a porta que esta sendo exposta para connexao com db sugest:5432
- [ ] DB_USERNAME= username sugest:postgres
- [ ] DB_PASSWORD= password sugest:postgres
- [ ] DB_DATABASE= database sugest:api_ginasio
- [ ] SECRET_KEY= um segredo para construção do jwt sugest:qualquer_secredo_string
- [ ] SALT = um salt de encriptação de senhas sugest:qualquer_valor_numerico

### Rodando o projeto backend

`docker-compose up -d && npm i && npm run start:dev`

### Limpando todos containers e images usadas (cuidado)

`docker-compose down  && docker rmi $(docker images -q) && docker images`

## Rodando frontend

### Prerequisitos
- Ter a aplicação backend rodando.
- Certificar-se de estar com o [backend](https://github.com/oficina-do-brito/ginasio) rodando.

### Rodando

` npm i && npm run dev`


<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=3498db&height=120&section=footer"/>