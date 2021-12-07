from PyPDF2 import PdfFileReader, PdfFileWriter
import sqlite3
from base64 import b64decode



def pdf_rotate(pageNum, degree):
    con = sqlite3.connect('pdf_data.sqlite')
    c = con.cursor()
    c.execute('''
        SELECT * FROM user_data
    ''')
    result = c.fetchall()
    for row in result:
        name = row[1]
        data =  row[2]
        with open('Output_pdfs/rot_'+name, 'wb') as output_file:
            output_file.write(data)
            pdf = open('Output_pdfs/rot_'+name, 'rb')

            open_pdf = PdfFileReader(pdf)
            n = open_pdf.getNumPages()
            writer = PdfFileWriter()
            for i in range(n):
                page = open_pdf.getPage(i)
                if i in pageNum:
                    page.rotateClockwise(degree)
                #
                writer.addPage(page)
                writer.write(output_file)
            output_file.close()




    c.execute('''
        DELETE FROM user_data WHERE id >-1
    ''')
    con.commit()
