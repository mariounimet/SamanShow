import requests
def init_data():
    print('cargando datos...')
    url = 'https://raw.githubusercontent.com/Algoritmos-y-Programacion/api_saman_show/main/api.json'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print('datos cargados')
        return data