# endpoints/endpoints.py
import requests
import json
from config.ConfigCafeina import Cafeinaheaders
from validations.ValidtionsCafeina import ValidationsCafeina

class EndpointsCafeina:
    
    URL1 = "https://hcm.serhcm.com.br/Casting/AppServices/api/Vendas/getVendasPeriodo/?unidadeId=627e1099-d821-4db7-a6db-3b0c538f7173&periodoId=b9883ea1-61a2-45ac-b3fd-5818ccb0c71b&t"
    #URL2 = "http://cstng.serhcm.com.br/Casting/API/api/Metas/GetMetasUnidade/?periodoId=58941765-da95-4a4d-83af-cc378a1cdded&metaQtd=:1"
    #URL1 = "http://cstng.serhcm.com.br/Casting/API/api/Common/GetDadosFechamento/"
    #URL2 = "http://cstng.serhcm.com.br/Casting/API/api/Metas/GetMetasUnidade/?periodoId=58941765-da95-4a4d-83af-cc378a1cdded&metaQtd=:1"
    #URL3  = "https://hcm.serhcm.com.br/Casting/AppServices/api/Periodo/GetPeriodoSelecionadoData/?selecionado=null"
    URL3 = "https://hcm.serhcm.com.br/Casting/AppServices/api/Post/GetNewPostCount/?FunId=21e2a637-ea74-475e-a7fb-91a32e674e23"
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
        response = requests.get(url, headers=Cafeinaheaders.HEADERS)
        return response

    @staticmethod
    def process_response(response, endpoint_name):
        if response.status_code == 200:
            success_message = f"Requisição bem-sucedida para o endpoint {endpoint_name}!"
            EndpointsCafeina.print_colored_message(success_message, "green")
            #print(json.dumps(response.json(), ensure_ascii=False, indent=4))

            # Chama a validação aqui
            ValidationsCafeina.validate_response(response, endpoint_name)
        else:
            error_message = f"Falha na requisição para o endpoint {endpoint_name}. Código de status: {response.status_code}"
            EndpointsCafeina.print_colored_message(error_message, "red")
            print(response.text)
