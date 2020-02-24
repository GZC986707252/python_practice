import smtplib,email

fromUserName = '986707252@qq.com'
password = 'ccmnpovcdlkgbdfe'

toUserName = '15073317939@139.com'

chst = email.charset.Charset(input_charset='utf-8')
header = ('From: %s\nTo: %s\nSubject: %s\n\n'%(fromUserName,'xiaoguo',chst.header_encode('这是一个python SMTP邮件测试！')))
body = '你好！'
email_con = header.encode('utf-8')+body.encode('utf-8')
smtp=smtplib.SMTP("smtp.qq.com")
smtp.login(fromUserName,password)
smtp.sendmail(fromUserName,toUserName,email_con)
smtp.quit()
