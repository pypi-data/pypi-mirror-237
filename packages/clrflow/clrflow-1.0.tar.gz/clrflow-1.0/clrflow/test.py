import clrflow,os,random,time
lorem = "clrflow is made by @rver. on discord, @rver38 on GitHub, and is part of the rverflow bundle.\nLorem ipsum dolor sit amet.\nAt vero eos et accusam et justo duo dolores et ea rebum.\nStet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."







time.sleep(1)
clr = """                             ▒
                         ▓▓▓▓▓
                       ▓▓▓▓▓▓ 
                    ▓▓▓▓▓▓▓▓  
                 ▓▓▓▓▓▓▓▓▓    
               ▓▓▓▓▓▓▓▓▓▓     
               ▓▓▓▓▓▓▓▓▓      
                 ░▓▓▓▓        
       ▓▓▓▓▓▓▓                
      ▓▓▓▓▓▓▓▓▓▓              
     ▒▓▓▓▓▓▓▓▓▓▓              
     ▓▓▓▓▓▓▓▓▓▓▓              
     ▓▓▓▓▓▓▓▓▓▓               
   ▓▓▓▓▓▓▓▓▓▓▓                
 ▓▓▓▓▓▓▓▓▓▓░                  """

rver = """            ▓       
     ▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      
   ▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓       
  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓        
 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓       
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒      
      ░▓▓░▓▓▓▓▓▓▓▓▓▓▓▓▓▓      
        ▓▓  ▓▓▓▓▓ ▓▓▓▓▓▓▓     
                   ▓▓▓▓▓▓░    
                     ▓▓▓▓▓    
                      ▓▓▓▓    
                       ▓▓▓    
                      ░▓▓▓▓▓  
                     ▓▓▓▓▓▓▓▓▓
                     ▓  ░▓▓░▓▓"""

print("gradient and align test")
time.sleep(1)
tmp = False
for v in ["top","center","bottom"]:
  for h in ["left","center","right"]:
    for s in ["left","center","right"]:
      os.system("cls")
      bc = clrflow.gradient(fr=(200,0,150),to=(225,255,0),layer="back",ignoreWhitespace=False)
      print(clrflow.tools.align(s=bc(lorem),horizontal=h,vertical=v,separate=s),end="")
      time.sleep(0.25)

os.system("cls")
print("pattern test")
time.sleep(1)
for x in ["fore","back"]:
  for i in clrflow.pattern.get_patterns():
    os.system("cls")
    print(clrflow.pattern(name=i,layer=x)(lorem))
    time.sleep(0.5)

os.system("cls")
print("progressbar test")
time.sleep(1)
a = clrflow.tools.progressbar(100)
for i in range(100):
  print(a.step(1),end="")
  time.sleep(0.01)
os.system("cls")
a = clrflow.tools.progressbar(75,mx=250,lc="*",mc=".",fr="\rclrflow: -{lc}{mc}- ({pr}%, {cn}/{mx})")
for i in range(100):
  print(a.step(2.5),end="")
  time.sleep(0.01)

os.system("cls")
print("additional text formatting test")
time.sleep(1)
for i in "BDIUbihs":
  os.system("cls")
  print(clrflow.clr.format(i)+lorem+clrflow.clr.reset)
  time.sleep(0.5)
  
os.system("cls")
print("print functions test")
time.sleep(1)
for i in range(20):
  os.system("cls")
  clrflow.tools.custom_print(lorem,i,i)
  time.sleep(0.1)
time.sleep(1)
os.system("cls")
clrflow.tools.slow_print(bc("clrflow is made by @rver. on discord, @rver38 on GitHub, and is part of the rverflow bundle."))
clrflow.tools.slow_print(clrflow.pattern(name="rainbow")(lorem),dur=0.01)
time.sleep(3)

clrflow.tools.slow_print(clrflow.pattern(name="galaxy")(clr),dur=0)
time.sleep(5)










