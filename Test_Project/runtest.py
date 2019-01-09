from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import smtplib
import unittest
import time, os

now = time.strftime("%Y-%m-%d_%H_%M_%S")

#============定义发送邮件==============

def send_mail(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    msgRoot = MIMEMultipart()
    subject = "自动化测试报告"
    #msgRoot= MIMEText(mail_body, 'html', 'utf-8')
    #msgRoot = MIMEText('测试案例执行结果见附件', 'html', 'utf-8')
    #msgRoot['Subject'] = Header("自动化测试报告", 'utf-8')
    #send_file = open(file_new, 'rb').read()
    #msgRoot = MIMEMultipart()
    att = MIMEText(mail_body, 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att['Content-Disposition'] = 'attachment; filename="test_Baidu.html"'
    msgRoot['Subject'] = subject
    msgRoot.attach(att)

    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com')
    smtp.login('hxk970903854@163.com', '1234qwer')
    smtp.sendmail('hxk970903854@163.com', 'hxk970903854@163.com', msgRoot.as_string())

    smtp.quit()
    print('email has send out!')

#==========查找测试报告目录，找到最新生成的测试报告文件============

def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + '\\' + fn))
    file_new = os.path.join(testreport, lists[-1])
    print(file_new)
    return file_new

if __name__ == '__main__':

    #test_dir = 'D:\\Python_Work\\Test_Project'
    test_dir = 'D:\\CompanyCode\\Python\\Python_Work\\Python_Work\\Test_Project'
    #test_report = 'D:\\Python_Work\\Test_Project\\Report\\test_report'
    test_report = 'D:\\CompanyCode\\Python\\Python_Work\\Python_Work\\Test_Project\\Report\\test_report'

    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')

    filename = test_report + '\\' + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='测试报告',
                            description='用例执行情况')
    runner.run(discover)
    fp.close()
    new_report = new_report(test_report)
    send_mail(new_report)


