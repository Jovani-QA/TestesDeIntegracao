# endpoints/endpoints.py
import requests
import json
from config.Config import Config

class Endpoints:
    #cafdeinaURL1 = "https://hcm.serhcm.com.br/Casting/AppServices/api/Vendas/GetVendasPeriodo/?periodoId=b9883ea1-61a2-45ac-b3fd-5818ccb0c71b"
    URL1 = "http://cstng.serhcm.com.br/Casting/API/api/Metas/GetMetasUnidade/?periodoId=58941765-da95-4a4d-83af-cc378a1cdded&metaQtd=:1"
    #URL3 = " "
    #URL4 = " "
    #URL5 = " "
    #URL6 = " "


    @staticmethod
    def print_colored_message(message, color):
        colors = {
            "green": "\033[92m",
            "red": "\033[91m",
            "reset": "\033[0m"
        }
        colored_message = f"{colors[color]}{message}{colors['reset']}"
        print(colored_message)

    @staticmethod
    def get_data_from_url(url):
        response = requests.get(url, headers=Config.HEADERS)
        return response

    @staticmethod
    def process_response(response, endpoint_name):
        if response.status_code == 200:
            success_message = f"Requisição bem-sucedida para o endpoint {endpoint_name}!"
            Endpoints.print_colored_message(success_message, "green")
            print(json.dumps(response.json(), ensure_ascii=False, indent=4))
        else:
            error_message = f"Falha na requisição para o endpoint {endpoint_name}. Código de status: {response.status_code}"
            Endpoints.print_colored_message(error_message, "red")
            print(response.text)
