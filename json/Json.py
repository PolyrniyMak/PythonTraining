
import json
import pymysql.cursors
# Connect to the database
connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='V18012002b',
                             db='mydb',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

with open('data.json', encoding='utf-8') as json_file:
    data = json.load(json_file)
    for item in data:
        try:
            with connection.cursor() as cursor:
            # Create a new record
                sql = "INSERT INTO `json` (`Name`, `TypeObject`, `Adress`, `global_id`, `SocialPrivileges`, `District`, `IsNetObject`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (item.get('Name')[:45], item.get('TypeObject'), item.get('Address')[:45], item.get('global_id'), item.get('SocialPrivileges'), item.get('District'), item.get('IsNetObject')))

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
        except Exception as e:
            print("Error", e)
        


    connection.close()