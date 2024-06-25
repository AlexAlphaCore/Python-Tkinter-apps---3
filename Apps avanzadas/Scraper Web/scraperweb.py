import requests
from bs4 import BeautifulSoup

def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza una excepción para códigos de estado HTTP no exitosos
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error al hacer la solicitud: {e}")
        return None

def parse_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    # Aquí puedes agregar el código para extraer la información que necesitas
    # Por ejemplo, si quieres extraer todos los títulos de los artículos en una página de noticias:
    titles = soup.find_all('h2', class_='article-title')
    for title in titles:
        print(title.get_text())

def main():
    url = 'https://vazzine.com/'  # Reemplaza con la URL de la página que deseas scrapear
    html = fetch_data(url)
    if html:
        parse_data(html)

if __name__ == "__main__":
    main()