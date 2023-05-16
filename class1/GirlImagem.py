import cv2

img = cv2.imread('img.png', - 1) # ele vai ler a imagem

#cv2.imread you tell to program to read a imagem
# as a first argumment you put ('name of the image'
# as a seconde argumment you put the scale you want it read
print(img)
# cv2.IMREAD_COLOR 1 = Loads a color image
# cv2.imgread_grayScale 0 = Loads image in grayscale mode
#cv2.imread_unchaged -1 = LOads image as such include alpha channel
print(img) # so com o comando cv2.readimg, não vai fazer nada. ele precisa printar

cv2.imshow('img.png', img) # se vc colocar so isso, a imagem vai aparecer por milisegundos na sua tela
#as a first argumment just put a name you want for the image
# as a second u need to put the documment u want to put

k = cv2.waitKey(2000) #this is for the image keep in the screen
#the second is the miliseconds time it will be on screen
# if we put 0 this window just close if u close it

# a letra k vai ser o tempo que a imagem vai ficar na tela

 # nesse bloco acontece que: se eu apertar k ele fecha, mas se eu apertar qualquer outra tecla ele cria uma cópia
if k == 27: #se eu press k ela vai fechar
    cv2.destroyAllWindows() # function allows users to destroy or close all windows at any time after exiting the scrip
elif k == ord('a'): #ord devolve um valor inteiro da string escrita dentro dele
    #porem toda via, se eu apertar a ele vai criar uma copia
    cv2.imwrite('lena_copy.png', img)
    cv2.destroyAllWindows()
#cv2.imgwrite = cria um arquivo novo
# primeiro argumento = nome da copia do arquivo
# segundo argumento = arquivo que ele vai copiar
