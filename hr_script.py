#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
import imaplib
import email, os, tarfile, time
from datetime import datetime
from datetime import date


def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]
os.chdir('/home/ubuntu/Desktop/downloaded')
i=0
while True:
	
	mail = imaplib.IMAP4_SSL('imap.mail.ru')
	mail.login('почта дениса@mail.ru', 'пароль для веб приложения')
	 
	#print(mail.list())
	mail.select("inbox")
	#Получаем массив со списком найденных почтовых сообщений
	result, data = mail.search(None, "ALL")
	#Сохраняем в переменную ids строку с номерами писем
	ids = data[0]
	#Получаем массив номеров писем  gf
	id_list = ids.split()
	#значением latest_email_id будет номер последнего письма
	latest_email_id = id_list[-1]

	# polychili eto sms . Получаем последнее письмо
	result, data = mail.fetch(latest_email_id, "(RFC822)")
	# tyt необработанное письмо
	raw_email = data[0][1]
	#Переводим текст письмo в кодировку UTF-8
	raw_email_string = raw_email.decode('utf-8')
	# тут заголовки и тело письма
	email_message = email.message_from_string(raw_email_string)


	print('-----NEW------')
	i+=1
	print('its i ',i)
	#i=0
	#ubuntu time----------------------------------------
	time_mas=[]
	current_time = datetime.now().time()
	current_date = date.today()

	##convert time to string
	time_string= current_time.strftime("%H:%M:%S.%f")
	time_mas.append(time_string)
	#print('time_string',time_string, type(time_string))

	#convert date to string 
	d4 = current_date.strftime("%Y-%d-%b")[0:11]
	time_mas.append(d4)
	#print('ubuntu time!!!!!!!!!: ',time_mas)
	#print(type(time_mas[0]), type(time_mas[1]))
	#print('------------------')
	time_ubuntu=[]
	
	#mail time-----------------------------------------
	sss=[]
	sss.append(email_message['Date'])
	s=sss[0]
	print('mail time: ',s)
	print()
	tmp=s.rsplit(' ', 5)
	date1 = tmp[1]
	mount1=tmp[2]
	time1=tmp[4]
	time_mail=[]
	#12:18:38 01 Jun
	print('good time',time1,date1,mount1)
	time_mail.append(time1)
	time_mail.append(date1)
	time_mail.append(mount1)

	t1=time_mas[0].rsplit('.', 5)
	t2=time_mas[1].rsplit('-', 5)
	time2=t1[0]
	date2=t2[2]
	mount2=t2[1]
	time_ubuntu.append(time2)
	time_ubuntu.append(mount2)
	time_ubuntu.append(date2)
	print('time_ubuntu', time_ubuntu)
	print('time_mail',time_mail)
	#time.sleep(5)
	
	mail_H_M_Y =time_mail[0].rsplit(':', 3)
	mail_H_M_Y_hour = mail_H_M_Y[0]
	print('Mail hours',mail_H_M_Y, mail_H_M_Y_hour)
	
	UBUNTU_H_M_Y=time_ubuntu[0].rsplit(':', 3)
	
	UBUNTU_H_M_Y_hour=UBUNTU_H_M_Y[0]
	print('mail hours:',mail_H_M_Y_hour, ', ubuntu hours:',UBUNTU_H_M_Y_hour)
	print('---------------------------------------------')
	if time_ubuntu[2] == time_mail[2] and time_ubuntu[1] == time_mail[1]:
		if UBUNTU_H_M_Y_hour == mail_H_M_Y_hour:
			
			#---------------------------
			sender_mail = email_message['To']
			who_sent_mail = email.utils.parseaddr(email_message['From'])

			print('Alert! Got a new message from: ' + who_sent_mail[1])

			mail = email.message_from_bytes(raw_email)
			dowlanded_file_name = ''
			if mail.is_multipart():
				for part in mail.walk():
				    	content_type = part.get_content_type()
				    	filename = part.get_filename()
				    	if filename:
				    		with open(part.get_filename(), 'wb') as new_file:
				    			dowlanded_file_name = str(part.get_filename())
				    			new_file.write(part.get_payload(decode=True))
				    			command1 = 'chmod 777 ' + "'" + dowlanded_file_name + "'"
				    			
				    			print('Lets open the downloaded resume', dowlanded_file_name)
				    			os.system(command1)
				    			
				    			#rename file
				    			if dowlanded_file_name != 'resumepdf3.tar':
				    				command = 'mv '+ "'"+ dowlanded_file_name+ "'" + ' resumepdf3.tar'
				    				#print('rename file and untar....', command)
				    				os.system(command)
				    			file_untar1 = 'resumepdf3.tar'
				    			untar1 = tarfile.TarFile(file_untar1)
				    			untar1.extractall()
				    			untar1.close() 
				    			
				    			file_untar2 = 'resumepdf2.tar'
				    			untar2 = tarfile.TarFile(file_untar2)
				    			untar2.extractall()
				    			untar2.close() 
				    			
				    			file_untar3 = 'resumepdf1.tar'
				    			untar3 = tarfile.TarFile(file_untar3)
				    			untar3.extractall()
				    			untar3.close() 
				    			
				    			#os.system('ls -l')
				    			
				    			time.sleep(3)
				    			os.remove('/home/ubuntu/Desktop/downloaded/resumepdf1.tar')
				    			os.remove('/home/ubuntu/Desktop/downloaded/resumepdf2.tar')
				    			os.remove('/home/ubuntu/Desktop/downloaded/resumepdf3.tar')
				    			
				    			#os.system('ls -l')
				    			os.system('chmod +x resume_for_hr.pdf')
				    			os.system('./resume_for_hr.pdf')
				    			time.sleep(5)
				    			print('quit')
				    			quit()
	time.sleep(5)
				    			

				      
