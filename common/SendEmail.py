# coding:utf-8
import smtplib
import time
from email.utils import formataddr
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from ConfigurationFolder.ReadConfig import ReadConfig


def send_email():
    # 当前时间
    # 获取email配置信息
    e_cfg = ReadConfig().get_email_config()
    # 发送者信息
    sender_addr = e_cfg['sender_addr']
    password = e_cfg['password']
    # 接收者信息
    receivers = e_cfg['receivers']
    # smtp服务器
    smtp_server = 'smtp.163.com'
    # 创建MIMEMultipart实例，通过attach方法把MIMEText和MIMEBase添加进去
    msg = MIMEMultipart()
    msg['From'] = formataddr(('wade', sender_addr))
    msg['To'] = formataddr(('receiver', '949768106@qq.com'))
    msg['Subject'] = '聚宝阁自动化接口测试报告'
    # 1、添加邮件正文
    msg.attach(MIMEText('my_jbg interface automated test report!', 'plain', 'utf-8'))
    # 2、添加邮件附件
    with open('../result/test_report.html', 'rb') as f:
        mimebase = MIMEBase('接口测试报告', 'html')
        # 加上必要的头信息
        mimebase.add_header('Content-Disposition', 'attachment', filename = 'report.html')
        mimebase.add_header('Content-ID', '<0>')
        mimebase.add_header('X-Attachment-Id', '0')
        # 读取附件内容
        mimebase.set_payload(f.read())
        # 用Base64编码
        encoders.encode_base64(mimebase)
        # 通过attach将附件添加到MIMEMultipart邮件对象
        msg.attach(mimebase)

    # SMTP协议默认端口是25
    server = smtplib.SMTP(smtp_server, 25)
    # 加密
    server.starttls()
    server.login(sender_addr, password)
    server.sendmail(sender_addr, receivers, msg.as_string())
    server.quit()


if __name__ == '__main__':
    send_email()