
import json
import os


def salvar_historico(nome_cidade, temperatura_atual, sensacao_terminca, descricao_tempo, umidade,horario_formatado, longitude, latitude):
   
    dados_historico = {
        "nome_cidade": nome_cidade,
        "temperatura_atual": temperatura_atual,
        "sensacao": sensacao_terminca,
        "descricao": descricao_tempo,
        "umidade": umidade,
        "data_hora": horario_formatado,
        "coordenadas": {"lon": longitude, "lat": latitude}
    }

    try:
         #Se caiu aqui o arquivo já existe, pega os dados dele, adicona novos e reescreve ele novamente.
        if os.path.exists("historico_consulta.json") == True:

            with open("historico_consulta.json", "r", encoding="utf-8") as arquivo:
                #json.load() - converte o arquivo recebido em arquivo de lista, que pode usar o append.
                #Sendo arquivo de de lista podemos adicionar os dados de dados_historico.
                historico_existente = json.load(arquivo)
            historico_existente.append(dados_historico)

            with open("historico_consulta.json", "w", encoding="utf-8") as arquivo:
                json.dump(historico_existente, arquivo, indent=4, ensure_ascii=False)
        else:   
            historico = []
            historico.append(dados_historico)

            #Se o arquivo não existir ele cria e escreve dentro dele os itens da variável historico
            with open("historico_consulta.json", "w", encoding="utf-8") as arquivo:
                json.dump(historico, arquivo, indent=4, ensure_ascii=False)
    except Exception as err:
        print(f"Erro ao criar ou ler o arquivo, por favor, verifique: {err}")
