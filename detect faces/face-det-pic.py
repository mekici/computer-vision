import cv2
import imageio
import matplotlib.pyplot as plt

# Cascade yükleme
face_cascade = cv2.CascadeClassifier('haarcascade-frontalface-default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade-eye.xml')

# Tanıma yapacak fonksiyon
def tani(fotograf):
    gray = cv2.cvtColor(fotograf, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor= 1.3, minNeighbors=3)
    
    for (x, y, w, h) in faces:
        
        #bu fonksiyon beş parametre alır, ilki fotograf 
        #ikincisi nereden başlayacağı
        #üçüncüsü boyutu
        #dördüncüsü rengi
        #beşincisi kalınlığı
        cv2.rectangle(fotograf, (x, y), (x+w, y+h), (255, 0, 0), 5)
       
        yuz_bulunan_alan_gri= gray[y:y+h, x:x+w]
        yuz_bulunan_alan_renkli= fotograf[y:y+h, x:x+w]
        
        eyes = eye_cascade.detectMultiScale(yuz_bulunan_alan_gri, 1.1, 5)
        
        print(eyes)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(yuz_bulunan_alan_renkli, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
        
        """
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
    """
    return fotograf

# Proje klasörü içerisindeki image.jpg dosyasında yüz ve göz tespiti yapılıyor.
# Daha sonra output.jpg dosyasına yazılıyor.
# Dosya isimlerini değiştirebilirsiniz.
image = imageio.imread('image.jpg')
image = tani(fotograf=image)
imageio.imwrite('output.jpg', image)

plt.imshow(image)

