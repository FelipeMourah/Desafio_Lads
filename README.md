# Desafio Lads Unama - Felipe Santos de Moura
---
## 📊 GitHub Languages Trend

---

## 🎯 Objetivo

Analisar as linguagens de programação mais populares entre os repositórios com maior número de estrelas no GitHub, utilizando a API pública da plataforma.  
Os dados são processados com Python e apresentados por meio de um gráfico gerado automaticamente.

---

## ⚙️ Tecnologias Utilizadas

- Python 3.x  
- [Requests](https://pypi.org/project/requests/) — Consumo da API do GitHub  
- [Matplotlib](https://matplotlib.org/) — Geração de gráficos

---

## 🚀 Como Rodar o Projeto

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu-usuario/github-languages-trend.git
   cd github-languages-trend
   ```
   ---
(Opcional) Crie um ambiente virtual:

```bash
python3 -m venv venv
source venv/bin/activate     # Linux/macOS
venv\Scripts\activate        # Windows
```
---
Instale as dependências:

```bash
python3 -m pip install -r requirements.txt
```
---
Execute o projeto:

```bash
python3 main.py
```

📈 Resultado: Um gráfico será salvo como grafico_linguagens.png no diretório raiz, exibindo as linguagens mais utilizadas nos repositórios mais populares do GitHub.
---
📂 Estrutura do Projeto
```bash
github-languages-trend/
├── main.py                # Código principal
├── requirements.txt       # Dependências
├── grafico_linguagens.png # Gráfico gerado após execução
└── README.md              # Documentação do projeto
```
---
📦 Requisitos (requirements.txt)
```txt
requests
matplotlib
```
---
💡 Sessão Inspirada

Este projeto foi inspirado na proposta da 2ª fase do processo seletivo da LADS UNAMA, que busca avaliar raciocínio lógico, clareza na comunicação e capacidade de aplicar conceitos em ciência de dados ou inteligência artificial.

Referência de inspiração: Real-Estate-Data-Analysis, adaptado para um contexto mais voltado à tecnologia e às tendências em programação.
