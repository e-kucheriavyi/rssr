import base64


class Response:
    img: bytearray = []
    x: int = 0
    y: int = 0

    def __init__(self, img, x=0, y=0):
        self.img = base64.b64encode(img)
        self.x = x
        self.y = y

    def to_dict(self):
        return {
            'img': self.img.decode(),
            'x': self.x,
            'y': self.y,
        }
