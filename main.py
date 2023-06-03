from flask import Flask, render_template
import pandas as pd
import os

DATABASE_DIR = 'database'
DATABASE_NAME = 'user.xlsx'

app = Flask(__name__)

def get_sheet_name(database_location):
    df = pd.ExcelFile(database_location)
    return df.sheet_names

def get_data_helper(database_location, sheet_name):
    df = pd.read_excel(database_location, sheet_name=sheet_name)
    df_rows, df_cols = df.shape

    l = []

    for i in range(df_rows):
        data_dict = df.iloc[i].to_dict()
        l.append(data_dict)

    return l

def get_data(database_dir, database_name):
    database_location = os.path.join(database_dir, database_name)
    sheet_names = get_sheet_name(database_location)

    main_dict = {}
    for sheet_name in sheet_names:
        main_dict[sheet_name] = get_data_helper(database_location=database_location, sheet_name=sheet_name)
    return main_dict

@app.route('/', methods=['GET', 'POST'])
def main():
    main_dict = get_data(DATABASE_DIR, DATABASE_NAME)
    return render_template('index.html', main_dict=main_dict)


print('Starting the Flask Application')
if __name__ == '__main__':
    app.run(debug=True)

print('Ending the Flask Application')
