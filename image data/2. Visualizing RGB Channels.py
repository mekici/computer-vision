#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 19:38:34 2018

@author: multiproxy
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Read in the image
image = mpimg.imread('images/wa_state_highway.jpg')

plt.imshow(image)

# RGB kanallarını izole etmek için aşağıdaki yöntem kullanılır. R-G-B sıralamasında dizinin 3. 
#boyutu renk kanalını içerir
r = image[:,:,0]
g = image[:,:,1]
b = image[:,:,2]

# Her bir renk kanalının gösterilmesi
f, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(20,10))
ax1.set_title('R channel')
ax1.imshow(r, cmap='gray')
ax2.set_title('G channel')
ax2.imshow(g, cmap='gray')
ax3.set_title('B channel')
ax3.imshow(b, cmap='gray')
