
import PIL
from PIL import Image as im
import numpy as np
import librosa
import soundfile
import sys

#class PIL.Image.Image vs Pil.PngImagePlugin.PngImageFile
def main(file): 
    
    image = PIL.Image.open(file)
    array = np.array(image)
    img_array = array.astype('float64')

    
    #initialize new array
    audio_array = np.ndarray((img_array.shape[0],img_array.shape[1]),dtype=float)

    
    print(img_array.shape, audio_array.shape)

    img_array = np.flip(img_array)  #make freq increase w y axis
    for i in range(img_array.shape[0]):
        img_array[i]=np.flip(img_array[i]) #make x axis left to right
        for j in range(img_array.shape[1]):
            if(len(img_array.shape) == 3):  #convert to 2d greyscale if needed
                avg = (img_array[i,j,0]+img_array[i,j,1]+img_array[i,j,2])/3
                audio_array[i,j] = (avg/10)
            elif(len(img_array.shape) == 2):
                audio_array[i,j] = img_array[i,j]/10  #scale down to audio range 0-255
            else: 
                print("image must be 2 or 3 dimensional, not ",len(img_array.shape))
                exit()

    
    
    file = file.split('.')
    file = file[0]
    print(file)

    #convert to audio
    audio_signal = librosa.core.spectrum.griffinlim(audio_array)
    path  = file+'_generated.wav'
    print(path)
    sr=8000
    print(sr/audio_array.shape[1])
    soundfile.write(path, audio_signal, sr)


    #revisualize 2d array
    """
    for i in range(audio_array.shape[0]):
        for j in range(audio_array.shape[1]):
            audio_array[i,j] = audio_array[i,j]*255

    data = im.fromarray(audio_array) 
    data = data.convert("L")
    data.save("2d_"+file+".png")
    """
    

if __name__ == "__main__" :
    main(sys.argv[1])
   



    """
    for row in array:
        for i in row:
            print(i," ",end='')
        print()
    
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            array[i,j]=array[i,j]
    
    #better for viewing

    pretty = img_spect.copy()
    pretty = np.flip(pretty)

    for i in range(pretty.shape[0]):
        pretty[i]=np.flip(pretty[i])
        for j in range(pretty.shape[1]):
            pretty[i,j]=pretty[i,j]*30

    data = im.fromarray(pretty[500:]) 
    data = data.convert("L")
    data.save("pretty spectrograms/"+file.strip('.wav')+".png")
    """