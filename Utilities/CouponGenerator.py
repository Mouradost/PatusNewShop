from typing import Union
from lxml import etree
from datetime import datetime
from qrcode import QRCode
from qrcode.image.svg import SvgImage, SvgFragmentImage, SvgPathImage
import os
from DB.DbTables import Coupon

"""
%a: Weekday in the locale’s abbreviated name (e.g., Mon)
%A: Weekday in the locale’s full name (e.g., Monday)
%b: month as locale’s abbreviated name (e.g., Dec)
%B: month as locale’s full name (e.g., December)
%m: month as zero-padded decimal number (e.g., 01)
%d: day as a zero-padded decimal number (e.g., 09)
%y: year without century (e.g., 2021)
%Y: year with century (e.g., 21)
"""


def to_qr_code(
    coupon: Coupon,
    fill_color: str = "#fe9830",
    back_color: str = "#9b0101",
    save: bool = False,
    show: bool = False,
    svg_method: str = None,
    box_size: int = 4,
    border: int = 0,
) -> Union[SvgImage, SvgFragmentImage, SvgPathImage]:

    qr = QRCode(box_size=box_size, border=border)
    # print(coupon)
    # print(coupon.to_qr_code())
    qr.add_data(coupon.to_qr_code())

    # qr.print_ascii()
    factory = None
    if svg_method == "basic":
        # Simple factory, just a set of rects.
        factory = SvgImage
    elif svg_method == "fragment":
        # Fragment factory (also just a set of rects)
        factory = SvgFragmentImage
    elif svg_method == "path":
        # Combined path factory, fixes white space that may occur when zooming
        factory = SvgPathImage

    im = qr.make_image(
        fill_color=fill_color, back_color=back_color, image_factory=factory
    )
    if save:
        if svg_method is not None:
            im.save(os.path.join(os.getcwd(), "Patus-coupon-qrcode.svg"))
        else:
            im.save(os.path.join(os.getcwd(), "Patus-coupon-qrcode.png"))
    if show and factory is None:
        im.show()
    return im


def create_coupon(
    coupon: Coupon = Coupon(
        id=1,
        date_start=datetime.now(),
        date_end=datetime.now(),
        date_creation=datetime.now(),
        amount=4000.0,
    ),
    template: str = os.path.join(
        os.getcwd(), "resource", "Coupon_template", "Coupon-original.svg"
    ),
    file_out: str = os.path.join(os.getcwd(), "tmp", "Coupon-new.svg"),
    side_image: str = "side_image.png",
):
    qr_code = to_qr_code(coupon, svg_method="basic")
    with open(template, "r") as f:
        tree = etree.parse(f)
        for element in tree.iter():
            if element.get("id") == "Price":
                element.text = f"{coupon.amount:,.2f} DA"
            elif element.get("id") == "Validity":
                element.text = f"Valide du {coupon.date_start:%d %b %Y} au {coupon.date_end:%d %b %Y}"
            elif element.get("id") == "Number":
                element.text = f"Number {coupon.id:05}"
            elif element.get("id") == "QRCode":
                element.clear()
                # element.set("class", "cls-88")
                # element.set("transform", "translate(320 1.3) scale(0.25 0.25)")
                element.set("class", "cls-5")
                # element.set("transform", "translate(7 0) scale(0.41 0.41)")
                element.set("transform", "translate(16 3)")
                for child in qr_code._img.getchildren():
                    element.append(child)
            elif element.get("id") == "SidePicture":
                element.clear()
                element.set("id", "SidePicture")
                element.set("height", "50")
                element.set("width", "40")
                element.set("href", side_image)
            elif element.get("id") == "SidePictureOld":
                element.clear()
                element.set("id", "SidePictureOld")
                element.set("height", "50")
                element.set("width", "40")
                element.set("{http://www.w3.org/1999/xlink}href", side_image)

        tree.write(file_out)
    return etree.tostring(tree)


def create_coupon_xml(
    coupon: Coupon = Coupon(
        id=1,
        date_start=datetime.now(),
        date_end=datetime.now(),
        date_creation=datetime.now(),
        amount=4000.0,
    ),
    template: str = os.path.join(
        os.getcwd(), "resource", "Coupon_template", "Coupon-original.svg"
    ),
    side_image: str = "side_image.png",
):
    qr_code = to_qr_code(coupon, svg_method="fragment", box_size=5, border=0)
    with open(template, "r") as f:
        tree = etree.parse(f)
        for element in tree.iter():
            if element.get("id") == "Price":
                element.text = f"{coupon.amount:,.2f} DA"
            elif element.get("id") == "Validity":
                element.text = f"Valide du {coupon.date_start:%d %b %Y} au {coupon.date_end:%d %b %Y}"
            elif element.get("id") == "Number":
                element.text = f"Number {coupon.id:05}"
            elif element.get("id") == "SidePicture":
                element.clear()
                element.set("id", "SidePicture")
                element.set("height", "50")
                element.set("width", "40")
                element.set("{http://www.w3.org/1999/xlink}href", side_image)
            elif element.get("id") == "QRCode":
                transform = element.get("transform")
                element.clear()
                element.set("id", "QRCode")
                element.set("fill", "#FE9830")
                element.set("width", "40")
                element.set("height", "40")
                element.set("transform", transform)
                for child in qr_code._img.getchildren():
                    for key in child.keys():
                        child.set(key, child.get(key).strip("mm"))
                    element.append(child)
    tree.write("Coupon-test.svg")
    return etree.tostring(tree)


def main():
    coupon = Coupon(
        id=55,
        date_start=datetime.now(),
        date_end=datetime.now(),
        date_creation=datetime.now(),
        amount=1000.0,
    )
    create_coupon_xml(coupon, template="./Coupon-tiny.svg")


if __name__ == "__main__":
    main()
