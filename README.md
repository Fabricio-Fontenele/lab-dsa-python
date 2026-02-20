<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white" />
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
</p>

<h1 align="center">📚 Formação Python — Data Science Academy</h1>

<p align="center">
  Repositório com todos os estudos, exercícios e mini-projetos desenvolvidos durante a <b>Formação Python para Análise de Dados</b> da <a href="https://www.datascienceacademy.com.br/">Data Science Academy</a>.
</p>

<p align="center">
  <img src="https://img.shields.io/github/last-commit/Fabricio-Fontenele/lab-dsa-python?style=flat-square&color=blue" />
  <img src="https://img.shields.io/badge/status-em%20andamento-yellow?style=flat-square" />
  <img src="https://img.shields.io/badge/capítulos-9+-green?style=flat-square" />
</p>

---

## 🗺️ Visão Geral

```
dsa/
├── 02-dsa-assistente/        → Mini-Projeto 1 — Assistente IA de Programação
├── 06.repeticao.../          → Repetição, Decisão e Modularização + Mini-Projeto
├── 07.poo/                   → Programação Orientada a Objetos + Mini-Projeto 2
├── 8.Numpy/                  → NumPy — Computação Numérica + Mini-Projeto 3
└── 9.pandas/                 → Pandas — Manipulação de Dados
```

---

## 🚀 Projetos em Destaque

### 🤖 Mini-Projeto 1 — DSA AI Coder
> **Assistente de programação com IA usando Streamlit + Groq API**

App web interativo que funciona como um assistente de programação Python alimentado por LLM. Construído com Streamlit para a interface e a API da Groq para acessar modelos de linguagem.

| Stack | |
|---|---|
| Interface | Streamlit |
| LLM Backend | Groq API |
| Funcionalidade | Chat interativo com foco em programação Python |

📁 `02-dsa-assistente/`

---

### 🏦 Mini-Projeto 2 — Sistema Bancário Digital
> **Aplicação full-stack em Python com POO**

Sistema bancário completo no terminal demonstrando conceitos avançados de Programação Orientada a Objetos: classes abstratas, herança, polimorfismo, encapsulamento e composição.

| Conceito | Implementação |
|---|---|
| Herança & Abstração | `BankAccount` (ABC) → `ContaCorrente`, `ContaPoupanca` |
| Encapsulamento | Atributos protegidos, `@property` para saldo |
| Composição | `Bank` gerencia `Client` e `BankAccount` |
| Exceções Customizadas | `InsufficientBalanceError`, `AccountNotFoundError` |

```
07.poo/mini-projeto-2/
├── main.py              # Menu principal da aplicação
├── entities/
│   ├── account.py       # Classes de conta (abstrata, corrente, poupança)
│   └── cliente.py       # Classe Cliente
├── operations/
│   └── bank.py          # Classe Banco (gerencia clientes e contas)
└── utils/
    └── exceptions.py    # Exceções personalizadas
```

📁 `07.poo/mini-projeto-2/`

---

### 📊 Mini-Projeto 3 — Análise Estatística para Marketing
> **Análise de dados de e-commerce com NumPy**

Análise estatística de dados de navegação e compras de uma plataforma de e-commerce, com o objetivo de segmentar clientes, identificar padrões de conversão e gerar insights acionáveis para as equipes de marketing/produto.

| Objetivo | Descrição |
|---|---|
| Segmentação | Clientes de Alto Valor vs. Visitantes sem Compra |
| Correlação | Tempo no site × Itens no carrinho × Valor da compra |
| Otimização | Insights para ROI de marketing e melhoria de UX |

📁 `8.Numpy/mini-projeto-3.ipynb`

---

## 📖 Conteúdo por Capítulo

| # | Capítulo | Conteúdo | Tipo |
|:-:|---|---|---|
| **02** | Assistente IA | Streamlit, Groq API, LLMs | 🐍 App |
| **06** | Repetição, Decisão e Modularização | Loops, condicionais, funções, análise de vendas | 📓 Notebook |
| **07** | Programação Orientada a Objetos | Classes, herança, abstração, polimorfismo, composição | 🐍 App |
| **08** | NumPy | Arrays, operações vetorizadas, álgebra linear, estatística | 📓 Notebook |
| **09** | Pandas | Series, DataFrames, leitura de CSV, manipulação de dados | 📓 Notebook |

---

## ⚙️ Como Usar

### Pré-requisitos
- Python 3.10+
- Jupyter Notebook / VS Code com extensão Jupyter

### Executar os Notebooks
```bash
# Clone o repositório
git clone https://github.com/Fabricio-Fontenele/lab-dsa-python.git
cd lab-dsa-python

# Crie um ambiente virtual
python -m venv .venv
source .venv/bin/activate

# Instale as dependências
pip install numpy pandas matplotlib seaborn jupyter

# Abra os notebooks
jupyter notebook
```

### Executar o Assistente IA (Mini-Projeto 1)
```bash
cd 02-dsa-assistente
pip install -r requirements.txt
streamlit run main.py
```

### Executar o Sistema Bancário (Mini-Projeto 2)
```bash
cd 07.poo/mini-projeto-2
python main.py
```

---

## 🛠️ Tecnologias

<table>
  <tr>
    <td align="center"><b>Linguagem</b></td>
    <td>Python 3</td>
  </tr>
  <tr>
    <td align="center"><b>Dados</b></td>
    <td>NumPy, Pandas</td>
  </tr>
  <tr>
    <td align="center"><b>Visualização</b></td>
    <td>Matplotlib, Seaborn</td>
  </tr>
  <tr>
    <td align="center"><b>Web/IA</b></td>
    <td>Streamlit, Groq API</td>
  </tr>
  <tr>
    <td align="center"><b>Ambiente</b></td>
    <td>Jupyter Notebook, VS Code</td>
  </tr>
</table>


