
import requests
import matplotlib.pyplot as plt

linguagens_validas = ["Python","JavaScript","TypeScript","Java","C#","C++","PHP","C","GO","Ruby","Rust","Kotlin","Swift","Dart","Lua","Objective-C","Perl","R","Scala"]

def get_trending_languages(top_n=5):
    url = "https://api.github.com/search/repositories?q=stars:>1&sort=stars"
    headers = {"Accept": "application/vnd.github.v3+json"}
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        raise Exception("Erro ao acessar a API do GitHub")
    
    items = response.json()["items"]
    
    language_count = {}
    for repo in items:
        language = repo.get("language")
        if language and language in linguagens_validas:
            language_count[language] = language_count.get(language,0) + 1

    sorted_languages = sorted(language_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_languages[:top_n]

def plot_languages(data):
    languages, counts = zip(*data)
    plt.figure(figsize=(12, 12))
    plt.bar(languages, counts, color='darkblue')
    plt.title("Top 5 Linguagens de Programação em Repositórios Populares no GitHub")
    plt.xlabel("Linguagens")
    plt.ylabel("Quantidade de Repositórios por usúario")
    plt.xticks(rotation=50)
    plt.tight_layout()
    plt.savefig("grafico_linguagens.png")

if __name__ == "__main__":
    data = get_trending_languages()
    plot_languages(data)