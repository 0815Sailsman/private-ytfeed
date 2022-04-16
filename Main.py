import PySimpleGUI as sg
from tools import get_all_subs, new_videos, get_png_from_url, generate_frame_for_vid


# Get newest videos
videos = new_videos(mode="list")

# Define the window's contents
subs = [
    [sg.Text("Current subscriptions:")],
    [sg.Multiline(get_all_subs(), size=(50, 5), key='subs-box'),
     sg.Button("Save subs", key="save-subs"),
     sg.Button("Reload vids", key="reload-vids")]
]

vids = [[generate_frame_for_vid(videos[0], 0), generate_frame_for_vid(videos[1], 1), generate_frame_for_vid(videos[2], 2)],
        [generate_frame_for_vid(videos[3], 3), generate_frame_for_vid(videos[4], 4), generate_frame_for_vid(videos[5], 5)],
        [generate_frame_for_vid(videos[6], 6), generate_frame_for_vid(videos[7], 7), generate_frame_for_vid(videos[8], 8)]]

layout = [[subs, sg.VerticalSeparator(),
           vids
           #sg.Button('', image_data=get_png_from_url("https://i.ytimg.com/vi/sgEn3Omab_Y/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLAXL0VaLI_TCPL25T146oL0gMWSbQ"), key=("thumbnail"+str(0)))
           ]]

# Create the window
window = sg.Window('Window Title', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    elif event == "save-subs":
        text = str(window["subs-box"].get())
        print(text)
        with open("subscriptions.txt", "w") as file:
            file.write(text)
    elif event == "reload-vids":
        videos = new_videos(mode="list")
        for i in range(9):
            window["vid"+str(i)].update(videos[i][0])
            window["thumbnail"+str(i)].update(image_data=get_png_from_url(videos[i][3]))

# Finish up by removing from the screen
window.close()
