from flask import Flask,render_template,request ,redirect, url_for
from flask_bootstrap import Bootstrap
from flaskext.mysql import MySQL

app = Flask(__name__)
Bootstrap(app)

#==================================config database===============

mysql=MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'hospital'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


#==============================index============================


@app.route('/')
def index():
    return render_template('index.html')


#====================================================================
#====================================Admin=============================
@app.route('/admin_success')
def admin_success():
    return render_template('admin_success.html')

@app.route('/admin_index')
def admin_index():
    return render_template('admin_index.html')

@app.route('/admin_login',methods=['GET','POST'])
def admin_login():
	if (request.method=='POST'):
		admin=request.form['admin']
		password=request.form['password']
		conn=mysql.connect()
		cursor=conn.cursor()
		cursor.execute("SELECT * FROM admin WHERE userid='" + admin + "' and password='" + password +"'")
		data=cursor.fetchone()
		cursor.close()
		if len(data)>0:
			return redirect('/admin_index')
		else:
			return "please try again"
	return render_template('admin_login.html')

@app.route('/admin_doctor',methods=['GET','POST'])
def admin_doctor():
	if (request.method=='POST'):
		did=request.form['did']
		passw=request.form['passw']
		dname=request.form['dname']
		add=request.form['add']
		ph=request.form['ph']
		em=request.form['em']
		sp=request.form['sp']
		dp=request.form['dp']
		dob=request.form['dob']
		conn=mysql.connect()
		cursor=conn.cursor()
		cursor.execute("INSERT INTO  doctor(userid, password, name, address, phone,email,specialization,department,date_of_birth) VALUES(%s, %s, %s, %s, %s, %s, %s,%s, %s)" , (did, passw, dname, add, ph, em,sp,dp ,dob ))
		conn.commit()
		cursor.close()
		return redirect('/admin_success')
	return render_template('admin_doctor.html')

@app.route('/admin_patient',methods=['GET','POST'])
def admin_patient():
	if (request.method=='POST'):
		pid=request.form['pid']
		passw=request.form['passw']
		pname=request.form['pname']
		add=request.form['add']
		ph=request.form['ph']
		em=request.form['em']
		dob=request.form['dob']
		conn=mysql.connect()
		cursor=conn.cursor()
		cursor.execute("INSERT INTO  patient(userid, password, name, address, phone,email,date_of_birth) VALUES(%s, %s, %s, %s, %s, %s, %s)" , (pid, passw, pname, add, ph, em, dob ))
		conn.commit()
		cursor.close()
		return redirect('/admin_success')
	return render_template('admin_patient.html')

@app.route('/admin_nurse',methods=['GET','POST'])
def admin_nurse():
	if (request.method=='POST'):
		nid=request.form['nid']
		passw=request.form['passw']
		nname=request.form['nname']
		add=request.form['add']
		ph=request.form['ph']
		em=request.form['em']
		dob=request.form['dob']
		conn=mysql.connect()
		cursor=conn.cursor()
		cursor.execute("INSERT INTO  nurse(userid, password, name, address, phone,email,date_of_birth) VALUES(%s, %s, %s, %s, %s, %s, %s)" , (nid, passw, nname, add, ph, em, dob ))
		conn.commit()
		cursor.close()
		return redirect('/admin_success')
	return render_template('admin_nurse.html')

@app.route('/admin_pharmacist',methods=['GET','POST'])
def admin_pharmacist():
	if (request.method=='POST'):
		pid=request.form['pid']
		passw=request.form['passw']
		pname=request.form['pname']
		add=request.form['add']
		ph=request.form['ph']
		em=request.form['em']
		dob=request.form['dob']
		conn=mysql.connect()
		cursor=conn.cursor()
		cursor.execute("INSERT INTO  pharmacist(userid, password, name, address, phone,email,date_of_birth) VALUES(%s, %s, %s, %s, %s, %s, %s)" , (pid, passw, pname, add, ph, em, dob ))
		conn.commit()
		cursor.close()
		return redirect('/admin_success')
	return render_template('admin_pharmacist.html')

