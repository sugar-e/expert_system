import sys
from unittest import result
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QDockWidget, QListWidget, QRadioButton, QButtonGroup
from PyQt5.QtGui import *
from first_sight import Ui_first_sight  #导入创建的GUI类
from result import Ui_Result

from welcome import Ui_welcome
from professional import Ui_professional
from character import Ui_character
import numpy as np
import string

DIC={11:'spring',12:'summer',13:'fall',14:'winter',21:'arbor',22:'bush',23:'herbal',24:'notsure',
    31:'white',32:'pink',33:'red',34:'yello',35:'orange',36:'blue',37:'purple'}

professionalRules=[]
class5_characters=['卵形花瓣','圆形花瓣','倒卵形花瓣','椭圆形花瓣','蓝色花瓣','蓝紫色花瓣','紫色花瓣','黄色花瓣','急尖叶端','下延叶基','总状花序','单朵腋生花序','花冠筒漏斗状\像风车','花瓣十字对生']

def icp(a):
    '''
    运算符的优先级
    '''
    if a=='AND' or a=='OR':
        return 1
    elif a=='(':
        return 0
    elif a=='$':
        return -1


def mid2pos(mid):
    '''
    将中缀表达式转换成后缀表达式
    '''
    pos=[]
    s=['$']
    for c in mid:
        if c=='0' or c=='1':
            pos.append(c)
        elif c == 'AND' or c=='OR':
            while icp(c) <= icp(s[len(s)-1]):
                pos.append(s[len(s)-1])
                del(s[len(s)-1])
            s.append(c)
        elif c=='(':
            s.append(c)
        elif c==')':
            while s[len(s)-1] != '(':
                pos.append(s[len(s)-1])
                del(s[len(s)-1])
            del(s[len(s)-1]) #把(去掉
    while len(s)>1:
        pos.append(s[len(s)-1])
        del(s[len(s)-1])
    print(pos)
    return pos


def calculate(pos):
    '''
    计算后缀表达式的值
    '''
    s=[]
    x=0
    y=0
    for c in pos:
        if c=='0':
            s.append(0)
        elif c=='1':
            s.append(1)
        elif c=='AND':
            x=s[len(s)-1]
            del(s[len(s)-1])
            y=s[len(s)-1]
            del(s[len(s)-1])
            s.append(x&y)
        elif c=='OR':
            x=s[len(s)-1]
            del(s[len(s)-1])
            y=s[len(s)-1]
            del(s[len(s)-1])
            s.append(x^y)
    result=s[len(s)-1]
    if len(s)==1:
        return result
    else:
        return -1



def loadRules():
    global professionalRules
    professionalRules=(np.load('./src/professional.npy',allow_pickle=True)).tolist()
    # print(professionalRules)


class MainWindow(QtWidgets.QMainWindow, Ui_welcome):
    '''
    主界面
    '''
    switch_window1=QtCore.pyqtSignal()#花卉植物的基本信息
    switch_window2=QtCore.pyqtSignal()#修改规则
    switch_window3=QtCore.pyqtSignal()#退出
    switch_window4=QtCore.pyqtSignal()#专业植物鉴别
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.goSearch)
        self.pushButton_3.clicked.connect(self.goEdit)
        self.pushButton_2.clicked.connect(QCoreApplication.instance().quit)
        self.pushButton_4.clicked.connect(self.goProfessional)
    def goSearch(self):
        self.switch_window1.emit()
    def goEdit(self):
        self.switch_window2.emit()
    def goProfessional(self):
        self.switch_window4.emit()





