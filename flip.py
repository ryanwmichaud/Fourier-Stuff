import PIL
from PIL import Image as im
import sys 
import numpy as np


def main(input_file):
    
    
    upsidedown = ''
    backwards = ''

    while (upsidedown != 'y' and upsidedown != 'n' ):
        print('upsidedown? (y/n)')
        upsidedown = input()
    
    while (backwards != 'y' and backwards != 'n' ):
        print('backwards? (y/n)')
        backwards = input()



    image = PIL.Image.open(input_file)
    array = np.array(image)

    if(upsidedown=='y'):
        array = np.flip(array)
   
    if(backwards=='n'):
        for i in range(array.shape[0]):
            array[i] = np.flip(array[i])

    image = im.fromarray(array) 
    image = image.convert("L")
    image.save(input_file+"_flipped.png")


if __name__ == "__main__" :
    main(sys.argv[1])