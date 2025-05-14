import json

CONFIG_PATH = 'config.json'

def ler_config():
    try:
        with open('config.json') as f:
            _data = json.load(f)
    except Exception as e:
        print(f"[CONFIG ERRO] Falha ao carregar config.json: {e}")
        _data = {}
    return _data

def salvar_config(**kwargs):
    config = ler_config()  # Lê o JSON
    for chave, valor in kwargs.items():
        config[chave] = valor  # Atualiza cada item
    with open(CONFIG_PATH, 'w') as f:
        json.dump(config, f, indent=4)  # Salva no JSON

