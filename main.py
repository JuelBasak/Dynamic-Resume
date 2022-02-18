from flask import Flask, render_template
import webbrowser
from threading import Timer
import sqlite3

app = Flask(__name__)

def get_data():
    conn = sqlite3.connect('database/user.db')
    main_dict = {}
    table1_dict = {}

    for i in conn.execute('SELECT * FROM ABOUT_ME'):
        table1_dict['tid'] = i[0]
        table1_dict['name'] = i[1]
        table1_dict['heading'] = i[2]
        table1_dict['description'] = i[3]
        table1_dict['email'] = i[4]
        table1_dict['linkedin'] = i[5]
        table1_dict['git'] = i[6]
        table1_dict['kaggle'] = i[7]
        
    main_dict['table1_dict'] = table1_dict

    table2_dict = {}

    for i in conn.execute('SELECT * FROM EDUCATION ORDER BY "tid" DESC;'):
        table2_dict['tid'] = i[0]
        table2_dict['degree'] = i[1]
        table2_dict['university'] = i[2]
        table2_dict['location'] = i[3]
        table2_dict['score'] = i[4]
        table2_dict['start_date'] = i[5]
        table2_dict['end_date'] = i[6]
        table2_dict['duration'] = i[7]

    main_dict['table2_dict'] = table2_dict

    table3_dict = {}
    l = []

    for i in conn.execute('SELECT * FROM EXPERIENCE ORDER BY "tid" DESC;'):
        temp_dict = {}
        temp_dict['tid'] = i[0]
        temp_dict['designation'] = i[1]
        temp_dict['company'] = i[2]
        temp_dict['location'] = i[3]
        temp_dict['start_date'] = i[4]
        temp_dict['end_date'] = i[5]
        temp_dict['duration'] = i[6]
        temp_dict['details'] = i[7]

        l.append(temp_dict)

    main_dict['table3_dict'] = l

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


@app.route('/', methods=['GET'])
def homepage():
    try:
        main_dict = get_data()
    except:
        return 'Database Problem'
    else:    
        return render_template('index.html', main_dict = main_dict)


if __name__ == '__main__':
    app.run()

