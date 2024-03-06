from Button1 import Opt1
from Button2 import Opt2
from Button3 import Opt3
from Button4 import Opt4
from Button5 import Opt5
from Button6 import Opt6
from Button7 import Opt7

class facade:

    def __init__(self):

        self.button1 = Opt1()
        self.button2 = Opt2()
        self.button3 = Opt3()
        self.button4 = Opt4()
        self.button5 = Opt5()
        self.button6 = Opt6()
        self.button7 = Opt7()

    def b1(self):

        self.button1.opt1()

    def b2(self):

        self.button2.opt2()

    def b3(self):

        self.button3.opt3()

    def b4(self):

        self.button4.opt4()

    def b5(self):

        self.button5.opt5()

    def b6(self):

        self.button6.opt6()
    
    def b7(self):

        self.button7.opt7()

    


    