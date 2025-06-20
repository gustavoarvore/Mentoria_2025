import requests
import json


def buscar_vagas():

    todas_vagas = []
    palavras_chave = ["dados"]
    limite = 10  
    info_paginacao = {}


    for palavra in palavras_chave:
        offset = 0
        total_vagas = None

        print(f"\nBuscando vagas para: {palavra}")
        
        while True:
            url = f'https://portal.api.gupy.io/api/job?name={palavra}&offset={offset}&limit={limite}'
            resposta = requests.get(url)

            if resposta.status_code != 200:
                print(f"Erro ao buscar vagas: {resposta.status_code}")
                break

            dados = resposta.json()
            vagas = dados.get("data", [])
            paginacao = dados.get("pagination", {})

            if total_vagas is None:
                total_vagas = paginacao.get("total", 0)
                info_paginacao[palavra] = paginacao

            if not vagas:
                break

            todas_vagas.extend(vagas)
            offset += limite

            if offset >= total_vagas:
                break

    resultado_final = {
        "vagas": todas_vagas,
        "pagination": info_paginacao
    }

#Trecho de código que salva os dados em um arquivo JSON
    with open("./data/vagas_gupy.json", "w", encoding="utf-8") as gupy:
        json.dump(resultado_final, gupy, ensure_ascii=False, indent=2)
    print("Vagas salvas com sucesso em './data/vagas_gupy.json'")

    return resultado_final

buscar_vagas()