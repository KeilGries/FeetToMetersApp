import PySimpleGUI as sg
from fm_converter import fmc

sg.theme('Black')

label1 = sg.Text('Enter feet: ')
input1 = sg.InputText(tooltip='Enter a digit representing feet', key='feet',
                      size=20)

label2= sg.Text('Enter inches: ')
input2 = sg.InputText(tooltip='Enter a digit representing inches', key='inches',
                      size=18)

button1 = sg.Button('Convert')
button2 = sg.Button('Exit')
output_label = sg.Text(key='output', text_color='green')

window = sg.Window('Feet to Meters Convertor', font='Helvetica',
                                               layout=[[label1, input1],
                                                       [label2, input2],
                                                       [button1, button2, output_label]])

while True:
    event, values = window.read(timeout=200)
    match event:
        case 'Exit':
            break
        case 'Convert':
            try:
                feet = values['feet']
                inches = values['inches']
                meters = fmc(feet, inches)
                window['output'].update(value=f'{meters} m')
            except ValueError:
                sg.popup('Please enter values for feet/inches using digits.',
                         font='Helvetica')

window.close()

