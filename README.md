# GastroFlow - Sistema de Gestão para Empreendimentos Alimentícios

<p align="center">
  <img src="logo.png" alt="GastroFlow Logo" width="200"/>
</p>

<p align="center">
  <strong>Sistema de gestão completo desenvolvido para empreendimentos do setor alimentício</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python Version"/>
  <img src="https://img.shields.io/badge/Database-MySQL-orange.svg" alt="Database"/>
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License"/>
  <img src="https://img.shields.io/badge/Status-Concluído-success.svg" alt="Status"/>
</p>

---

## Sobre o Projeto

**GastroFlow** é um sistema de gestão desenvolvido como projeto acadêmico do **3º ano do SENAC**, focado em simular operações reais de um empreendimento alimentício, como restaurantes, lanchonetes, bares e cafeterias.

O sistema oferece funcionalidades essenciais para o gerenciamento eficiente do negócio, incluindo controle de estoque, pedidos, cardápio, relatórios e muito mais.

### Objetivos do Projeto
- Aplicar conceitos de programação estruturada e orientada a objetos
- Implementar persistência de dados com banco de dados SQL
- Desenvolver interface de usuário funcional
- Simular fluxos de trabalho reais de um negócio alimentício
- Praticar boas práticas de desenvolvimento de software

---

## Funcionalidades

### Gestão de Cardápio
- Cadastro de produtos e itens do menu
- Categorização de produtos (bebidas, pratos, sobremesas, etc.)
- Definição de preços e descrições
- Edição e remoção de itens

### Controle de Estoque
- Gerenciamento de ingredientes e insumos
- Controle de quantidades disponíveis
- Alertas de estoque baixo
- Histórico de movimentações

### Sistema de Pedidos
- Registro de pedidos de clientes
- Cálculo automático de valores
- Status de pedidos (pendente, em preparo, concluído)
- Histórico de pedidos

### Relatórios e Dashboard
- Relatório de vendas por período
- Produtos mais vendidos
- Faturamento total
- Análise de desempenho

### Gestão de Usuários
- Cadastro de funcionários
- Controle de acesso
- Registro de atividades

---

## Tecnologias Utilizadas

| Tecnologia | Descrição |
|-----------|-----------|
| **Python 3.8+** | Linguagem principal do projeto |
| **MySQL** | Banco de dados relacional |
| **Tkinter/CustomTkinter** | Interface gráfica (GUI) |
| **SQL** | Linguagem de consulta ao banco de dados |

---

## Estrutura do Projeto

```
empreendimento_alimenticios/
├── main.py                              # Arquivo principal de execução
├── db.py                                # Módulo de conexão com banco de dados
├── empreendimento_alimenticio_db.sql    # Script SQL para criação do banco
├── logo.png                             # Logo do sistema
├── icones/                              # Ícones da interface
│   └── ...
├── __pycache__/                         # Arquivos compilados Python
├── GastroFlow.rar                       # Versão empacotada do sistema
├── empreendimento_alimenticio_beta.zip  # Versão beta
└── README.md                            # Documentação do projeto
```

---

## Como Executar

### Pré-requisitos
- Python 3.8 ou superior instalado
- MySQL Server instalado e rodando
- Bibliotecas Python necessárias

### Passo 1: Clone o Repositório
```bash
git clone https://github.com/444dex/empreendimento_alimenticios.git
cd empreendimento_alimenticios
```

### Passo 2: Configure o Banco de Dados
```bash
# Acesse o MySQL
mysql -u root -p

# Crie o banco de dados
source empreendimento_alimenticio_db.sql
```

### Passo 3: Configure a Conexão (db.py)
Edite o arquivo `db.py` com suas credenciais do MySQL:
```python
DB_CONFIG = {
    'host': 'localhost',
    'user': 'seu_usuario',
    'password': 'sua_senha',
    'database': 'empreendimento_alimenticio'
}
```

### Passo 4: Instale as Dependências
```bash
pip install mysql-connector-python
pip install customtkinter  # Se usar interface gráfica moderna
```

### Passo 5: Execute o Sistema
```bash
python main.py
```

---

## Exemplo de Uso

### Cadastro de Produto
```python
# Exemplo de código para cadastrar um produto
produto = {
    'nome': 'Hambúrguer Clássico',
    'categoria': 'Lanches',
    'preco': 25.90,
    'descricao': 'Hambúrguer com queijo, alface e tomate'
}
cadastrar_produto(produto)
```

### Registro de Pedido
```python
# Exemplo de código para registrar um pedido
pedido = {
    'cliente': 'João Silva',
    'itens': [
        {'produto_id': 1, 'quantidade': 2},
        {'produto_id': 5, 'quantidade': 1}
    ],
    'total': 51.80
}
registrar_pedido(pedido)
```

---


## Esquema do Banco de Dados

```sql
-- Principais tabelas do sistema

CREATE TABLE produtos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    categoria VARCHAR(50),
    preco DECIMAL(10,2),
    estoque INT,
    descricao TEXT
);

CREATE TABLE pedidos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    cliente VARCHAR(100),
    data_pedido DATETIME,
    status VARCHAR(20),
    total DECIMAL(10,2)
);

CREATE TABLE itens_pedido (
    id INT PRIMARY KEY AUTO_INCREMENT,
    pedido_id INT,
    produto_id INT,
    quantidade INT,
    FOREIGN KEY (pedido_id) REFERENCES pedidos(id),
    FOREIGN KEY (produto_id) REFERENCES produtos(id)
);
```

---

## Contexto Acadêmico

Este projeto foi desenvolvido como **atividade avaliativa do 3º ano do curso de TI do SENAC**, com os seguintes objetivos pedagógicos:

- Aplicação prática de conceitos de Programação Orientada a Objetos
- Modelagem e implementação de banco de dados relacional
- Desenvolvimento de interface gráfica com Python
- Trabalho em equipe e gestão de projeto
- Documentação técnica de software

### Aprendizados Conquistados
- Integração entre frontend (interface) e backend (lógica + banco)
- Modelagem de dados para sistemas comerciais
- Tratamento de exceções e validação de dados
- Fluxo completo de CRUD (Create, Read, Update, Delete)
- Boas práticas de organização de código

---

## Contribuições

Este é um projeto acadêmico, mas sugestões e melhorias são bem-vindas!

Para contribuir:
1. Fork este repositório
2. Crie uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um Pull Request


---

## Licença

Este projeto está sob a licença **MIT**. Veja o arquivo `LICENSE` para mais detalhes.

---

## Autor

**444dex**
- GitHub: [Miguel "444dex" Kuipers](https://github.com/444dex)
- Projeto: Atividade Acadêmica SENAC - 3º Ano TI

---

## 🙏 Agradecimentos

- **SENAC** - Instituição de ensino
- Professores e orientadores do curso
- Colegas de turma que contribuíram com ideias
- Comunidade Python Brasil

---

<p align="center">
  <sub>Se este projeto foi útil para você, considere dar uma ⭐!</sub>
</p>
