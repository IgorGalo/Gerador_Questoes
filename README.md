# Gerador Inteligente de Questões para Estudos

Aplicação desenvolvida para o Trabalho Prático 2 da disciplina de **Inteligência Artificial**, com o objetivo de transformar textos didáticos em questões de revisão utilizando um Grande Modelo de Linguagem (LLM).

O sistema permitirá que estudantes e professores forneçam um conteúdo de estudo e gerem automaticamente questões relacionadas ao material, com respostas corretas e explicações. A aplicação também contará com um modo simulado para responder às questões e visualizar o desempenho.

## Objetivos

- Facilitar a criação de questões de revisão a partir de textos didáticos.
- Utilizar um modelo de linguagem pré-treinado para interpretar o conteúdo fornecido.
- Gerar questões relacionadas às informações presentes no texto, evitando acrescentar conteúdo sem fundamento no material.
- Apoiar a avaliação da qualidade das questões geradas.

## Funcionalidades previstas

- **Entrada de conteúdo:** permite colar um texto ou enviar um arquivo `.txt`.
- **Configuração das questões:** permite selecionar a quantidade e o tipo de questões.
- **Geração automática:** cria questões com base no conteúdo fornecido.
- **Tipos de questões:** múltipla escolha, verdadeiro ou falso e resposta curta.
- **Gabarito e explicações:** apresenta a resposta correta e uma breve justificativa para cada questão.
- **Modo simulado:** permite responder às questões e visualizar a pontuação e as respostas corretas ao final.

## Tecnologias

- **Python** — linguagem utilizada no desenvolvimento.
- **Streamlit** — construção da interface da aplicação.
- **Hugging Face Transformers** — carregamento e utilização do modelo de linguagem.
- **PyTorch** — execução do modelo.
- **Qwen2.5-1.5B-Instruct** — modelo de linguagem escolhido para interpretar os textos e gerar as questões.

Modelo: [`Qwen/Qwen2.5-1.5B-Instruct`](https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct)

A geração será orientada por prompts, sem realização de ajuste fino (*fine-tuning*) do modelo.

## Organização do repositório

A estrutura abaixo é uma sugestão inicial e poderá ser adaptada conforme a implementação:

```text
.
├── app.py                  # Ponto de entrada da aplicação Streamlit
├── src/                    # Módulos da aplicação e integração com o modelo
├── data/                   # Textos e materiais utilizados nos testes
├── tests/                  # Testes da aplicação
├── docs/                   # Relatório, imagens e materiais da documentação
├── requirements.txt        # Dependências do projeto
└── README.md               # Documentação principal
```

Não é necessário manter exatamente essa estrutura; atualizem os caminhos conforme os arquivos reais do projeto forem criados.

## Como executar

As instruções definitivas de instalação e execução serão atualizadas quando a estrutura e os arquivos do projeto estiverem definidos.

### 1. Pré-requisitos

- Python instalado.
- Git instalado.
- Conexão com a internet para instalar as dependências e, quando necessário, baixar o modelo.

### 2. Clonar o repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd <NOME_DA_PASTA>
```

### 3. Criar e ativar um ambiente virtual

**Windows (PowerShell):**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**Linux/macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Instalar as dependências

Depois que o arquivo `requirements.txt` estiver configurado:

```bash
pip install -r requirements.txt
```

A instalação do PyTorch pode variar conforme o sistema operacional e o uso de CPU ou GPU. Consultem a [página oficial de instalação do PyTorch](https://pytorch.org/get-started/locally/) para selecionar o comando adequado ao ambiente.

### 5. Executar a aplicação

Quando o arquivo principal estiver definido como `app.py`, a aplicação poderá ser iniciada com:

```bash
streamlit run app.py
```

## Dados e avaliação

Os testes utilizarão textos didáticos em português, selecionados principalmente no [Wikilivros em português](https://pt.wikibooks.org/). Também será preparado um pequeno conjunto de textos acompanhado de questões e respostas de referência, elaboradas e revisadas manualmente.

A avaliação considerará, entre outros aspectos:

- **Relação com o texto:** se as questões geradas correspondem ao conteúdo fornecido.
- **Correção das respostas:** se o gabarito está correto em relação ao material.
- **Clareza:** se os enunciados, alternativas e explicações são compreensíveis.

Os materiais de terceiros utilizados nos testes deverão ter suas licenças verificadas e os devidos créditos atribuídos.

## Desenvolvimento em equipe

O projeto será desenvolvido colaborativamente por dois integrantes. Recomenda-se que cada integrante trabalhe em uma branch própria e que as alterações sejam integradas à branch principal após revisão e testes.

Exemplo de fluxo de trabalho:

```bash
# Atualizar a branch principal
git switch main
git pull

# Criar uma branch para uma tarefa
git switch -c feature/nome-da-tarefa

# Registrar alterações
git add .
git commit -m "Descrição da alteração"

# Enviar a branch ao GitHub
git push -u origin feature/nome-da-tarefa
```

Depois, abram um *Pull Request* no GitHub para revisar e integrar as alterações à branch principal. Evitem desenvolver diretamente na `main` e não enviem arquivos de ambiente virtual, caches ou arquivos com credenciais para o repositório.

## Integrantes

- Igor Luís Galo
- Yuri Codreanski Collinett Guimarães

## Contexto acadêmico

Trabalho Prático 2 — Disciplina de Inteligência Artificial  
Universidade Federal de São João del-Rei (UFSJ)  
Professora: Érica Carvalho