class FirstWindow(QtWidgets.QWidget, Ui_first_sight):
    '''
    根据季节、高度、花色进行组别分类
    '''
    switch_window1=QtCore.pyqtSignal()#主菜单
    switch_window2=QtCore.pyqtSignal()
    def __init__(self):
        
        #需要重载一下
        super().__init__()
        Ui_first_sight.__init__(self)
        self.setupUi(self)

        self.bg1 = QButtonGroup(self)
        self.bg1.addButton(self.radioButton,11)# 'spring')
        self.bg1.addButton(self.radioButton_3,12)# 'summer')
        self.bg1.addButton(self.radioButton_2, 13)#'fall')
        self.bg1.addButton(self.radioButton_4, 14)#'winter')

        self.bg2 = QButtonGroup(self)
        self.bg2.addButton(self.radioButton_8, 21)#'arbor')
        self.bg2.addButton(self.radioButton_6, 22)#'bush')
        self.bg2.addButton(self.radioButton_5, 23)#'herbal')
        self.bg2.addButton(self.radioButton_15, 24)#'notsure')

        self.bg3=QButtonGroup(self)
        self.bg3.addButton(self.radioButton_9, 31)#'white')
        self.bg3.addButton(self.radioButton_10,32)# 'pink')
        self.bg3.addButton(self.radioButton_7, 33)#'red')
        self.bg3.addButton(self.radioButton_11, 34)#'yello')
        self.bg3.addButton(self.radioButton_12, 35)#'orange')
        self.bg3.addButton(self.radioButton_13, 36)#'blue')
        self.bg3.addButton(self.radioButton_14, 37)#'purple')

        self.season=''
        self.type=''
        self.color=''
       
        self.pushButton_3.clicked.connect(self.goMain)
        self.pushButton_2.clicked.connect(self.classify) #“确认”按钮
        self.bg1.buttonClicked.connect(self.rbclicked)
        self.bg2.buttonClicked.connect(self.rbclicked)
        self.bg3.buttonClicked.connect(self.rbclicked)

    def goMain(self):
        self.close()
        self.switch_window1.emit()

    def classify(self):
        #根据输入的三个基本信息判断组别
        self.data=[self.season,self.type,self.color]

        f=open('./src/rules.txt')
        for line in f.readlines():
        
            front=(line.split('THEN')[0]).split(' ')
            del(front[0]) #删去'IF'
            i=0
            while i < len(front):   #计算命题变元（a is b）的值计算出来，并用bool值替换掉原来的变元
                if front[i] == 'is':
                    if front[i+1] in self.data:
                        front[i]='1'
                    else:
                        front[i]='0'
                    del(front[i-1])
                    del(front[i])
                if front[i] == 'isnot':
                    if front[i+1] in self.data:
                        front[i]='0'
                    else:
                        front[i]='1'
                    del(front[i-1])
                    del(front[i])
                i+=1
            pos=mid2pos(front) #将中缀表达式转换成后缀表达式
            result=calculate(pos)#计算表达式的值
                        
                
               
            if result == 1:
                self.classtype=line.split('THEN ')[1]
                break
        else:
            self.classtype='wrong'
        print(self.classtype)
        #转换到结果界面
        #TODO
        self.photo='./src/樱花.jpg'
        self.inference='鉴定结果：樱花\n性状：春，乔木，粉，花瓣有缺刻'
        self.switch_window2.emit()
            

    def rbclicked(self):
        sender=self.sender()
        if sender == self.bg1:
            self.season=DIC[self.bg1.checkedId()]
        if sender == self.bg2:
            self.type=DIC[self.bg2.checkedId()]
        if sender == self.bg3:
            self.color=DIC[self.bg3.checkedId()]
       
class CharacterWindow(QtWidgets.QWidget, Ui_character):
    '''
    根据性状向量计算匹配度
    '''
    switch_window1=QtCore.pyqtSignal()#主菜单
    switch_window2=QtCore.pyqtSignal()
    def __init__(self):
        
        #需要重载一下
        super().__init__()
        Ui_character.__init__(self)
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.goMain) #返回主菜单
        self.pushButton.clicked.connect(self.onClick)

    # def setup(self,classtype):
    #     self.setupUi(self,classtype)#传入图片和输出信息
        
    def goMain(self):
        self.close()#返回主菜单，先将自己关闭
        self.switch_window1.emit()
    def onClick(self):
        '''
        读入用户输入，计算匹配度
        '''
        global class5_characters
        self.charactertext=self.editor.text()
        c=[]
        items=self.charactertext.split(',')
        items=[int(x) for x in items]
        for t in items:
            c.append(class5_characters[t])
        max_degree=0
        match_degreeds={}
        result=''
        classRules=(np.load('./src/class5.npy',allow_pickle=True)).tolist()
        for r in classRules:
            print(r)
            tmp=0
            for t in items:
                tmp+=classRules[r][t-1]
            match_degreeds[r]=tmp
            if tmp > max_degree:
                max_degree=tmp
                
                result=r
        
        message=''
        print("成功鉴别")
        message="鉴别出这是:"+result+"\n"
        message+="【判断依据】\n根据您的选择，该植物有以下性状:\n"
        for t in items:
            message+=class5_characters[t-1]+','
        message+='\n各个类型的植物的匹配度分别为：\n'
        for r in match_degreeds:
            message+=r+str(match_degreeds[r])+'\n'
        #转换到结果界面

        self.photo='./src/'+result+'.jpg'
        self.inference=message
        # self.close()
        self.switch_window2.emit()

        # print(self.charactertext)



class ResultWindow(QtWidgets.QWidget, Ui_Result):
    '''
    结果界面
    '''
    switch_window1=QtCore.pyqtSignal()#主菜单
    def __init__(self):
        super().__init__()
        Ui_Result.__init__(self)

        # super(MainWindow, self).__init__()
    def setup(self,photo,inference):
        self.setupUi(self,photo,inference)#传入图片和输出信息
        self.pushButton.clicked.connect(self.goMain)
        self.pushButton_2.clicked.connect(QCoreApplication.instance().quit)
    def goMain(self):
        self.close()#返回主菜单，先将自己关闭
        self.switch_window1.emit()



