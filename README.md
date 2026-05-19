#  Conversor de Moedas em Tempo Real (Base BRL)

Um conversor de moedas dinâmico desenvolvido em Python que consome dados em tempo real da API [Frankfurter](https://api.frankfurter.dev/). 

O principal diferencial deste projeto é a sua **Arquitetura Modular (Multi-Frontend)**. A lógica de negócio e as requisições HTTP foram isoladas em um módulo central, permitindo que o sistema seja operado por duas interfaces completamente diferentes (Terminal e Web) sem a necessidade de reescrever o código de processamento.

##  Arquitetura e Diferenciais

- **Separação de Responsabilidades (Clean Architecture):** O núcleo lógico (`currency_converter.py`) é blindado e independente, não contendo código de interface gráfica ou prints de terminal.
- **Multi-Interface:** - **CLI (Command Line Interface):** Interface rápida e direta via terminal para desenvolvedores (`main.py`).
  - **GUI (Graphical User Interface):** Interface web interativa e amigável construída com Streamlit (`app.py`).
- **Resiliência e Tratamento de Erros:** Implementação de timeouts nas requisições HTTP e validação de chaves no dicionário JSON para evitar que a aplicação quebre em caso de falha na API externa.

##  Estrutura do Projeto

```text
📁 conversor_moedas
├── 📄 currency_converter.py  # Núcleo lógico e requisições à API
├── 📄 main.py                # Interface 1: Interação via Terminal
├── 📄 app.py                 # Interface 2: Aplicação Web (Streamlit)
└── 📄 README.md              # Documentação do projeto