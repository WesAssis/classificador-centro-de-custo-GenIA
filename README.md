# Classificador de Centro de Custo via XML de NF-e

Este projeto oferece uma solução inteligente para classificar automaticamente itens de Notas Fiscais Eletrônicas (NF-e) em centros de custo específicos, utilizando inteligência artificial. Desenvolvido com Streamlit, ele proporciona uma interface intuitiva para upload de arquivos XML, extração de dados relevantes e visualização das despesas classificadas, facilitando a gestão financeira e contábil de empresas.




## Funcionalidades

*   **Classificação Inteligente**: Utiliza IA para categorizar descrições de produtos/serviços em centros de custo.
*   **Processamento de XML**: Extrai automaticamente dados essenciais de arquivos XML de NF-e.
*   **Interface Intuitiva**: Desenvolvido com Streamlit para uma experiência de usuário amigável.
*   **Visualização de Dados**: Apresenta a distribuição de despesas por centro de custo através de gráficos interativos.
*   **Exportação de Dados**: Permite baixar os resultados da classificação em formato Excel (.xlsx).
*   **Suporte a Múltiplos Arquivos**: Capacidade de processar múltiplos arquivos XML simultaneamente.




## Tecnologias Utilizadas

*   **Python**: Linguagem de programação principal.
*   **Streamlit**: Framework para criação da interface web interativa.
*   **Pandas**: Biblioteca para manipulação e análise de dados.
*   **Plotly Express**: Biblioteca para criação de gráficos interativos.
*   **OpenAI API**: Utilizada para a classificação inteligente (assumindo que a IA é baseada em modelos da OpenAI, dado o contexto de "GenIA" e "prompt_classificacao.txt").
*   **LXML**: (Assumido) Biblioteca para parsing de XML.




## Como Usar

### Pré-requisitos

Certifique-se de ter o Python 3.8+ instalado em sua máquina.

### Instalação

1.  **Clone o repositório:**

    ```bash
    git clone https://github.com/WesAssis/classificador-centro-de-custo-GenIA.git
    cd classificador-centro-de-custo-GenIA
    ```

2.  **Crie e ative um ambiente virtual (recomendado):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3.  **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```


### Execução

1.  **Execute o aplicativo Streamlit:**

    ```bash
    streamlit run app.py
    ```

2.  **Acesse a interface:**

    O aplicativo será aberto automaticamente em seu navegador padrão (geralmente em `http://localhost:8501`).

### Configuração da API OpenAI

Para que a classificação inteligente funcione, você precisará configurar sua chave de API da OpenAI. Recomenda-se usar variáveis de ambiente para isso.

```bash
export OPENAI_API_KEY="sua_chave_api_aqui"
```

Ou crie um arquivo `.env` na raiz do projeto com o conteúdo:

```
OPENAI_API_KEY="sua_chave_api_aqui"
```

E carregue-o no `app.py` (se ainda não estiver sendo feito).




## Estrutura do Projeto

```
classificador-centro-de-custo-GenIA/
├── app.py                  # Aplicação principal Streamlit
├── core/                   # Lógica de negócio
│   ├── classificacao.py    # Funções de classificação com IA
│   └── parser.py           # Funções para parsing de XML
├── data/                   # Dados de exemplo (XMLs de NF-e)
│   ├── nfe_ficticia_01.xml
│   └── ...
├── prompts/                # Templates de prompts para a IA
│   └── prompt_classificacao.txt
├── utils/                  # Utilitários diversos
│   └── prompt_loader.py    # Função para carregar prompts
├── venv/                   # Ambiente virtual (gerado após instalação)
├── requirements.txt        # Dependências do projeto
└── README.md               # Este arquivo
```
