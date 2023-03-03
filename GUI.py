import PySimpleGUI as sg
import fm_converter as fmc

label1 = sg.Text('Enter feet: ', background_color='black')
input1 = sg.InputText(tooltip='Enter a digit representing feet', key='feet')

label2= sg.Text('Enter inches: ', background_color='black')
input2 = sg.InputText(tooltip='Enter a digit representing inches', key='inches')

button1 = sg.Button('Convert')
output_label = sg.Text(key='output', background_color='black', text_color='green')

window = sg.Window('Feet to Meters Convertor', background_color='black',
                                               layout=[[label1, input1],
                                                       [label2, input2],
                                                       [button1, output_label]])

while True:
    event, values = window.read()
    print(event, values)
    feet = values['feet']
    inches = values['inches']

    meters = fmc.fmc(feet, inches)
    window['output'].update(value=f'{meters} m')



window.close()