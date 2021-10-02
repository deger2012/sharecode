from configparser import ConfigParser
from pprint import pprint
import smtplib
import email
import ssl
from email.mime.text import MIMEText
from email.header import Header

class MyMailSender:
    def sendMail(subject, mailMessage):
        mailSettings = MyMailSender.iniReader();
        # 第三方 SMTP 服务
        mail_host=mailSettings['mail_host']  #设置服务器
        mail_port=mailSettings['mail_port']  #设置端口
        mail_user=mailSettings['mail_user']    #用户名
        mail_pass=mailSettings['mail_pass']   #口令 
 
 
        sender = mailSettings['sender']
        receivers = mailSettings['receiver']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
 
        message = MIMEText(mailMessage, 'plain', 'utf-8')
        message['From'] = mailSettings['from']
        message['To'] =  Header(mailSettings['to'], 'utf-8')
 
        message['Subject'] = Header(subject, 'utf-8')
 
 
        try:
            smtpObj = smtplib.SMTP(mail_host, mail_port)
            #context = ssl.create_default_context()
            smtpObj.starttls()
            #smtpObj.connect(mail_host, mail_port)    # 25 为 SMTP 端口号
            smtpObj.login(mail_user,mail_pass)  
            smtpObj.sendmail(sender, receivers, message.as_string())
            print("邮件发送成功")
        except smtplib.SMTPException as e:
            print("Error: 无法发送邮件", e.args)

    def iniReader():
        ini_file = './MailSettings.ini';
        section = 'qqmailsettings';

        cfg = ConfigParser()
        # 读取文件内容
        cfg.read(ini_file);
        cfg_content = dict(cfg.items(section));
        return cfg_content;