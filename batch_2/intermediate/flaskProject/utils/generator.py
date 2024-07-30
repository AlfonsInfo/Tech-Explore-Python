import base64
from PyPDF2 import PdfWriter, PdfReader, PaperSize, Transformation, PageObject
from PyPDF2.generic import RectangleObject, NameObject, NumberObject
import pdfkit

import sys

from PIL import Image
from io import BytesIO


def doStamp(file_input, signature, output, output_image_path):
    try:
        # open file pdf
        existing_pdf = PdfReader(open(file_input, "rb"), strict=False)
        box = existing_pdf.pages[0].mediaBox

        tempImage = Image.open(signature);
        if existing_pdf.pages[0].get('/Rotate') == 90:
            h = box.getWidth()
            w = box.getHeight() * 3 / 4
            sign = tempImage.rotate(90, expand=1)
        else:
            h = box.getWidth()
            w = box.getHeight() * 3 / 4
            sign = tempImage

        buff = BytesIO()
        sign.save(buff, format="PNG")

        base64s = base64.b64encode(buff.getvalue()).decode("utf-8")
        # generate qr pdf
        if existing_pdf.pages[0].get('/Rotate') == 90:
            htmls = f"<html><body style=\"width: " + str(
                w) + ";\"><div style=\"overflow:hidden;position: absolute;bottom:0;right:0;\"><img src=\"data:image/jpeg;base64," + str(
                base64s) + " style=\" width:" + str(w) + " \"></img></div></body></html>"
        else:
            htmls = f"<html><body style=\"width: " + str(
                w) + "\"><div style=\"overflow:hidden;position: absolute;bottom:0;\" ><img src=\"data:image/jpeg;base64," + str(
                base64s) + "\" style=\"width:" + str(w) + ";\"></img></div></body></html>"

        pdfkit.configuration(wkhtmltopdf="/usr/local/bin/wkhtmltopdf")

        pdfkit.from_string(htmls, output_image_path)

        stamp = PdfReader(open(output_image_path, "rb"))

        outputs = PdfWriter()
        # merge
        count = existing_pdf.numPages
        for i in range(count):

            page = existing_pdf.getPage(i)
            if i == 0:
                if existing_pdf.pages[0].get('/Rotate') == 90:
                    #    stamp for landscape
                    h = float(page.mediabox.height)
                    w = float(page.mediabox.width)
                    s = stamp.pages[0]

                    transform = Transformation().scale(0.9, 0.9).translate(300, 0)
                    s.add_transformation(transform)

                    s.cropbox = RectangleObject((0, 0, s.mediaBox.height, s.mediaBox.width))
                    page_A4 = PageObject.create_blank_page(width=w, height=h)
                    s.mediabox = page_A4.mediabox
                    page_A4.merge_page(s)

                    page.merge_page(page_A4)
                    outputs.add_page(page)
                else:
                    # stamp for potrait
                    page.merge_page(stamp.pages[0])
                    outputs.add_page(page)

            else:
                outputs.add_page(page)
        # save
        output_stream = open(output, "wb")
        outputs.write(output_stream)
        output_stream.close()

    except:
        pass