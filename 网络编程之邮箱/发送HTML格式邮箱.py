import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = '1@sina.com'
receivers = ['@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

mail_msg = """
<p>Python 邮件发送测试...</p>
<p><a href="http://www.toppr.net">Python教程链接</a></p>
"""
message = MIMEText(mail_msg, 'html', 'utf-8')
message['From'] = Header("Python教程", 'utf-8')
message['To'] =  Header("测试", 'utf-8')

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')


try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message.as_string())
    print ("邮件发送成功")
except smtplib.SMTPException:
    print ("Error: 无法发送邮件")
