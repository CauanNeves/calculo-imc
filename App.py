import PySimpleGUI as sg

#tema
sg.theme('BrownBlue')
#layout
top_row= ['IMC', 'Classificações']
rows= [
    ['< 17', 'Muito Abaixo do Peso'],
    ['17 - 18,5', 'Abaixo do Peso'],
    ['18,5 - 24,9', 'Peso Normal'],
    ['25 - 29,9', 'Acima do peso'],
    ['30 - 34,9', 'Obesidade I '],
    ['35 - 39,9', 'Obesidade II (severa)'],
    ['> 40', 'Obesidade III (mórbida)']
]


frame_calc= [
    [sg.Text('Altura (m): '), sg.Input(key='altura', size=(5, 1)), 
     sg.Text('Peso (kg): '), sg.Input(key='peso', size=(5, 1)), 
     sg.Button('Calcular', key='btn_calc')],

    [sg.Text(key='result', expand_x=True, justification='center')]
]

main_layout = [
    [sg.Table(values=rows, headings=top_row, justification='center', 
              hide_vertical_scroll=True, expand_x=True, num_rows=7, row_height=25)],
    [sg.Frame('Calcular IMC', frame_calc)]

]

#Janela
window= sg.Window('Calculadora de IMC', layout= main_layout, element_justification='c')
#leitura de eventos e valores
while True:
    event, values = window.read()
    #ler e reagir
    if event == sg.WIN_CLOSED:
        break
    elif event == 'btn_calc':
        try:
            window['result'].update('')
            altura = float(values['altura'].replace(',', '.'))
            peso = float(values['peso'].replace(',', '.'))
            imc = peso / (altura ** 2)

            imc_ranges = [
                (0, 17, 'medium slate blue'),
                (17, 18.5, 'light slate blue'),
                (18.5, 25, 'forest green'),
                (25, 30, 'yellow', 'blue'),
                (30, 35, 'orange'),
                (35, 40, 'orange red'),
                (40, float('inf'), 'red')
            ]
            imc_class = ''
            for min_imc, max_imc, text_color, *bg_color in imc_ranges:
                if min_imc <= imc < max_imc:
                    imc_class = rows[imc_ranges.index((min_imc, max_imc, text_color, *bg_color))][1]
                    window['result'].update(f'Seu IMC é {imc:,.2f} ({imc_class})', text_color=text_color, background_color=bg_color[0] if bg_color else 'white')
                    break
            
        except ValueError:
            window['result'].update('Os campos acima não podem ser vazios', text_color= 'red')