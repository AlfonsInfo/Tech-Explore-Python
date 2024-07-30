import base64
from PyPDF2 import PdfWriter, PdfReader, PaperSize, Transformation, PageObject
from PyPDF2.generic import RectangleObject, NameObject, NumberObject
import pdfkit
import qrcode
from qrcode import QRCode

from PIL import Image
from io import BytesIO

def do_stamp(file_input_base64, signature_base64, output_image_path):
    """
    :param file_input_base64: Base64 encoded input PDF file
    :param signature_base64: Base64 encoded signature image
    :param output_image_path: Path to save the temporary image of the stamp
    :return: Base64 encoded output PDF file
    """
    try:
        # Decode the input file
        file_bytes = base64.b64decode(file_input_base64)
        file_input = BytesIO(file_bytes)

        # Open the PDF file from binary data
        existing_pdf = PdfReader(file_input, strict=False)
        box = existing_pdf.pages[0].mediabox

        # Decode the signature image
        signature_bytes = base64.b64decode(signature_base64)
        tempImage = Image.open(BytesIO(signature_bytes))
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

        # Generate HTML for the QR PDF
        if existing_pdf.pages[0].get('/Rotate') == 90:
            htmls = f"<html><body style=\"width: {w};\"><div style=\"overflow:hidden;position: absolute;bottom:0;right:0;\"><img src=\"data:image/jpeg;base64,{base64s}\" style=\" width:{w}\"></img></div></body></html>"
        else:
            htmls = f"<html><body style=\"width: {w}\"><div style=\"overflow:hidden;position: absolute;bottom:0;\"><img src=\"data:image/jpeg;base64,{base64s}\" style=\"width:{w};\"></img></div></body></html>"

        path_wkhtmltopdf = "C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe"
        pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
        pdfkit.from_string(htmls, output_image_path)

        stamp = PdfReader(open(output_image_path, "rb"))

        outputs = PdfWriter()
        # Merge pages
        count = existing_pdf.numPages
        for i in range(count):
            page = existing_pdf.pages[i]
            if i == 0:
                if existing_pdf.pages[0].get('/Rotate') == 90:
                    # Stamp for landscape
                    h = float(page.mediabox.height)
                    w = float(page.mediabox.width)
                    s = stamp.pages[0]

                    transform = Transformation().scale(0.9, 0.9).translate(300, 0)
                    s.add_transformation(transform)

                    s.cropbox = RectangleObject((0, 0, s.mediabox.height, s.mediabox.width))
                    page_A4 = PageObject.create_blank_page(width=w, height=h)
                    s.mediabox = page_A4.mediabox
                    page_A4.merge_page(s)

                    page.merge_page(page_A4)
                    outputs.add_page(page)
                else:
                    # Stamp for portrait
                    page.merge_page(stamp.pages[0])
                    outputs.add_page(page)
            else:
                outputs.add_page(page)

        output_buffer = BytesIO()
        outputs.write(output_buffer)
        output_buffer.seek(0)
        output_base64 = base64.b64encode(output_buffer.getvalue()).decode('utf-8')

        return output_base64

    except Exception as e:
        print(f"An error occurred: {e}")
        raise

def generate_base64_qr(data):
    try:
        qr = qrcode.main.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        # Buat gambar QR code
        img = qr.make_image(fill_color="black", back_color="white")

        # Simpan gambar ke dalam buffer
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        # Konversi gambar ke base64
        img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    except Exception as e:
        print(e)
        raise
    return img_str



# Anyflow 1.0
def do_stamp_anyflow1(file_input, signature, output_image_path):
    """
    :param file_input: Lokasi file PDF asli.
    :param signature:  Lokasi gambar yang akan dijadikan stempel.
    :param output_image_path: Lokasi penyimpanan file gambar sementara yang digunakan dalam proses pembuatan stempel.
    """
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

        path_wkhtmltopdf = "C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe"
        pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
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
        # # save
        # output_stream = open(output, "wb")
        # outputs.write(output_stream)
        # output_stream.close()

    except Exception as e:
        print(e)
        raise
