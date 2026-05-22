import requests
import json
import os
from datetime import datetime
from historico import salvar_historico
from dotenv import load_dotenv
from notificacao import enviar_webhook
from datetime import timezone, timedelta




#Trás a KEY de outro arquivo, aonde ela está oculta.
load_dotenv()
API_KEY = os.getenv("API_KEY")


def get_api():

    while True:
        try:
            print("\n")
            print("O que você quer fazer?")
            print("1 - Pesquisar cidade | 2 - Ver histórico de pesquisa | 3 - Sair do programa")
            resposta = int(input("Responda aqui: "))
        except ValueError:
            print("\nDigite aprenas números!")
            continue

        if resposta == 1:
            cidade = input("Digite uma cidade para consultar: ").strip()
            url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&units=metric&lang=pt_br"

            try:
                response = requests.get(url)
                if response.status_code == 404:
                    raise ValueError(f"Erro ao buscar cidade. Verifique se o nome está correto.")
                

                dados = response.json()

                #LÓGICA PEGA HORÁRIO LOCAL DA CIDADE---------------------------------------------------
                #EX: Londres: 3600 (1 hora), informação vem da API
                offset_fuso_horario = dados["timezone"]
                #O timedelta converte os segundos em um objeto de duração de tempo,
                #Depois é criado um objeto de fuso horário com esse offset. EX: fuso UTC +1
                fuso_cidade = timezone(timedelta(seconds=offset_fuso_horario))
                #Pega o horário atual já convertido para o fuso da cidade
                horario_cidade = datetime.now(tz=fuso_cidade)
                #Formata a data no padrão brasileiro
                horario_formatado = horario_cidade.strftime("%d/%m/%Y %H:%M")
                #--------------------------------------------------------------------------------------


                nome_cidade = dados["name"]
                temperatura_atual = dados["main"]["temp"]
                sensacao_terminca = dados["main"]["feels_like"]
                # temp_max = dados["main"]["temp_max"]
                # temp_min = dados["main"]["temp_min"]
                umidade = dados["main"]["humidity"]
                descricao_tempo = dados["weather"][0]["description"]
                longitude = dados["coord"]["lon"]
                latitude = dados["coord"]["lat"]
                visibilidade = dados["visibility"]
                visibilidade_formatada = str(visibilidade)[:2]
                
                print("\n")
                print(f"A previsão do tempo para {nome_cidade} é:")
                print(f"temperatura atual de {temperatura_atual:.1f}".replace(".",",") + f"°C, com sensação térmica de {sensacao_terminca:.1f}".replace(".",",") + "°C")
                # print(f"a temperatura mínima pode chegar à {temp_min:.1f}".replace(".",",") + f"°C, e a máxima até {temp_max:.1f}".replace(".",",") + "°C")
                print(f"a visibilidade é de {visibilidade_formatada}km, temos {descricao_tempo}, e umidade de {umidade}%")
                print(f"as coordenadas são: lon:{longitude} ; lat:{latitude}")
                print(f"Data e hora da local: {horario_formatado}")

                salvar_historico(nome_cidade, temperatura_atual, sensacao_terminca, descricao_tempo, umidade, horario_formatado, longitude, latitude)

                enviar_webhook({
                    "cidade": nome_cidade,
                    "temperatura": temperatura_atual,
                    "sensacao_termica": sensacao_terminca,
                    "descricao": descricao_tempo,
                    "umidade": umidade,
                    "data_hora": horario_formatado,
                    "coordenadas": {"lon": longitude, "lat": latitude},            
                })
            except Exception as err:
                print("\n")
                print(f"Erro na busca da API: {err}")
        elif resposta == 2:
            try:
                #Se caiu aqui o arquivo já existe
                if os.path.exists("historico_consulta.json") == True:
                    with open("historico_consulta.json", "r", encoding="utf-8") as arquivo:
                        #json.load() - converte o arquivo recebido em arquivo de lista.
                        historico_existente = json.load(arquivo)
                        
                        #historico percorre cada item da lista e imprime
                        for historico in historico_existente:
                            print("\n")
                            for chave, valor in historico.items():
                                print(f"{chave}: {valor}")                            
                else:
                    print("\n") 
                    print("Não tem histórico ainda, faça uma pesquisa primeiro!")
            except Exception as err:
                print("\n")
                print(f"Erro ao consultar histórico, verifique: {err}")
        elif resposta == 3:
            print("\n")
            print("VOCÊ SAIU DO PROGRAMA!")
            break
        else:
            print("\n")
            print("OPÇÃO INVÁLIDA, POR FAVOR VERIFIQUE!")
        


get_api()


