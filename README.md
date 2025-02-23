# Shop Management System 🛍️

Sistema de gerenciamento de loja com Python + MySQL para controle de:
- **Usuários** (Gerentes/Vendedores)
- **Produtos** (Estoque e Preços)
- **Clientes** (Cadastro completo)
- **Pedidos** (Processamento e Relatórios)

## Funcionalidades Principais ✨
- ✅ CRUD completo para todas entidades
- 🛒 Criação de pedidos com atualização automática de estoque
- 📊 Relatórios de:
  - Produtos mais vendidos
  - Clientes com menor movimentação
  - Histórico completo de pedidos
- 🔒 Controle de acesso por tipo de usuário


## Estrutura do Projeto 📂

shop/
├── models/ # Lógica de banco de dados
├── views/ # Interface do usuário
├── controllers/ # Regras de negócio
├── BD.sql # Script de criação do banco
└── main.py # Ponto de entrada
