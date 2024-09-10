# Projeto de Data Science em Python

Este projeto apresenta uma estrutura base para análise de dados utilizando Python e suas principais bibliotecas para Data Science, com a estrutura do projeto criada no Visual Studio Code (VSCode).

## Estrutura do Projeto

A estrutura do projeto foi gerada usando o VSCode e está organizada da seguinte forma:

```
projetofiap2024/
│
├── .vscode/            # Configurações específicas do VSCode
├── data/               # Diretório para armazenar datasets
├── notebooks/          # Jupyter notebooks para análises exploratórias
├── src/                # Código-fonte do projeto
│   ├── __init__.py
│   ├── data_processing.py
│   ├── feature_engineering.py
│   └── modeling.py
├── tests/              # Testes unitários
├── .gitignore          # Arquivos e diretórios ignorados pelo Git
├── requirements.txt    # Dependências do projeto
└── README.md           # Este arquivo
```

## Bibliotecas Utilizadas

As principais bibliotecas utilizadas neste projeto são:

- pandas: para manipulação e análise de dados
- numpy: para computação numérica
- scikit-learn: para aprendizado de máquina
- matplotlib e seaborn: para visualização de dados

## Configuração do Ambiente no VSCode

1. Instale a extensão "Python" no VSCode
2. Selecione o interpretador Python apropriado (recomenda-se usar um ambiente virtual)
3. Instale a extensão "Jupyter" para trabalhar com notebooks diretamente no VSCode

## Como Usar

1. Clone este repositório
2. Abra a pasta do projeto no VSCode
3. Crie um ambiente virtual: `python -m venv venv`
4. Ative o ambiente virtual:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
5. Instale as dependências: `pip install -r requirements.txt`
6. Execute os notebooks na pasta `notebooks/` ou os scripts em `src/`

## Dicas para Usar o VSCode com Python e Data Science

- Use o "Python Interactive Window" para execução interativa de código
- Aproveite a integração do Git no VSCode para controle de versão
- Utilize a funcionalidade de depuração do VSCode para encontrar e corrigir erros
- Personalize suas configurações no arquivo `.vscode/settings.json`

## Contribuição

Contribuições são bem-vindas! Por favor, abra uma issue para discutir mudanças propostas.
