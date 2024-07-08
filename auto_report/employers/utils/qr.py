import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer


def generate_qr(link:str, name:str):
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
    qr.add_data(link)
    img = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())
    img.save(name+".png")
    return name+".png"