class ProfessionalWindow(QtWidgets.QMainWindow, Ui_professional):
    '''
    专业植物鉴别，根据专业知识，鉴别植物所属的科
    最终输出相应的科，以及判断依据（即选择的相应的植物性状）
    '''
    switch_window1=QtCore.pyqtSignal()#主菜单
    def __init__(self):
        super(ProfessionalWindow, self).__init__()
        self.count=0 #用于记录查询的rule的数量
        self.inference=[]#用于记录推断过程
        self.result='1' #用于记录结果
        self.has=0
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Yes)
        self.pushButton_2.clicked.connect(self.goMain)
        self.pushButton_3.clicked.connect(self.No)
        self._translate = QtCore.QCoreApplication.translate

        print(professionalRules[self.result][self.count][0])
        self.label_2.setText(self._translate("professional", professionalRules[self.result][self.count][0]))


    def goMain(self):
        self.close()
        self.switch_window1.emit()

    def Yes(self):
        global professionalRules
        self.inference.append(professionalRules[self.result][self.count][0])
        self.result=professionalRules[self.result][self.count][1]
        self.count=0
        if "科" in self.result:
            print("成功鉴别")
            message="鉴别出这是:"+self.result+"\n"
            message+="【判断依据】\n根据您的选择，该植物有以下性状:\n"
            for m in self.inference:
                message+=m+"。\n"
            self.label_3.setText(self._translate("professional", message))
        else:
            self.label_2.setText(self._translate("professional", professionalRules[self.result][self.count][0]))
    def No(self):
        self.count+=1
        if (self.count < len(professionalRules[self.result])) :
            
            self.label_2.setText(self._translate("professional", professionalRules[self.result][self.count][0]))
        else:
            # print("出错")
            #所有规则都没有匹配的，展示错误信息，提示用户返回主菜单重新开始
            reply = QMessageBox.warning(self,
                "错误", 
                "没有找到对应的类别，请返回主菜单重新开始", 
                QMessageBox.Yes | QMessageBox.No)
            self.echo(reply)
    
    
    def Search(self):
        global professionalRules
        print("确认")

        
        if self.has==1:
            
            self.inference.append(professionalRules[self.result][self.count][0])
            self.result=professionalRules[self.result][self.count][1]
            self.count=0
            if "科" in self.result:
                print("成功鉴别")
                message="鉴别出这是:"+self.result+"\n"
                message+="【判断依据】根据您的选择，该植物有以下性状:\n"
                for m in self.inference:
                    message+=m+"。\n"
                self.label_3.setText(self._translate("professional", message))
            else:
                self.label_2.setText(self._translate("professional", professionalRules[self.result][self.count][0]))
            
        else:
            if (self.count < len(professionalRules[self.result])) :
                self.label_2.setText(self._translate("professional", professionalRules[self.result][self.count][0]))
                self.count+=1
            else:
                reply = QMessageBox.warning(self,
                  "错误", 
                  "没有找到对应的类别，请返回主菜单重新开始", 
                  QMessageBox.Yes | QMessageBox.No)
                self.echo(reply)

    def echo(self, value):
        '''显示对话框返回值'''
        QMessageBox.information(self, "返回值",  "得到：{}\n\ntype: {}".format(value, type(value)), QMessageBox.Yes | QMessageBox.No)
    def rbclicked(self):
        if self.bg.checkedId() == 1:
            self.has=1
            print("是")
        else:
            self.has=0
            



# 利用一个控制器来控制页面的跳转
class Controller:
    def __init__(self):
        pass
    # 跳转到 main 窗口
    def show_main(self):
        self.main = MainWindow()
        self.main.switch_window1.connect(self.show_search)
        self.main.switch_window4.connect(self.showProfessional)
        self.main.show()

    # 跳转到search窗口, 注意关闭原页面
    def show_search(self):
        self.search = FirstWindow()
        #跳转回主菜单
        self.search.switch_window1.connect(self.show_main)
        self.search.switch_window2.connect(self.showCharacter)
        # self.search.switch_window2.connect(self.showResult)


        # self.main.close()
        self.search.show()
    def showCharacter(self):
        self.CharacterWindow=CharacterWindow()
        # self.CharacterWindow.setup(self.search.classtype)
        self.CharacterWindow.switch_window1.connect(self.show_main)
        self.CharacterWindow.switch_window2.connect(self.showResult)
        
        
        self.CharacterWindow.close()#把上一级界面关闭
        self.CharacterWindow.show()

    def showResult(self):
        self.resultwindow=ResultWindow()
        self.resultwindow.setup(self.CharacterWindow.photo,self.CharacterWindow.inference)
        # self.resultwindow.setup(self.search.photo,self.search.inference)

        self.resultwindow.switch_window1.connect(self.show_main)
        # self.CharacterWindow.close()
        self.resultwindow.show()

    def showProfessional(self):
        self.professionalwindow=ProfessionalWindow()
        self.professionalwindow.switch_window1.connect(self.show_main)
        self.main.close()
        self.professionalwindow.show()
   


if __name__ == '__main__':
    #自动适应屏幕分辨率
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)


    app = QtWidgets.QApplication(sys.argv)
    #生成mywindow的实例
    controller = Controller() # 控制器实例
    loadRules()

    controller.show_main() # 默认展示的是 main 页面
    sys.exit(app.exec_())