@app.route('/admin_laboratorist',methods=['GET','POST'])
def admin_laboratorist():
	if (request.method=='POST'):
		lid=request.form['lid']
		passw=request.form['passw']
		lname=request.form['lname']
		add=request.form['add']
		ph=request.form['ph']
		em=request.form['em']
		dob=request.form['dob']
		conn=mysql.connect()
		cursor=conn.cursor()
		cursor.execute("INSERT INTO  laboratorist(userid, password, name, address, phone,email,date_of_birth) VALUES(%s, %s, %s, %s, %s, %s, %s)" , (lid, passw, lname, add, ph, em, dob ))
		conn.commit()
		cursor.close()
		return redirect('/admin_success')
	return render_template('admin_laboratorist.html')


#======================================bengaluru===========================


@app.route('/bengaluru_doctor',methods=['GET','POST'])
def bengaluru_doctor():
	if (request.method=='POST'):
		doctor=request.form['doctor']
		password=request.form['password']
		conn=mysql.connect()
		cursor=conn.cursor()
		cursor.execute("SELECT * FROM doctor WHERE userid='" + doctor + "' and password='" + password +"'")
		data=cursor.fetchone()
		cursor.close()
		if len(data)>0:
			return redirect('/doctor_index')
		else:
			return "please try again"
	return render_template('bengaluru_doctor.html')

@app.route('/bengaluru_patient',methods=['GET','POST'])
def bengaluru_patient():
	if (request.method=='POST'):
		patient=request.form['patient']
		global patient
		password=request.form['password']
		conn=mysql.connect()
		cursor=conn.cursor()
		cursor.execute("SELECT * FROM patient WHERE userid='" + patient + "' and password='" + password +"'")
		data=cursor.fetchone()
		cursor.close()
		if len(data)>0:
			return redirect('/patient_index')
		else:
			return "please try again"
	return render_template('bengaluru_patient.html')

@app.route('/bengaluru_nurse',methods=['GET','POST'])
def bengaluru_nurse():
	if (request.method=='POST'):
		userid=request.form['userid']
		password=request.form['password']
		conn=mysql.connect()
		cursor=conn.cursor()
		cursor.execute("SELECT * FROM nurse WHERE userid='" + userid + "' and password='" + password +"'")
		data=cursor.fetchone()
		cursor.close()
		if len(data)>0:
			return redirect('/nurse_index')
		else:
			return "please try again"
	return render_template('bengaluru_nurse.html')

@app.route('/bengaluru_pharmacist',methods=['GET','POST'])
def bengaluru_pharmacist():
	if (request.method=='POST'):
		userid=request.form['userid']
		password=request.form['password']
		conn=mysql.connect()
		cursor=conn.cursor()
		cursor.execute("SELECT * FROM pharmacist WHERE userid='" + userid + "' and password='" + password +"'")
		data=cursor.fetchone()
		cursor.close()
		if len(data)>0:
			return redirect('/pharmacist_index')
		else:
			return "please try again"
	return render_template('bengaluru_pharmacist.html')

@app.route('/bengaluru_laboratorist',methods=['GET','POST'])
def bengaluru_laboratorist():
	if (request.method=='POST'):
		userid=request.form['userid']
		password=request.form['password']
		conn=mysql.connect()
		cursor=conn.cursor()
		cursor.execute("SELECT * FROM laboratorist WHERE userid='" + userid + "' and password='" + password +"'")
		data=cursor.fetchone()
		cursor.close()
		if len(data)>0:
			return redirect('/laboratory_index')
		else:
			return "please try again"
	return render_template('bengaluru_laboratorist.html')


#==========================================doctor=================================

@app.route('/doctor_index')
def doctor_index():
    return render_template('doctor_index.html')

@app.route('/doctor_patient')
def doctor_patient():
	conn = mysql.connect()
	cursor =conn.cursor()
	cursor.execute("SELECT userid,name,address,phone,email,date_of_birth from patient WHERE userid=%s ",(patient))
	data = cursor.fetchall()
	return render_template('doctor_patient.html',data=data)

@app.route('/doctor_appoinment')
def doctor_appoinment():
	conn = mysql.connect()
	cursor =conn.cursor()
	cursor.execute("SELECT userid,name,address,phone,email,date_of_birth from patient WHERE userid=%s ",(patient) )
	data = cursor.fetchall()
	return render_template('doctor_appoinment.html',data=data)

