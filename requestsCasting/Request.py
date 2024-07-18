from endpoints.Endpoints import Endpoints

# Defina a URL da requisição
url1 = Endpoints.URL1
#url2 = Endpoints.URL2

# Faça as requisições GET e processe as respostas
response1 = Endpoints.get_data_from_url(url1)
Endpoints.process_response(response1, "GetDadosFechamento")

#response2 = Endpoints.get_data_from_url(url2)
#Endpoints.process_response(response2, "URL2")