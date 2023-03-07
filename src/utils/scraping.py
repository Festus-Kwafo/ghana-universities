import json
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import mysql.connector
from logs import log


def get_all_uni():
    log.info("Data Scraping Started Successfully")
    data = []
    try:
        url = f"https://www.4icu.org/gh/a-z/"
        page = urlopen(url)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, 'html.parser')
        line = list(soup.find_all('table'))


        for element in line:
            rows = soup.findAll('tr')
            rows = rows[2:]
            for x in range(len(rows)):
                uni_dict = {}
                school = rows[x]
                names = list(school.findAll('td'))
                link = list(school.findAll('a'))
                schoolName = names[1].get_text()
                ranking = names[0].get_text()
                reviewlink = link[0]['href']
                uni_dict.update({"name": schoolName})
                uni_dict.update({"ranking": ranking})
                uniID = re.findall(r'\d+', reviewlink)
                if len(uniID) > 0:
                    review = f"https://www.4icu.org/reviews/{uniID[0]}.htm"
                    uniRankId = uniID[0]
                    uni_dict.update({'uniRankId': uniRankId})
                    page = urlopen(review)
                    html = page.read().decode("utf-8")
                    soup = BeautifulSoup(html, 'html.parser')
                    rws = list(soup.find_all("div", {"class": "col-md-3 col-lg-2"}))
                    website = rws[0].findAll('a')
                    websitelink = website[0]['href']
                    uni_dict.update({'website': websitelink})
                    imgtag = list(rws[0].findAll('img'))
                    imgsrclink = imgtag[0]['src']
                    uni_dict.update({'logo': "https://www.4icu.org"+imgsrclink})
                    rwq = list(soup.find_all("div", {"class": "col-md-7 col-lg-8"}))
                    description = rwq[0].find('p').get_text()
                    uni_dict.update({"description": description})

                    # University Identity
                    res = list(soup.find_all('tbody')[0].findAll('td'))
                    try:
                        nickname = res[1].get_text()
                        uni_dict.update({'acronym': nickname})
                    except:
                        uni_dict.update({'acronym': ''})
                    try:
                        founded = res[2].get_text()
                        uni_dict.update({'founded': founded})
                    except:
                        uni_dict.update({'founded': ''})
                    try:
                        motto = res[3].get_text()
                        uni_dict.update({'motto': motto})
                    except:
                        uni_dict.update({'motto': ''})
                    try:
                        colors = res[4].get_text()
                        uni_dict.update({'colors': colors})
                    except:
                        uni_dict.update({'colors': ''})

                    feg = list(soup.find_all('div', 'col-md-5 col-lg-4')[1].findAll('td'))
                    address = feg[0].get_text()
                    tel = feg[1].get_text()
                    fax = feg[2].get_text()
                    uni_dict.update({'address': address})
                    uni_dict.update({'tel': tel})
                    uni_dict.update({'fax': fax})
                    data.append(uni_dict)
        with open('data.json', 'w') as f:
            json.dump(data, f)
    except Exception as e:
        log.error("Error in Scraping Data", extra={"error": e})
    return data


def store_in_db():
    with open('data.json', 'r') as f:
        data = json.load(f)
    # Connect to the database
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="uni_data"
    )
    cursor = db.cursor()
    # Create a table
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS universities_data (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), ranking VARCHAR(255), website VARCHAR(255), logo VARCHAR(255), description TEXT, acronym VARCHAR(255), founded VARCHAR(255), motto VARCHAR(255), colors VARCHAR(255), address VARCHAR(255), tel VARCHAR(255), fax VARCHAR(255))")
    for i in range(len(data)):
        name = data[i].get('name')
        ranking = data[i].get('ranking')
        website = data[i].get('website')
        logo = data[i].get('logo')
        description = data[i].get('description')
        acronym = data[i].get('acronym')
        founded = data[i].get('founded')
        motto = data[i].get('motto')
        colors = data[i].get('colors')
        address = data[i].get('address')
        tel = data[i].get('tel')
        fax = data[i].get('fax')
        sql_select = "SELECT * FROM universities_data WHERE name = %s AND logo = %s;"
        val_select = (name, logo)
        cursor.execute(sql_select, val_select)
        result = cursor.fetchone()
        if result:
            sql_update = "UPDATE universities_data SET ranking = %s, website = %s, logo = %s,description = %s,acronym = %s,founded = %s,motto = %s,colors = %s,address = %s,tel = %s,fax = %s  WHERE name = %s"
            sql_val = (ranking, website, logo, description, acronym, founded, motto, colors, address, tel, fax, name)
            cursor.execute(sql_update, sql_val)
            db.commit()
        else:
            # Data does not exist, insert it
            sql_insert = "INSERT INTO universities_data (name, ranking, website, logo, description, acronym, founded, motto, colors, address, tel, fax) VALUES (%s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val_insert = (name, ranking, website, logo, description, acronym, founded, motto, colors, address, tel, fax)
            print("")
            cursor.execute(sql_insert, val_insert)

            db.commit()
    db.close()