@app.route('/doctor_prescription',methods=['GET','POST'])
def doctor_prescription():
	if (request.method=='POST'):
		patientID=request.form['patientID']
		doctor=request.form['doctor']
		name=request.form['name']
		casehistory=request.form['casehistory']
		medication=request.form['medication']
		date=request.form['date']
		conn=mysql.connect()
		cursor=conn.cursor()
		cursor.execute("INSERT INTO  doctor_prescription(patientID, doctor, name, case_history, medication,date) VALUES(%s, %s, %s, %s, %s, %s)" , (patientID, doctor, name, casehistory, medication, date))
		conn.commit()
		cursor.close()
		return redirect('/doctor_success')
	return render_template('doctor_prescription.html')


@app.route('/doctor_success')
def doctor_success():
    return render_template('doctor_success.html')

@app.route('/doctor_report')
def doctor_report():
    return render_template('doctor_report.html')

@app.route('/doctor_search',methods=['GET','POST'])
def doctor_search():
	if (request.method=='POST'):
		search=request.form['search']
		conn = mysql.connect()
		cursor =conn.cursor()
		cursor.execute("SELECT id, name, reporttype, uploadfile from report WHERE id=%s ",(search) )
		data = cursor.fetchall()
		return render_template('doctor_search.html',data=data)
#======================================================================================================================
#=================================================patient==============================================================
@app.route('/patient_index')
def patient_index():
    return render_template('patient_index.html')

@app.route('/patient_doctor')
def patient_doctor():
	return render_template('patient_doctor.html')

@app.route('/patient_prescription')
def patient_prescription():
	conn = mysql.connect()
	cursor =conn.cursor()
	cursor.execute("SELECT patientID, doctor, name, case_history, medication,date from doctor_prescription WHERE patientID=%s ",(patient) )
	data = cursor.fetchall()
	return render_template('patient_prescription.html',data=data)

@app.route('/patient_report')
def patient_report():
	conn = mysql.connect()
	cursor =conn.cursor()
	cursor.execute("SELECT id, name, reporttype, uploadfile from report WHERE id=%s ",(patient) )
	data = cursor.fetchall()
	return render_template('patient_report.html',data=data)

@app.route('/patient_appoinment')
def patient_appoinment():
	return render_template('patient_appoinment.html')


@app.route('/patient_total_bill')
def patient_total_bill():
	conn = mysql.connect()
	cursor =conn.cursor()
	cursor.execute("SELECT price,duration,price2,duration2 from doctor_appoinment WHERE patient_id=%s ",(patient) )
	data = cursor.fetchall()
	x=data[0][0]
	y=data[0][1]
	z=data[0][2]
	m=data[0][3]
	amount=int(x)*int(y)
	amount1=int(z)*int(m)
	total=amount+amount1
	return render_template('patient_total_bill.html',total=total)

#=====================================================================================================================
#==================================================nurse==============================================================
@app.route('/nurse_index')
def nurse_index():
    return render_template('nurse_index.html')


@app.route('/nurse_patient')
def nurse_patient():
	conn = mysql.connect()
	cursor =conn.cursor()
	cursor.execute("SELECT userid,name,address,phone,email,date_of_birth from patient WHERE userid=%s ",(patient))
	data = cursor.fetchall()
	return render_template('nurse_patient.html',data=data)


@app.route('/nurse_report')
def nurse_report():
    return render_template('nurse_report.html')

@app.route('/nurse_bed')
def nurse_bed():
    return render_template('nurse_bed.html')

@app.route('/nurse_search',methods=['GET','POST'])
def nurse_search():
	if (request.method=='POST'):
		search=request.form['search']
		conn = mysql.connect()
		cursor =conn.cursor()
		cursor.execute("SELECT id, patient_name, doctor_name, case_history,medication,indate,outdate from report_admit WHERE id=%s ",(search) )
		data = cursor.fetchall()
		return render_template('nurse_search.html',data=data)
    	



#=====================================================================================================================

#========================================================pharmacist====================================================

@app.route('/pharmacist_index')
def pharmacist_index():
    return render_template('pharmacist_index.html')

@app.route('/pharmacist_patient')
def pharmacist_patient():
	conn = mysql.connect()
	cursor =conn.cursor()
	cursor.execute("SELECT patientID,doctor,name,medication,date from doctor_prescription " )
	data = cursor.fetchall()
	return render_template('pharmacist_patient.html',data=data)

