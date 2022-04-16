import Scraper
import io
import requests
from PIL import Image
import tempfile
import PySimpleGUI as sg


def get_all_subs(mode="string"):
    if mode == "string":
        text = ""
        with open("subscriptions.txt") as file:
            for line in file:
                text += line
        return text
    elif mode == "list":
        subs = list()
        with open("subscriptions.txt") as file:
            for line in file:
                subs.append(line)
        return subs
    return ""


def new_videos(mode="text"):
    unsorted = list()
    for url in get_all_subs(mode="list"):
        videos = Scraper.get_newest_videos_from_channel(url)
        for video in videos:
            unsorted.append(video)
    unsorted.sort(key=second)
    if mode == "text":
        titles = [video[0] for video in unsorted]
        text = ""
        for title in titles:
            text += title + "\n"
        return text
    elif mode == "list":
        return unsorted
    else:
        return ""


def second(elem):
    return elem[1]


def get_png_from_url(url):
    buffer = tempfile.SpooledTemporaryFile(max_size=1e9)
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        downloaded = 0
        filesize = int(r.headers['content-length'])
        for chunk in r.iter_content(chunk_size=1024):
            downloaded += len(chunk)
            buffer.write(chunk)
        buffer.seek(0)
        i = Image.open(io.BytesIO(buffer.read()))
    buffer.close()
    png_bio = io.BytesIO()
    i.save(png_bio, format="PNG")
    png_data = png_bio.getvalue()
    return png_data


def generate_Frame_layout_for_vid(vid, nr):
    frame_layout = [
        [sg.Image(get_png_from_url(
            vid[3]), key="thumbnail"+str(nr))],
    ]
    return frame_layout


def generate_frame_for_vid(vid, nr):
    return sg.Frame(vid[0], generate_Frame_layout_for_vid(vid, nr), font='Any 11', title_color='Black', size=(400, 150), key="vid" + str(nr))


if __name__ == "__main__":
    # print(new_videos())
    get_png_from_url("https://i.ytimg.com/vi/sgEn3Omab_Y/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLAXL0VaLI_TCPL25T146oL0gMWSbQ").show()
