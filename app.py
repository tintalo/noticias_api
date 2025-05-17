from flask import Flask, render_template, request
import requests
import math

app = Flask(__name__)
API_KEY = "146b02655ac947c0a464fa8fd605f101"
CATEGORIAS = ["technology", "business", "health", "science", "sports", "entertainment"]
PAGE_SIZE = 10

@app.route('/')
def home():
    # Leer categoría y página de la URL
    categoria = request.args.get('category', 'technology')
    if categoria not in CATEGORIAS:
        categoria = 'technology'
    page = int(request.args.get('page', 1))

    # Llamada con paginación
    url = (
        f"https://newsapi.org/v2/everything?"
        f"q={categoria}&language=es"
        f"&sortBy=publishedAt&pageSize={PAGE_SIZE}&page={page}"
        f"&apiKey={API_KEY}"
    )
    r = requests.get(url)
    data = r.json()
    noticias = data.get("articles", [])
    total = data.get("totalResults", 0)
    total_pages = math.ceil(total / PAGE_SIZE)

    return render_template(
        "index.html",
        noticias=noticias,
        seleccion=categoria,  # << CORREGIDO: antes decía categoria_actual
        page=page,
        total_pages=total_pages
    )

@app.route('/search')
def search():
    termino = request.args.get('q', '').strip()
    page = int(request.args.get('page', 1))
    noticias = []
    total = 0
    total_pages = 0

    if termino:
        url = (
            f"https://newsapi.org/v2/everything?"
            f"q={termino}&language=es"
            f"&sortBy=publishedAt&pageSize={PAGE_SIZE}&page={page}"
            f"&apiKey={API_KEY}"
        )
        r = requests.get(url)
        data = r.json()
        noticias = data.get("articles", [])
        total = data.get("totalResults", 0)
        total_pages = math.ceil(total / PAGE_SIZE)

    return render_template(
        "search.html",
        noticias=noticias,
        termino=termino,
        page=page,
        total_pages=total_pages
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
