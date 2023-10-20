import json

# Carga el JSON desde el archivo channels.json
with open('channels.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Función para generar una línea M3U para un canal
def generate_m3u_entry(channel):
    tvg_logo = channel["Image"]
    tvg_id = channel["Name"]
    stream_url = channel["Link"]
    return f'#EXTINF:-1 tvg-logo="{tvg_logo}" tvg-id="{tvg_id}",{tvg_id}\n{stream_url}\n'

# Genera las líneas M3U para todos los canales
m3u_entries = [generate_m3u_entry(channel) for channel in data]

# Guarda las líneas M3U en un archivo
with open('canales.m3u', 'w', encoding='utf-8') as m3u_file:
    m3u_file.write('\n'.join(m3u_entries))

print('Archivo M3U generado con éxito.')
