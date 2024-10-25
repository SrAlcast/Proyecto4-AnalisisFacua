import requests
from bs4 import BeautifulSoup
import pandas as pd

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

def sacar_tabla(url):

    # Extraer el título del <h2>
    title = url.find('h2').text.strip('Tabla de precios por día para')

    # Localizar la tabla por su clase
    table = url.find('table', {'class': 'table table-striped table-responsive text-center'})

    # Extraer datos de la tabla
    data = []
    for row in table.find_all('tr')[1:]:  # Omitir la fila de encabezados
        cols = row.find_all('td')
        day = cols[0].text.strip()
        price = cols[1].text.strip()
        variation = cols[2].text.strip()
        data.append([day, price, variation])

    # Convertir en DataFrame de pandas
    df = pd.DataFrame(data, columns=["Día", "Precio (€)", "Variación"])

    # Agregar el título como una columna adicional
    df['Producto'] = title
