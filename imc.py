import PySimpleGUI as sg

def calcular_imc(peso, altura):
    return round(peso / (altura ** 2), 2)

layout = [
    [sg.Text("Peso (kg):"), sg.Input(key='peso')],
    [sg.Text("Altura (m):"), sg.Input(key='altura')],
    [sg.Button("Calcular IMC")],
    [sg.Text("", size=(80,1), key='resultado')]
]

janela = sg.Window("Calculadora de IMC", layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WINDOW_CLOSED:
        break
    if evento == "Calcular IMC":
        try:
            peso = float(valores['peso'])
            altura = float(valores['altura'])
            imc = calcular_imc(peso, altura)

            if imc < 18.5:
                status = "Cuidado, você está abaixo do seu peso ideal"
            elif 18.5 <= imc <= 24.9:
                status = "Você está no peso ideal"
            elif 25 <= imc <= 29.9:
                status = "Cuidado, você está com sobrepeso"
            elif 30 <= imc <= 34.9:
                status = "Cuidado, você está com obesidade grau I"
            elif 35 <= imc <= 39.9:
                status = "Cuidado, você está com obesidade grau II"
            else:
                status = "Você está com obesidade mórbida, procure um nutricionista e cuide da sua saúde."

            janela['resultado'].update(f"IMC: {imc} - {status}")
        except:
            janela['resultado'].update("Digite valores válidos.")
janela.close()