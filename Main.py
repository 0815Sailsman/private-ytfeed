import PySimpleGUI as sg
from tools import get_all_subs


# Define the window's contents
layout = [[sg.Text("Current subscriptions:")],
          [sg.Multiline(get_all_subs(), size=(40,10), key='textbox', disabled=True)],
          [sg.Button('Quit')]]

# Create the window
window = sg.Window('Window Title', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    print(event)
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

# Finish up by removing from the screen
window.close()
