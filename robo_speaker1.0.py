import pyttsx3
if __name__=='__main__':

   robo=pyttsx3.init()
   while True:
      x=input("write here something,I can help you to speak ") 
      if x=="q"or x=="Q" or x=="quit" or x=="QUIT":
       robo.say("bye bye guys")
       robo.runAndWait()
       break
      robo.say(x)
      robo.runAndWait()