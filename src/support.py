import requests
from bs4 import BeautifulSoup

def obtener_sopa(url):
    # Hacer una solicitud HTTP a la URL
    response = requests.get(url)
    
    # Comprobar que la solicitud fue exitosa
    if response.status_code == 200:
        # Convertir el contenido de la página a BeautifulSoup
        sopa = BeautifulSoup(response.text, 'html.parser')
        return sopa
    else:
        print(f"Error al acceder a {url}: Código de estado {response.status_code}")
        return None


