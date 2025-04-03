import PySimpleGUI as sg

#tema
sg.theme('BrownBlue')

#layout
#Cabeçalho tabela 
top_row= ['IMC', 'Classificações']
#Linhas tabela
rows= [
    ['< 17', 'Muito Abaixo do Peso'],
    ['17 - 18,5', 'Abaixo do Peso'],
    ['18,5 - 24,9', 'Peso Normal'],
    ['25 - 29,9', 'Acima do Peso'],
    ['30 - 34,9', 'Obesidade I '],
    ['35 - 39,9', 'Obesidade II (severa)'],
    ['> 40', 'Obesidade III (mórbida)']
]

#Separando a aba IMC
frame_calc= [
    [sg.Text('Altura (m): '), sg.Input(key='height', size=(5, 1)), 
     sg.Text('Peso (kg): '), sg.Input(key='weight', size=(5, 1)), 
     sg.Button('Calcular', key='btn_calc_imc')],

    [sg.Text(key='result', expand_x=True, justification= 'c', expand_y= True)]
]

#tabela
tab_imc = [
    [sg.Table(values=rows, headings=top_row, justification='center', 
              hide_vertical_scroll=True, expand_x=True, num_rows=7, row_height=25)],
    [sg.Frame('Calcular IMC', frame_calc, expand_x= True, element_justification= 'c', expand_y= True)]

]

#Taxa Basal
frame_result_tb= [
    [sg.Text('', key= 'txt_result_tb'), sg.Text('', key= 'result_tb')],
    [sg.Text('O ideal, para calcular o peso, é que seja em jejum logo pela manhã. Calcule todos os dias durante uma semana e depois tire uma média.',
              size=(45, None))
     ],
    [sg.Text('A taxa metabólica basal, conhecida também como gasto energético basal, é a quantidade de energia que o corpo, em repouso, gasta para manter as suas funções vitais, como respiração, batimentos do coração e manutenção da temperatura corporal.',
             size= (45, None))]
]

tab_txbasal= [
    [sg.Text('Selecione o seu gênero:')],
    [sg.Radio('Homem', group_id= 'sexo', key= 'radio_male', default= True), sg.Radio('Mulher', group_id= 'sexo', key= 'radio_female')],
    [sg.Text('Altura (m):'), sg.Input(key='height_tb', size=(5, 1)), 
     sg.Text('Peso (kg):'), sg.Input(key='weight_tb', size=(5, 1)),
     sg.Text('Idade:'), sg.Input(key= 'age_tb', size= (5, 1))
     ],
    [sg.Button('Calcular', key= 'btn_calc_tb', expand_x= True)],
    [sg.Frame('Resultado', frame_result_tb, expand_x= True, expand_y= True)]
]

#Layout Principal
main_layout= [
    [sg.TabGroup([
        #Uma lista para cada tab
        [sg.Tab('IMC', tab_imc)],
        [sg.Tab('Taxa Basal', tab_txbasal)]
    ])]
]

#Janela
window= sg.Window('Calculadora de IMC', layout= main_layout, element_justification='c')
#leitura de eventos e valores
while True:
    event, values = window.read()
    #ler e reagir
    if event == sg.WIN_CLOSED:
        break
    elif event == 'btn_calc_imc':
        try:
            window['result'].update('')
            height = float(values['height'].replace(',', '.'))
            weight = float(values['weight'].replace(',', '.'))
            imc = weight / (height ** 2)

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
            window['result'].update('Os campos acima estão incorretos.\n Não podem ser vazios e não pode conter letras.', text_color= 'red')
            
    elif event == 'btn_calc_tb':
        try:
            height = float(values['height_tb'].replace(',', '.')) * 100
            weight = float(values['weight_tb'].replace(',', '.'))
            age= float(values['age_tb'].replace(',', '.'))
            
            if values['radio_male'] == True:
                tmb_male= 66 + (13.7 * weight) + (5 * height) - (6.8 * age)
                window['txt_result_tb'].update('Este é o seu gasto calórico basal: ')
                window['result_tb'].update(f'{tmb_male:,.2f}', text_color= 'green', background_color= 'white')
            else:
                tmb_female = 655 + (9.6 * weight) + (1.8 * height) - (4.7 * age)
                window['result_tb'].update(f'{tmb_female:,.2f}', text_color= 'green', background_color= 'white')
        except:
            sg.popup('Os campos não podem ser vazios')