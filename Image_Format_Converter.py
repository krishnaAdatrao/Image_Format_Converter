import os
from PIL import Image

# Add Path of the images which has to be converted

path = 'C:\\Users\\hp\\OneDrive\\Desktop\\Img_Converter\\Sample_Images\\roses_jpg'
img_path = os.listdir(path)
for i in range(len(img_path)):
    img = Image.open(img_path[i]).convert('RGB')
    
    # Saving images with the required format in the a certain location
    # {}.png or {}.tif or {}.jpg or {}.jpeg or {}.gif
    # Any format image can be converted to any other format
    
    img.save('C:\\Users\\hp\\OneDrive\\Desktop\\Img_Converter\\Sample_Images\\roses_png\\{}.png'.format(i))
        

        