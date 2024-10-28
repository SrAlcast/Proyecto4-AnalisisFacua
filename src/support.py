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

def sacar_tabla1(sopa):
    # Extraer el título del <h2>
    title = sopa.find('h2').text.strip('Tabla de precios por día para')

    info = [item.text.strip() for item in sopa.select('li.breadcrumb-item')][1:]

    # Extraer datos de la tabla
    data = []
    for fila in sopa.find_all('tr')[1:]:  # Omitir la fila de encabezados
        columnas = fila.find_all('td')
        dia = columnas[0].text.strip()
        precio = columnas[1].text.strip()
        variacion = columnas[2].text.strip()
        data.append([dia, precio, variacion])

    # Convertir en DataFrame de pandas
    df = pd.DataFrame(data, columns=["Día", "Precio (€)", "Variación"])

    # Agregar el título como una columna adicional
    df['Nombre'] = title
    df['Supermercado'] = info[0]
    df['Tipo producto'] = info[1]
    try:
        df['Tipo subproducto'] = info[2]
    except: None
    return df

def sacar_tabla2(sopa):
    try:
        # Extraer el título del <h2>
        title = sopa.find('h2').text.strip('Comparativa de precios de')
        info = [item.text.strip() for item in sopa.select('li.breadcrumb-item')][1:]

        # # Extraer datos de la tabla
        tabla_precios = sopa.find_next("table")

        # Si la tabla está en divs en lugar de una tabla HTML
        if not tabla_precios:
            tabla_precios = sopa.find_next("div", class_="tabla-precios")  # Ajusta la clase si es necesario

        # Almacena los datos en listas y convierte a DataFrame
        if tabla_precios:
            filas = tabla_precios.find_all("tr")
            data = []
            for fila in filas:
                columnas = fila.find_all(["td", "th"])  # Considera tanto headers como datos
                datos = [columna.get_text(strip=True) for columna in columnas]
                if len(datos) == 3:  # Solo agrega filas que tengan las tres columnas Día, Precio, Variación
                    data.append(datos)

            # Crear el DataFrame con encabezados específicos
        df = pd.DataFrame(data, columns=["Día", "Precio (€)", "Variación"]).drop([0, 1]).reset_index(drop=True)
        # Agregar el título como una columna adicional
        df['Nombre'] = title
        df['Supermercado'] = info[0]
        df['Tipo producto'] = info[1]
        return df
    except:
        return print("Error al sacar tabla")