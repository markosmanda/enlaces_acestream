import json

# Define la ruta del archivo JSON de entrada y el archivo M3U de salida
archivo_json = 'channels.json'
archivo_m3u = 'canales.m3u'

# Función para cargar el JSON y crear el archivo M3U
def json_a_m3u(archivo_json, archivo_m3u):
    try:
        # Abre el archivo JSON
        with open(archivo_json, 'r') as json_file:
            data = json.load(json_file)
            
        # Abre el archivo M3U para escritura
        with open(archivo_m3u, 'w') as m3u_file:
            # Escribe la cabecera M3U
            m3u_file.write("#EXTM3U\n")
            
            # Recorre los canales y escribe las entradas M3U
            for canal in data:
                nombre = canal["Name"]
                url = canal["Link"]
                image = canal["Image"]
                
                m3u_file.write(f"#EXTINF:-1,{nombre}\n{url}\n{image}")
                
        print(f'Archivo M3U creado: {archivo_m3u}')
    except Exception as e:
        print(f'Ocurrió un error: {e}')

# Llama a la función para convertir JSON a M3U
json_a_m3u(archivo_json, archivo_m3u)
