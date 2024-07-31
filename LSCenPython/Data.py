#Importar Librerias
import cv2
import os

# Importarr la clase
import SeguimientoManos as sm

nombre = 'Letra_A'

direccion = 'C:/Users/Tomas/Documents/Lenguaje de programacion/LSC/data'
carpeta = direccion + '/' + nombre

# Si no esta creada la carpeta
if not os.path.exists(carpeta):
    print("CARPETA CREADA: ", carpeta)
    # Creamos la carpeta
    os.makedirs(carpeta)
    
# Lectura de la camara
cap = cv2.VideoCapture(1)

# Cambiar la resolucion
cap.set(3, 1280)
cap.set(4, 720)

# Declaramos contador
cont = 0

# Declarar detector
detector = sm.detectormanos(Confdeteccion = 0.9)

while True:
    # Realizar la lectura de la captura
    ret, frame = cap.read()
    
    # Extraer informacion de la mano
    frame = detector.encontrarmanos(frame, dibujar = False)
    
    # Posicion de una sola mano
    lista1, bbox, mano = detector.encontrarposicion(frame, ManoNum = 0, dibujarPuntos = False, DibujarBox = False, color = [0, 255, 0])
    
    # Si hay mano
    if mano == 1:
        
        # Extrear la informacion del cuadro
        xmin, ymin, xmax, ymax = bbox
        
        # Asignamos margen
        xmin = xmin - 40
        ymin = ymin - 40
        xmax = xmax + 40
        ymax = ymax + 40
        
        # Realizar recorte de nuestra mano
        recorte = frame[ymin:ymax, xmin:xmax]
        
        # Almacenar nuestras imagenes
        cv2.imwrite(carpeta + "/A_{}.jpg".format(cont), recorte)
      
        # Aumentamos contador
        cont = cont + 1
        
        cv2.imshow("RECORTE", recorte)
            
    # Mosttrar FPS
    cv2.imshow("Lengua de senas colombiana", frame)
    
    # Leer nuestro teclado
    t = cv2.waitKey(1)
    if t == 27 or cont == 11:
        break
    
cap.release()
cv2.destroyAllWindows() 
