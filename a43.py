#!/usr/bin/env python
from typing import IO
import random 

class PyArtConfig:
    def __init__(self,x,y):
        """
        this function will initialize the python art config class and declare all the variabls
        """
       
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
    



    
class ellipse:
    def __init__(self, rec: tuple, col: tuple) -> None:
        """
        this funciton  will initializ the ellipse class and declare all the variabls
        
        """
        self.cx: int = rec[0]
        self.cy: int = rec[1]
        self.rx: int = rec[2]
        self.ry: int = rec[3]
        self.red: int = col[0]
        self.green: int = col[1]
        self.blue: int = col[2]
        self.op: float = col[3]

    def drawellipseLine(self,f:IO[str],t:int):

        """
        this function will created the line that produce a ellipse in svg lines. the shape will be output to the html file
        in visualising, we will get a ellipse after calling this function
        """
       
        ts: str = "   " * t
        line1: str = f'<ellipse cx="{self.cx}" cy="{self.cy}" rx="{self.rx}" ry="{self.ry}" '
        line2: str = f'fill="rgb({self.red}, {self.green}, {self.blue})" fill-opacity="{self.op}"></ellipse>'
        f.write(f"{ts}{line1+line2}\n")


class rectangle:
    """Circle class"""
    def __init__(self, rec: tuple, col: tuple) -> None:
        """
        this function will initialize the rectangle class and declare all the variable 
        """
        self.cx: int = rec[0]
        self.cy: int = rec[1]
        self.wid: int = rec[2]
        self.hei: int = rec[3]
        self.red: int = col[0]
        self.green: int = col[1]
        self.blue: int = col[2]
        self.op: float = col[3]

    def drawrectangleLine(self,f:IO[str],t:int):
        """
        this function will created the line that produce a rectangle in svg lines. the shape will be output to the html file
        in visualising, we will get a rectangle after calling this function
        """
       
        ts: str = "   " * t
        line1: str = f'<rect x="{self.cx}" y="{self.cy}" width="{self.wid}" height="{self.hei}" '
        line2: str = f'fill="rgb({self.red}, {self.green}, {self.blue})" fill-opacity="{self.op}"></rect>'
        f.write(f"{ts}{line1+line2}\n")

   
class Circle:
    """Circle class"""
    def __init__(self, cir: tuple, col: tuple) -> None:
        """
        this functino will initialize circle class and declare all the variable
        """
        self.cx: int = cir[0]
        self.cy: int = cir[1]
        self.rad: int = cir[2]
        self.red: int = col[0]
        self.green: int = col[1]
        self.blue: int = col[2]
        self.op: float = col[3]

    def drawCircleLine(self,f:IO[str],t:int):
        """
        this function will created the line that produce a circle in svg lines. the shape will be output to the html file
        in visualising, we will get a circle after calling this function
        """
      
        ts: str = "   " * t
        line1: str = f'<circle cx="{self.cx}" cy="{self.cy}" r="{self.rad}" '
        line2: str = f'fill="rgb({self.red}, {self.green}, {self.blue})" fill-opacity="{self.op}"></circle>'
        f.write(f"{ts}{line1+line2}\n")

class HtmlDoc:
    """generate html tags"""
    def __init__(self, content: str) -> None:
        """
        this program will initialize the html class and declare all the variables 
        """
        self.Shtml: str= "<html>"
        self.Ehtml: str= "</html>"
        self.Shead: str= "<head>"
        self.Ehead: str= "</head>"
        self.Sbody: str= "<body>"
        self.Ebody: str= "</body>"
        self.content = content



    def writeHTMLHeader(self,f: IO[str], title: str)-> None:
        '''
        this function will write the html head line to the html file we created before
        '''
        self.writeHTMLline(f, 0, self.Shtml)
        self.writeHTMLline(f, 0, self.Shead)
        self.writeHTMLline(f, 1, f"<title>{title}</title>")
        self.writeHTMLline(f, 0, self.Ehead)
        self.writeHTMLline(f, 0, self.Sbody)
    
    def writeHTMLline(self,f: IO[str], t:int, line:str)-> None:
        """
        this function will write the html linee into the html file we created before
        """
        ts = "   " * t 
        f.write(f"{ts}{line}\n")

class SvgCanvas:
    """generate svg tags"""
    def __init__(self,f:IO[str],t:int, canvas:tuple) -> None:
        self.t = t
        self.canvas = canvas
        self.f = f
    
    def openSVGcanvas(self) -> None:
        '''
        this function will create a svg header/opener so that other svg command can be input
        '''
        ts: str = "   " * self.t
        self.f.write(f'{ts}<svg width="{self.canvas==[0]}" height="{self.canvas[1]}">\n')
    def closeSVGcanvas(self)-> None:
        """
        this function will produce the line in html style to close the svg part as long as thee html part. 
        this funciton will be called at the last part
        """
        ts: str = "   " * self.t
        self.f.write(f"{ts}</svg>\n")
        self.f.write(f"</body>\n")
        self.f.write(f"</html>\n")
    def gen_art(self) -> None:
         """
         this function will create shape and output it to the html file.
         the created shape depends on the random value
         """
         for i in range(self.canvas[2]):
            num1: PyArtConfig =  PyArtConfig(self.canvas[0], self.canvas[1])
            if(num1.sha == 0):
                Circle((num1.x,num1.y,num1.rad),(num1.r,num1.g,num1.b,num1.op)).drawCircleLine(self.f, self.t)
            elif(num1.sha == 1):
                rectangle((num1.x,num1.y,num1.w,num1.h),(num1.r,num1.g,num1.b,num1.op)).drawrectangleLine(self.f,self.t)
            else:
                ellipse((num1.x,num1.y,num1.rx,num1.ry),(num1.r,num1.g,num1.b,num1.op)).drawellipseLine(self.f,self.t)


def writeHTMLFile()-> None:
        """
        this function will open a htmlfile and decide what to write in
        """
        fnam: str = "my-Part3-Art.html"
        winTitle: str = "My Art"
        f: IO[str] = open(fnam, "w")
        ans = HtmlDoc(winTitle) 
        ans.writeHTMLHeader(f, winTitle)

        
        
        ans2 = SvgCanvas(f, 1, (600,400,10000))
        ans2.openSVGcanvas()
        ans2.gen_art()
        #ans2.genArt(f, 2)
        ans2.closeSVGcanvas()
        f.close()

        fnam: str = "my-Part3-Art2.html"
        winTitle: str = "My Art"
        f: IO[str] = open(fnam, "w")
        ans = HtmlDoc(winTitle) 
        ans.writeHTMLHeader(f, winTitle)

        
        
        ans2 = SvgCanvas(f, 1, (900,600,50000))
        ans2.openSVGcanvas()
        ans2.gen_art()
        #ans2.genArt(f, 2)
        ans2.closeSVGcanvas()
        f.close()

        fnam: str = "my-Part3-Art3.html"
        winTitle: str = "My Art"
        f: IO[str] = open(fnam, "w")
        ans = HtmlDoc(winTitle) 
        ans.writeHTMLHeader(f, winTitle)

        
        
        ans2 = SvgCanvas(f, 1, (200,1200,20000))
        ans2.openSVGcanvas()
        ans2.gen_art()
        #ans2.genArt(f, 2)
        ans2.closeSVGcanvas()
        f.close()




def main() -> None:
    """
    this is the main function.
    """
    writeHTMLFile()

if __name__== "__main__":
    main()