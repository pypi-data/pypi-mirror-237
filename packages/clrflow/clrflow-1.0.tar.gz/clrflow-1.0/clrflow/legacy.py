import os

def color(fr,to,ch,s,mode="horizontal",ignore_spaces=True):
     os.system("")
     f = ""
     r,g,b = fr
     if ch=="auto":
          if mode == "horizontal":
               ch=round(255/len(max(s.splitlines(), key=len)))
          elif mode=="vertical":
               ch=round(255/len(s.splitlines()))
          else:
               ch=0
     for line in s.splitlines():
          if mode == "horizontal":
               r,g,b = fr
          for char in line:
               if (r,g,b)!=to:
                    if isinstance(ch,tuple):
                         if r != to[0]:
                              if fr[0] < to[0]:
                                   r += ch[0]
                              else:
                                   r -= ch[0]
                         if g != to[1]:
                              if fr[1] < to[1]:
                                   g += ch[1]
                              else:
                                   g -= ch[1]
                         if b != to[2]:
                              if fr[2] < to[2]:
                                   b += ch[2]
                              else:
                                   b -= ch[2]
                    elif isinstance(ch,int):
                         if mode == "horizontal":
                              if r != to[0]:
                                   if fr[0] < to[0]:
                                        r += ch
                                   else:
                                        r -= ch
                              if g != to[1]:
                                   if fr[1] < to[1]:
                                        g += ch
                                   else:
                                        g -= ch
                              if b != to[2]:
                                   if fr[2] < to[2]:
                                        b += ch
                                   else:
                                        b -= ch
               if r < 0:
                    r = 0
               elif r > 255:
                    r = 255
               if g < 0:
                    g = 0
               elif g > 255:
                    g = 255
               if b < 0:
                    b = 0
               elif b > 255:
                    b = 255
               f += f"\033[38;2;{r};{g};{b}m{char}\033[0m"
          if mode == "vertical":
               if isinstance(ch,int):
                    if r != to[0]:
                         if fr[0] < to[0]:
                              r += ch
                         else:
                              r -= ch
                    if g != to[1]:
                         if fr[1] < to[1]:
                              g += ch
                         else:
                              g -= ch
                    if b != to[2]:
                         if fr[2] < to[2]:
                              b += ch
                         else:
                              b -= ch
          f+="\n"
     f+="]"
     return f[:-2]

def create(*, fr:tuple,to: tuple,change:tuple or int or str,mode="horizontal"):
     return lambda s: color(fr,to,change,s,mode)


cls = {}
def loop(*, name,colors,steps):
     tmp = []
     for i in range(len(colors)):
          fr = colors[i]
          to = colors[(i+1)%len(colors)]
          for y in range(steps+1):
               r = int(round(fr[0] + (to[0] - fr[0]) * y / (steps-1)))
               g = int(round(fr[1] + (to[1] - fr[1]) * y / (steps-1)))
               b = int(round(fr[2] + (to[2] - fr[2]) * y / (steps-1)))
               r = int(max(0, min(255, r)))
               g = int(max(0, min(255, g)))
               b = int(max(0, min(255, b)))
               tmp.append((r,g,b))
     cls[name] = tmp


loop(name="rainbow",colors=[(255,0,0),(255,255,0),(0,255,0),(0,255,255),(0,0,255),(255,0,255),],steps=9)
loop(name="fire",colors=[(255,0,0),(255,100,0),(255,0,0),(255,255,0),],steps=10)
loop(name="galaxy",colors=[(0,0,255),(0,255,255),(255,0,255)],steps=10)
loop(name="water",colors=[(45, 105, 215),(0,255, 215),(0,100,255)],steps=10)
loop(name="bubblegum",colors=[(255,0,255),(255,255,255),(195, 105, 220)],steps=10)
def templates(tmp,s,mode):
     os.system("")
     f = ""
     if tmp in cls.keys():
          for i,line in enumerate(s.splitlines()):
               if mode == "vertical":
                    r,g,b = cls[tmp][i % len(cls[tmp])]
               for y,char in enumerate(line):
                    if mode == "horizontal":
                         r,g,b = cls[tmp][y % len(cls[tmp])]
                    f += f"\033[38;2;{r};{g};{b}m{char}\033[0m"
               f += "\n"
     elif isinstance(tmp,tuple):
          r,g,b = tmp
          for line in s.splitlines():
               for char in line:
                    f += f"\033[38;2;{r};{g};{b}m{char}\033[0m"
               f+="\n"
     return f[:-1]

def template(*,tmp,mode="horizontal"):
     return lambda s: templates(tmp,s,mode)


class tools:
     def center(*,s,mode="h",a=False,i=True):
          f = """"""
          if not a and "h" in mode:
               l = len(max(s.splitlines(),key=len))
               spaces = round((os.get_terminal_size()[0]-l)/2)
          if "v" in mode:
               lines = round((os.get_terminal_size()[1]-len(s.splitlines()))/2)
               f += "\n" * lines
          for i in s.splitlines():
               if a:
                    l = len(i)
                    spaces = round((os.get_terminal_size()[0]-l)/2)
               if not "h" in mode:
                    spaces = 0
               f+=(" "*spaces)+i+"\n"
          if "v" in mode and i:
               f += "\n" * lines
          return f
     class progressbar:
          def __init__(self,l,*,lc="#",mc=" ",fr="\r[{}{}] - {}%"):
               self.lenght = l
               self.steps = 0
               self.lc = lc
               self.mc = mc
               self.fr = fr
          def step(self,s):
               self.steps += s
               tmp = round(self.steps/(100/self.lenght))
               return self.fr.format(*[self.lc*tmp,self.mc*round(self.lenght-tmp),round(self.steps,2)])
          
