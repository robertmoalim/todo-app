import PySimpleGUI as sg
from conversion_function import convert


label1 = sg.Text("Enter feet:")
input_box1 = sg.InputText(tooltip="Enter feets here", key="feet")

label2 = sg.Text("Enter inches:")
input_box2 = sg.InputText(tooltip="Enter inches here", key="inch")

convert_button = sg.Button("Convert")
output_label = sg.Text(key="output", size=(20, 1))

window = sg.Window('Convertor', layout=[[label1, input_box1], [label2, input_box2], [convert_button, output_label]])

while True:
    event, values = window.read()

    # feet_conversion = float(values["feet"])
    # total_feet_conversion = feet_conversion * 0.3048
    #
    # inch_conversion = float(values["inch"])
    # total_inch_conversion = inch_conversion * 0.0254
    #
    # meters = float(total_feet_conversion) + float(total_inch_conversion)
    meters_result = convert(float(values["feet"]), float(values["inch"]))
    window["output"].update(value=f"{meters_result} meters")


window.close()