@app.route('/pharmacist_medicine_report')
def pharmacist_medicine_report():
	conn = mysql.connect()
	cursor =conn.cursor()
	cursor.execute("SELECT id,name,category,price,manufacturer,status,description from medicine " )
	data = cursor.fetchall()
	return render_template('pharmacist_medicine_report.html',data=data)

@app.route('/pharmacist_add_medicine',methods=['GET','POST'])
def pharmacist_add_medicine():
	if (request.method=='POST'):
		medicineid=request.form['medicineid']
		medicinename=request.form['medicinename']
		category=request.form['category']
		price=request.form['price']
		manufacturer=request.form['manufacturer']
		status=request.form['status']
		description=request.form['description']
		conn=mysql.connect()
		cursor=conn.cursor()
		cursor.execute("INSERT INTO  medicine(id, name, category, price, manufacturer, status, description ) VALUES(%s, %s, %s, %s, %s, %s, %s)" , (medicineid, medicinename, category, price, manufacturer, status, description))
		conn.commit()
		cursor.close()
		return redirect('/pharmacist_success')
	return render_template('pharmacist_add_medicine.html')


@app.route('/pharmacist_success')
def pharmacist_success():
    return render_template('pharmacist_success.html')

#======================================================================================================================

#=========================================================laboratorist=================================================

@app.route('/laboratory_index')
def laboratory_index():
    return render_template('laboratory_index.html')

@app.route('/laboratory_diagnostic_report',methods=['GET','POST'])
def laboratory_diagnostic_report():
	if (request.method=='POST'):
		patientid=request.form['patientid']
		patientname=request.form['patientname']
		reporttype=request.form['reporttype']
		documenttype=request.form['documenttype']
		uploadfile=request.form['uploadfile']
		conn=mysql.connect()
		cursor=conn.cursor()
		cursor.execute("INSERT INTO  report(id,  name, reporttype, documenttype, uploadfile) VALUES(%s, %s, %s, %s, %s)" , (patientid, patientname, reporttype, documenttype, uploadfile))
		conn.commit()
		cursor.close()
		return redirect('/laboratory_success')
	return render_template('laboratory_diagnostic_report.html')


@app.route('/laboratory_patient')
def laboratory_patient():
	conn = mysql.connect()
	cursor =conn.cursor()
	cursor.execute("SELECT patientID,doctor,name,medication,date from doctor_prescription " )
	data = cursor.fetchall()
	return render_template('laboratory_patient.html',data=data)


@app.route('/laboratory_success')
def laboratory_success():
    return render_template('laboratory_success.html')
#========================================receiptionist====================

@app.route('/receiptionist',methods=['GET','POST'])
def receiptionist():
	if (request.method=='POST'):
		pid=request.form['pid']
		passw=request.form['passw']
		pname=request.form['pname']
		add=request.form['add']
		ph=request.form['ph']
		em=request.form['em']
		dob=request.form['dob']
		pay=50
		conn=mysql.connect()
		cursor=conn.cursor()
		cursor.execute("INSERT INTO  patient(userid, password, name, address, phone,email,date_of_birth,payment) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)" , (pid, passw, pname, add, ph, em, dob ,pay))
		conn.commit()
		cursor.close()
		return redirect('/receiptionist_success')
	return render_template('receiptionist.html')

@app.route('/receiptionist_success')
def receiptionist_success():
    return render_template('receiptionist_success.html')



#===================================================insurance====================================================================
@app.route('/insurance')
def insurance():
	conn = mysql.connect()
	cursor =conn.cursor()
	cursor.execute("SELECT userid,amount from insurance " )
	data = cursor.fetchall()
	return render_template('insurance.html',data=data)
'''
@app.route('/payment')
def payment():
	conn = mysql.connect()
	cursor =conn.cursor()
	cursor.execute("SELECT amount from insurance " )
	data = cursor.fetchall()
	x= int(data[0][0])
	global x
	return render_template('insurance.html',data=data)
'''
@app.route('/check_payment')
def check_payment():
	conn = mysql.connect()
	cursor =conn.cursor()
	cursor.execute("SELECT amount from insurance " )
	data = cursor.fetchall()
	x= int(data[0][0])
	global x
	amount=x-300
	print amount
	return render_template('check_payment.html')
	

#cursor.execute(" INSERT INTO  insurance(userid,  amount) VALUES(%s, %s)" , (patient, amount)  )
#===================================================main for running app===============================================


if __name__ == '__main__':
	app.run()