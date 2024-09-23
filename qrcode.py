import pyqrcode
from PIL import Image

link = input("Enter anything: ")

qr_code = pyqrcode.create(link)

qr_code.png("QRCode.png", scale=5)

image = Image.open("QRCode.png")
image.show()
