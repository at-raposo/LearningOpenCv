import cv2

cap = cv2.VideoCapture(1); ##TERMO TÉCNICO: The number on the argumment just say which camera we're use
#here we are say to it just Capture a video from cam
# in the inside where u put something for argument, u can put the name of the file name, and it will read your video for you

#now, in this block we´re create a loop to always capture frame by frame

while(True):
    ret, frame = cap.read() ## TERMO TÉCNICO: Vai retornar a bct do true

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #This literraly means transform BGR(blue, green&red frame0 to gray frame
    cv.imshow('frame', gray)
#while so vai ser verdadeiro enquanto o caption conseguir capturar alguma coisa

#só vai ser possível mostrar essa frame se a gente colocar o comando para ela ser mostrada

    if cv2.waitKey(1) & 0xFF == ord('q'): # vai esperar 1s and when click on the "q" on the keyboard this will close the cam and break the loop
#the "OxFF" is like a mask for the 64-bit ?? (WTFKC THIS MEANS)
        break

#para nos meros mortais liberar tudo isso e o programa simplesmente fechar, temos que fazer mais coisas "...no próximo bloco.."

cap.release() #libera
cv2.destroyAllWindows()
