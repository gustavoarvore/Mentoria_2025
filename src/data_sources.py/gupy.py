import requests
import json
import os

SETTINGS = {
    "file_path": "./data/vagas_gupy.json",
    "palavras_chave": ["dados"],
    "offsets": range(0, 200)  
}

def buscar_vagas():
    todas_vagas = []
    os.makedirs(os.path.dirname(SETTINGS["file_path"]), exist_ok=True)

    for palavra in SETTINGS["palavras_chave"]:
        print(f"\nBuscando vagas para: {palavra}")

        for offset in SETTINGS["offsets"]:
            url = f'https://portal.api.gupy.io/api/job?name={palavra}&offset={offset}&limit=10'
            resposta = requests.get(url)

            if resposta.status_code != 200:
                print(f"Erro ao buscar vagas")
                break

            dados = resposta.json()
            vagas = dados.get("data", [])

            todas_vagas.extend(vagas)

    with open(SETTINGS["file_path"], "w", encoding="utf-8") as gupy:
        json.dump(todas_vagas, gupy, ensure_ascii=False, indent=2)


buscar_vagas()
