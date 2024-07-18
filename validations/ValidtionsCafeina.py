import json

class ValidationsCafeina:
    @staticmethod
    def validate_response(response, endpoint_name):
        file_path = f"arquivosJson/{endpoint_name}.json"
        
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                expected_data = json.load(file)
        except FileNotFoundError:
            print(f"Arquivo {file_path} não encontrado.")
            return False
        except json.JSONDecodeError:
            print(f"Erro ao decodificar o JSON do arquivo {file_path}.")
            return False

        response_data = response.json()

        if not ValidationsCafeina.compare_objects(expected_data, response_data):
            print("As estruturas dos objetos não coincidem.")
            return False

        print("A resposta da API corresponde à estrutura esperada.")
        return True

    @staticmethod
    def compare_objects(expected, actual, path=""):
        if isinstance(expected, dict) and isinstance(actual, dict):
            for key in expected:
                if key not in actual:
                    print(f"Chave ausente na resposta da API: {path + key}")
                    return False
                if not ValidationsCafeina.compare_objects(expected[key], actual[key], path + f"{key}."):
                    return False
        elif isinstance(expected, list) and isinstance(actual, list):
            if len(expected) != len(actual):
                print(f"Tamanhos diferentes para listas em {path}")
                return False
            for index, item in enumerate(expected):
                if not any(ValidationsCafeina.compare_objects(item, actual_item, path + f"[{index}].") for actual_item in actual):
                    print(f"Item ausente na resposta da API: {path + str(item)}")
                    return False
        else:
            return True
        return True
