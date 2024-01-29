from gtts import gTTS       ## importing the package
import os                   ## The OS module in python provides functions for interacting with the operating system.
text="Hello how are you ?"  ## Text that you want system to voice out
output=gTTS(text=text,lang="en",slow=False)  ## using gTTS package for Python to speak what is mentioned in Text
output.save("output.mp3")                 ## saving the file as mp3 in your local system
os.system('afplay output.mp3')            ## This actually uses the output file using  afplay on mac machine.
#os.system('start output.mp3')            ## if you are using windows machine, you can use start



