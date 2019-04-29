#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 22:09:49 2019

@author: Murat Ekici
"""
import matplotlib.pyplot as plt
import pytesseract 
from PIL import Image

#eger pytesseract kurulu değilse anaconda prompt'u kullanarak şu kodu yazıp çalıştırın: conda install -c jiayi_anaconda pytesseract 


# Konfigürasyon parametreleri.
  # '-l eng'  İngilizce için eng
  # '--oem 1' OCR Motorununun Modunu LSTM ye ayarlar (Long short-term memory).
  #
  #  Dört tür oem OCR motoru modu var
  #  0    Legacy engine only.
  #  1    Neural nets LSTM engine only.
  #  2    Legacy + LSTM engines.
  #  3    Default, based on what is available.
  #
  #  '--psm 3' sayfa segmentasyon modunu (Page Segmentation Mode (psm)) otoya ayarlar.
  # daha geniş bilgi için -> https://github.com/tesseract-ocr/tesseract/wiki/ImproveQuality

config = ('-l tr --oem 1 --psm 3')
value=Image.open("images/computer-vision.jpg")
plt.imshow(value)

text = pytesseract.image_to_string(value, config='')    

print("text present in images:",text)
