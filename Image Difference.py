#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sys 
import time

import PIL
from PIL import Image

start = time.time()

for i in range(10):
    print(i)
time.sleep(1)

img1 = Image.open(r"Image1(1).jpg")
img1.show()
# print(img1.size)

img2 = Image.open(r"Image2.jpg")
img2.show()
# print(img2.size)

diff = PIL.ImageChops.difference(img1, img2)
diff.show()

end = time.time()
print(f"Runtime of the program is {end - start}")


# In[ ]:




