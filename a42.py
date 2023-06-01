#!/usr/bin/env python

import random  
from collections import namedtuple

class PyArtConfig:
    """
    this porgram will initialize a python art config class and declare all the variable there
    """
    def __init__(self,x,y):
       
        self.sha = random.randint (0,2)
        self.x = random.randint(0,x)
        self.y = random.randint(0,y)
        self.rad = random.randint(0,100)
        self.rx = random.randint(10,30)
        self.ry = random.randint(10,30)
        self.w = random.randint(10,100)
        self.h = random.randint(10,100)
        self.r = random.randint(0,255)
        self.g = random.randint(0,255)
        self.b = random.randint(0,255)
        self.op = round(random.random(),1)
    def createtuple(self):
        '''
        this function will create a tuple and put them into a particular format
        '''
        return f'{self.sha:>8} {self.x:>10} {self.y:>10} {self.rad:>10} {self.rx:>10} {self.ry:>10} {self.w:>10} {self.h:>10} {self.r:>10} {self.g:>10} {self.b:>10} {self.op:>10}'

class RandomShape:
    def __init__(self, count,x,y):
        """
        this function will initializ a randomshape variable and declare all the variable.
        """
        self.count = count
        self.x = x
        self.y = y
    def __str__(self)->str:
            """
            this fucntion will produce a string about the information of the pyartconfig in a particular format 
            """
        #print(f"CNT SHA X Y RAD RX RY W H R G B OP")
            num1: PyArtConfig =  PyArtConfig(self.x, self.y)
            return f"Sha = {num1.sha}\n"\
            f"X = {num1.x}\n" \
            f"Y = {num1.y}\n" \
            f"RAD = {num1.rad}\n"\
            f"RX = {num1.rx}\n"\
            f"RY = {num1.ry}\n"\
            f"W = {num1.w}\n"\
            f"H = {num1.h}\n"\
            f"R = {num1.r}\n"\
            f"G = {num1.g}\n"\
            f"B = {num1.b}\n"\
            f"OP = {num1.op}\n"

        

    
    def as_par2_line(self):
        """
        this part will create a huge string in the format that part 2 want us to do
        """
        print(f"{'CNT'} {'SHA':>8} {'X':>10} {'Y':>10} {'RAD':>10} {'RX':>10} {'RY':>10} {'W':>10} {'H':>10} {'R':>10} {'G':>10} {'B':>10} {'OP':>10}")
        for i in range(self.count):
            num1: PyArtConfig =  PyArtConfig(self.x, self.y)
            print(f"{i:>3} {num1.createtuple()}")
            

            
        


        return 0
    def as_svg(t:int,canvas:tuple):
        """
        this part will output the data as svg line
        """

       
        width = canvas[0]
        height = canvas[1]
    



        ts: str = "   " * t
        line1 = (f'{ts}<svg width="{width}" height="{height}">\n')
        line2 = (f"{ts}</svg>\n")
        line3 = (f"</body>\n")
        line4 = (f"</html>\n")
        return line1 + line2 + line3 + line4
    
def main()->None:
    """
    this is main function
    i will call delcare the random shape  here and call the the as parline funciton. 
    at the end we should get the data in the shell. 
    """
    ans = RandomShape(7,600,400)
    ans.as_par2_line()
    #print(ans)

if __name__== "__main__":
    main()