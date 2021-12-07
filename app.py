from main import *
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import sqlite3

app = Flask(__name__, template_folder="./template")

#
# creating a database to store pdf
# con = sqlite3.connect('pdf_data.sqlite')
# c = con.cursor()
# c.execute('''CREATE TABLE user_data (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     title TEXT,
#     pdf BLOB
# )
# ''')
# con.commit()
# con.close()


def index_page(p_num):
    return int(p_num) -1
def insert_user_data(title, pdf):
    con = sqlite3.connect("pdf_data.sqlite")
    cur = con.cursor()
    query = """
        INSERT INTO user_data (title, pdf) VALUES (?, ?);
    """
    cur.execute(query, [title, pdf])
    con.commit()


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        # Getting PDF and it's name to upload in the database
        pdf = request.files['pdf'].read()
        file_name = request.files['pdf'].filename

        # Getting the selected pages to rotate from user
        page_num = request.form['pages'].strip()


        page_num = page_num.split(',')          # split method creates an array of single element containing empty string
        # for i in range(len(page_num)):
        #     if page_num[0] == '' or not page_num[i].isnumeric():
        #         return render_template('index.html', warning = 'Please enter valid page no.')

        page_arr = list(map(index_page, page_num))
        print(page_arr)
        degree = request.form.get('angle')
        insert_user_data(file_name, pdf)
        pdf_rotate(page_arr, int(degree))
        # except:
        #     print('--------Error---------')




    return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
