#-*-coding:utf-8-*-
from selenium import webdriver
import time,sys,configparser,os
base_dir = os.path.abspath(os.path.dirname(os.getcwd())) #获取上级目录路径
config = configparser.ConfigParser()
config.read(base_dir + '/Project_Add/Configuration/config.ini') #读取配置文件
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + 'D:\Python_Work\SettleMent_System\test_case\SettleMent_Parameters\Business_Parameters\Basefunction'))
#username = config.get("user", "userno") #获取登录名
#passwd = config.get("user", "passwd") #获取登录密码
'''
名称：choseData
功能：获取table中指定的内容并选择
参数：driver:驱动，number：查询到的数据总数  name：查考名称
返回值：无
Created on 2017年2月13日
@author: 张伟豪
'''
j=1
def choseData(driver,number,name):
    for i in range(number):
        global j
        path2="//table[@id='mr_table']/tbody/tr["+str(j)+"]/td[4]"
        getData = driver.find_element_by_xpath(path2).text
        if getData==name:
            time.sleep(2)
            driver.find_element_by_xpath(path2).click()
            print(getData)
            break
        if i==9:
            driver.find_element_by_link_text("›").click()
            time.sleep(2)
            j=1
        j=j+1
#             print getData




'''
名称returnDictsvalue
功能：循环遍历自定义字典，并返回指定的value值
参数：chose:想要获取的数据名称 ，**dd：自定义字典名称
返回值：字典指定key的value值
Created on 2017年2月13日
@author: 张伟豪
'''
def returnDictsvalue(chose,**dd):

    for key,value in dd.items():
        try:
            if key==chose:
                break
        except:
            print("找不到该类型")
    return value
'''
名称：getTop
功能：操作页面滚动条至顶部，使元素可见
参数：driver：驱动
返回值：无
Created on 2017年2月13日
@author: 张伟豪
'''
def getTop(driver):
    js="var q=document.documentElement.scrollTop=0"
    driver.execute_script(js)
    time.sleep(3)
'''
名称：getBottom
功能：操作页面滚动条至底部，使元素可见
参数：driver：驱动
返回值：无
Created on 2017年2月13日
@author: 张伟豪
'''
def getButtom(driver):
    js="var q=document.documentElement.scrollTop=5000"
    driver.execute_script(js)
    time.sleep(3)

'''
名称：insert_image
功能：截屏函数
参数：driver：驱动
返回值：无
Created on 2018年5月13日
@author: 韩晓坤
'''
def insert_image(driver,file_name):
    base= os.getcwd()
    file_path=base+"/Report/screenshot/"+file_name
    print("image_address:"+file_path)
    driver.get_screenshot_as_file(file_path)

'''
名称：getbasepath
功能：获取当前文件路径
参数：无
返回值：字段名boss之前的文件路径
Created on 2017年2月13日
@author: 张伟豪
'''
def getbasepath():
    base_dir=os.path.dirname(os.path.dirname(__file__))
    base_dir=str(base_dir)
    base_dir=base_dir.replace('\\','/')
    base=base_dir.split('/boss')[0]
#     print base
    return base

'''
名称：getsuperiorpath
功能：获取当前文件的上级路径
参数：无
返回：当前文件的上级文件夹的路径
Created on 2018-05-17
@author: 韩晓坤
'''
def getsuperiorpath():
    base_dir=os.path.abspath(os.path.dirname(os.getcwd()))
    return base_dir

'''
名称:测试函数
@author: 韩晓坤
'''
if __name__=='__main__':
    driver=webdriver.Firefox()
    driver.get("https://www.baidu.com")
    insert_image(driver,'baidu.jpg')
    driver.quit()

'''
名称：浏览器启动
@author：韩晓坤
'''
def Setup(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get('http://test.pmp.jr.jd.com')

'''
名称：系统登录
@author：韩晓坤
'''
def Login(self):
        self.driver.find_element_by_id('username').clear()
        self.driver.find_element_by_id('username').send_keys(username)
        self.driver.find_element_by_id('password').clear()
        self.driver.find_element_by_id('password').send_keys(passwd)
        self.driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/form/div[4]/input').click()


'''
名称：浏览器关闭
@author：韩晓坤
'''
def Teardown(self):
        print("测试执行完毕")
        self.driver.quit()