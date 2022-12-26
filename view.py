import librosa
import soundfile
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import librosa.display
from PIL import Image as im
import sys

def main(input):
   
    sig, fs = librosa.core.load(input, sr=8000)
    #stft! 
    data = np.abs(librosa.core.spectrum.stft(sig))
   
   #flip and scale to be viewable
    data = np.flip(data)
    print(type(data))
    for i in range(data.shape[0]):
        data[i]=np.flip(data[i])
        for j in range(data.shape[1]):
            data[i,j]=data[i,j]*255
    
 
    input = input.split('.')
    input = input[0]
    print(input)


    data = im.fromarray(data) 
    data = data.convert("L")
    data.save(input+"_img.png")

if __name__ == "__main__" :
    main(sys.argv[1])
   
