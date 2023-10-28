import requests

class Clicker:
    def __init__(self, platform):
        self.platform = platform
    def game(platform):
        if platform == "gamejolt":
            gj = requests.get("http://source.pythonanywhere.com/platform/gamejolt")
            print(gj.text)
        elif platform == "itch":
            iio = requests.get("http://source.pythonanywhere.com/platform/itch")
            print(iio.text)
        elif platform == "classic":
            c = requests.get("http://source.pythonanywhere.com/platform/classic")
            print(c.text)