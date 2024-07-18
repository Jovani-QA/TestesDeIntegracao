from endpoints.PointCafeina import EndpointsCafeina

# Defina a URL da requisição
url1 = EndpointsCafeina.URL1
#url2 = EndpointsCafeina.URL2
url3 = EndpointsCafeina.URL3

# Faça as requisições GET e processe as respostas
response1 = EndpointsCafeina.get_data_from_url(url1)
EndpointsCafeina.process_response(response1, "url1")

#response2 = Endpoints.get_data_from_url(url2)
#Endpoints.process_response(response2, "URL2")

response3 = EndpointsCafeina.get_data_from_url(url3)
EndpointsCafeina.process_response(response3, "URL3")