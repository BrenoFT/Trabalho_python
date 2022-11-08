print("Para encerrar a operação digite -1 no campo hora!!")

x = 0
while(x < 1):
    hora = int(input("Digite a hora: "))
    if hora == -1:
        break
    minuto = int(input("Digite os minutos: "))

    def converter_hora(hora):
        return (hora - 12)

    def exibir_hora(hora,minuto):
        if(hora <= 12):
            print(f"{hora}:{minuto} AM")
        if(hora > 12):
            print(f"{converter_hora(hora)}:{minuto} PM")
    if(hora > 24):
        print("Horário impossível de ser convertido.")
        break
    exibir_hora(hora, minuto)