import PIL
from PIL import Image as im
import sys 
import numpy as np


def main(input_file):
    
    
    upsidedown = ''
    backwards = ''
    int_entered = False
    

    while (upsidedown != 'y' and upsidedown != 'n' ):
        print('upsidedown? (y/n)')
        upsidedown = input()
    
    while (backwards != 'y' and backwards != 'n' ):
        print('backwards? (y/n)')
        backwards = input()

    while (not int_entered):
        print('amount?')
        shift = input()
        try:
            shift = int(shift)
            int_entered = True
        except:
            print("enter an amount to shift down")
        
    print(upsidedown, backwards)
        



    image = PIL.Image.open(input_file)
    array = np.array(image)

    if(upsidedown=='y'):
        array = np.flip(array)
   
    if(backwards=='y'):
        for i in range(array.shape[0]):
            array[i] = np.flip(array[i])


    if(shift != 0):
        new_array = np.ndarray(array.shape)
        if(shift<0):
            print('neg')
            for i in range(shift,array.shape[0]):
                new_array[i] = array[i+shift]
        else:
            for i in range(array.shape[0]-shift):
                new_array[i] = array[i+shift]
        array = new_array
            




    image = im.fromarray(array) 
    image = image.convert("L")
    input_file = input_file.split('.')
    input_file = input_file[0]
    image.save(input_file+"_flipped.png")


if __name__ == "__main__" :
    main(sys.argv[1])