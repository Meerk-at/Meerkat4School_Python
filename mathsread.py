import json
import mysql.connector
from mysql.connector import errorcode

try:
	cnx = mysql.connector.connect(user='meer', password='kat',
                              host='localhost',charset='utf8',
                              database='meerkat4s')
	csr = cnx.cursor()
	query = (
      "INSERT INTO course "
      "(version,ects,name)"
      "VALUES (%s,%s,%s)")
	json_data=open("courses_names").read()
	jdata = json.loads(json_data)
	for k in range (0, len(jdata['unchosenCourses'])):
		course_name = jdata['unchosenCourses'][k][1]
		print (course_name)
		data = (1,1,course_name)
		try:
			csr.execute(query,data)
			print ('hey')
		except Exception, e:
			print (str(e))
	cnx.commit()
	csr.close()
except mysql.connector.Error as err:
	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("Something is wrong with your user name or password")
	elif err.errno == errorcode.ER_BAD_DB_ERROR:
		print("Database does not exists")
	else:
		print(err)
cnx.close()
    