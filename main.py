import requests
import matplotlib.pyplot as plt
import time

def get_trending_languages_paginated(pages=10):
    language_count = {}

    for page in range(1, pages + 1):
        print(f"🔄 Buscando dados da página {page}...")
        url = f"https://api.github.com/search/repositories?q=stars:>1&sort=stars&page={page}&per_page=100"
        headers = {"Accept": "application/vnd.github.v3+json"}
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            print(f" Erro na página {page}: {response.status_code}")
            continue

        items = response.json().get("items", [])
        for repo in items:
            language = repo.get("language")
            if language:
                language_count[language] = language_count.get(language, 0) + 1

        time.sleep(1.5)  # Evita rate limite da API pública

    sorted_languages = sorted(language_count.items(), key=lambda x: x[1], reverse=True)
    # vai retornar as 10 melhores
    return sorted_languages[:10]  

def plot_languages(data):
    languages, counts = zip(*data)
    plt.figure(figsize=(10, 8))
    plt.bar(languages, counts, color='darkblue')
    plt.title("As 10 Melhores Linguagens de Programação em Repositórios Populares no GitHub")
    plt.xlabel("Linguagens")
    plt.ylabel("Quantidade de Repositórios")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("grafico_linguagens.png")
    print("📊 Gráfico salvo como grafico_linguagens.png")

if __name__ == "__main__":
    dados = get_trending_languages_paginated(pages=10)
    for lang, count in dados:
        print(f"{lang}: {count}")
    plot_languages(dados)
