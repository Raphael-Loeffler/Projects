from qrcode import QRCode
from qrcode.constants import ERROR_CORRECT_L
from qrcode.image.base import BaseImage

from pyzbar.pyzbar import decode, Decoded

from PIL import Image
from PIL.PngImagePlugin import PngImageFile


class QR_Code_RW:
  def __init__(self):
    pass
  
  def decode_qr_code(image_path) -> str:
    img: PngImageFile = Image.open(image_path)
    url_decoded: Decoded = decode(img)
    url: str = url_decoded[0].data.decode('utf-8')
    return url
  
  def encode_qr_code(text: str, image_name: str) -> None:
    qr: QRCode = QRCode(
      version=None,
      error_correction=ERROR_CORRECT_L,
      box_size=10,
      border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(image_name)
  
  def run(self) -> None:
    print("What would you like to do?")
    print("\t1. Create QR Code")
    print("\t2. Read QR Code")
    user_input: int = int(input("Option: "))
    match user_input:
      case 1:
        url: str = input("url: ")
        image_name: str = input("File name to save the QR code: ") + '.png'
        self.encode_qr_code(text=url, image_name=image_name)
      case 2: 
        image_path: str = input("Please provide the path to the files: ")
        self.decode_qr_code(image_path=image_path)
      case _: ...

if __name__ == "__main__":
  qr_manager = QR_Code_RW
  qr_manager.decode_qr_code()