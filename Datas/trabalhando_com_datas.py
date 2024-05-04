from datetime import datetime

data_hora_atual = datetime.now()
mascara = "%d/%m/%Y %a"

print(data_hora_atual.strftime(mascara))