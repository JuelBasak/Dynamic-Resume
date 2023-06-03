from flask import Flask, render_template
import pandas as pd
import os
import logging

app = Flask(__name__)


def get_data():
    database_location = os.path.join('database', 'user.xlsx')
    main_dict = {}

    df = pd.read_excel(database_location, sheet_name='ABOUT_ME')
    df_rows, df_cols = df.shape

    table1_dict = {}

    table1_dict['TID'] = df['TID']
    table1_dict['NAME'] = df['NAME']
    table1_dict['HEADING'] = df['HEADING']
    table1_dict['DESCRIPTION'] = df['DESCRIPTION']
    table1_dict['EMAIL'] = df['EMAIL']
    table1_dict['LINKEDIN'] = df['LINKEDIN']
    table1_dict['GIT'] = df['GIT']
    table1_dict['KAGGLE'] = df['KAGGLE']

    main_dict['table1_dict'] = table1_dict

    table2_dict = {}

    df = pd.read_excel(database_location, sheet_name='EDUCATION')
    table2_dict['TID'] = df['TID']
    table2_dict['DEGREE'] = df['DEGREE']
    table2_dict['UNIVERSITY'] = df['UNIVERSITY']
    table2_dict['LOCATION'] = df['LOCATION']
    table2_dict['SCORE'] = df['SCORE']
    table2_dict['START_DATE'] = df['START_DATE']
    table2_dict['END_DATE'] = df['END_DATE']
    table2_dict['DURATION'] = df['DURATION']

    main_dict['table2_dict'] = table2_dict

    table3_dict = {}
    l = []

    df = pd.read_excel(database_location, sheet_name='EDUCATION')
    df_rows, df_cols = df.shape

    for i in range(df_rows):
        data_dict = df.iloc[i].to_dict()
        l.append(data_dict)

    pass

    l = []

    for i in conn.execute('SELECT * FROM SKILLS;'):
        l.append(i[1])

    main_dict['table4_dict'] = l

    l = []

    for i in conn.execute('SELECT * FROM INTEREST;'):
        l.append(i[1])

    main_dict['table5_dict'] = l

    l = []

    for i in conn.execute('SELECT * FROM PROFESSION;'):
        l.append(i[1])

    main_dict['table6_dict'] = l

    l = []

    for i in conn.execute('SELECT * FROM CERTIFICATES ORDER BY "tid" DESC;'):
        temp_dict = {}
        temp_dict['tid'] = i[0]
        temp_dict['certificate_name'] = i[1]
        temp_dict['issuer'] = i[2]
        temp_dict['location'] = i[3]
        temp_dict['certificate_link'] = i[4]
        temp_dict['start_date'] = i[5]
        temp_dict['end_date'] = i[6]
        temp_dict['duration'] = i[7]
        temp_dict['details'] = i[8]

        l.append(temp_dict)

    main_dict['table7_dict'] = l

    l = []

    for i in conn.execute('SELECT * FROM PROJECTS'):
        temp_dict = {}
        temp_dict['tid'] = i[0]
        temp_dict['project_name'] = i[1]
        temp_dict['project_git_link'] = i[2]
        temp_dict['project_deployment_link'] = i[3]
        temp_dict['start_date'] = i[4]
        temp_dict['end_date'] = i[5]
        temp_dict['duration'] = i[6]
        temp_dict['details'] = i[7]
        temp_dict['youtube_link'] = i[8]

        l.append(temp_dict)

    main_dict['table8_dict'] = l

    return main_dict


@app.route('/', methods=['GET', 'POST'])
def main():
    print('Homepage Function')
    main_dict = get_data()
    return render_template('index.html', main_dict=main_dict)


print('Starting the Flask Application')
if __name__ == '__main__':
    app.run(debug=True)

print('Ending the Flask Application')
