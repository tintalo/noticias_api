import requests

API_KEY = "146b02655ac947c0a464fa8fd605f101"

url = f"https://newsapi.org/v2/top-headlines?language=es&category=technology&apiKey={API_KEY}"

response = requests.get(url)
data = response.json()

print("\n--- Últimas Noticias de Tecnología ---\n")
for i, article in enumerate(data["articles"][:5], 1):
    print(f"{i}. {article['title']}")
    print(article['url'])
    print()
