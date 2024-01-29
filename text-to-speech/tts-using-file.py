from gtts import gTTS
import os
text=open('demo.txt','r').read()
output=gTTS(text=text,lang="en",slow=False)

output.save("file_output.mp3")

os.system('afplay file_output.mp3')
