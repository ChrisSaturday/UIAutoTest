import sys
current_work_dir = "D:\Python_Work"
sys.path.append(current_work_dir)
from selenium import webdriver
#import publicfunction
from HTMLTestRunner import HTMLTestRunner
from Basefunction import publicfunction
import configparser
import time, unittest, os
#from Test_Project.Basefunction import publicfunction
base_dir = os.path.abspath(os.path.dirname(os.getcwd())) #获取上级目录路径
current_dir = os.getcwd() #获取当前目录路径
config = configparser.ConfigParser()
config.read(current_dir + '/Configuration/config.ini') #读取配置文件
now = time.strftime("%Y-%m-%d %H_%M_%S") #获取当前时间
username = config.get("user", "userno") #获取登录名
passwd = config.get("user", "passwd") #获取登录密码

class MyTestCase(unittest.TestCase):

    def Setup(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("http://www.baidu.com")



    def Login(self):
        self.driver.find_element_by_id('username').clear()
        self.driver.find_element_by_id('username').send_keys(username)
        self.driver.find_element_by_id('password').clear()
        self.driver.find_element_by_id('password').send_keys(passwd)
        self.driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/form/div[4]/input').click()

    def TearDown(self):
        print('测试执行完毕')
        self.driver.quit()

    def test_Search(self):
        self.Setup()
        public = publicfunction
        self.driver.find_element_by_id('kw').send_keys('selenium')
        self.driver.find_element_by_id('su').click()
        public.insert_image(self.driver, now + '跳转完成.png') #搜索成功截图
        self.TearDown()


if __name__ == "__main__":
    testunit = unittest.TestSuite()
    testunit.addTest(MyTestCase('test_Search'))
    report_path = current_dir + '/Report/test_report/'
    Htmlfile = report_path + now + 'baisearch.html' #设置报告命名格式
    fp = open(Htmlfile, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='测试报告',
                            description='用例执行情况')
    runner.run(testunit)
    fp.close()
