import librosa
import soundfile
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import librosa.display
from PIL import Image as im
import sys

def main(input, output):
   
    sig, fs = librosa.core.load(input, sr=8000)
    
    #stft! 
    raw = np.abs(librosa.core.spectrum.stft(sig))
    pretty = raw.copy
    pretty = np.flip(pretty)
   

    for i in range(pretty.shape[0]):
        pretty[i]=np.flip(pretty[i])
        for j in range(pretty.shape[1]):
            pretty[i,j]=pretty[i,j]*255

    input = input.split('.')
    input = input[0]
    print(input)

    p = im.fromarray(pretty[700:]) 
    p = p.convert("L")
    p.save(output+"_pretty.png")

    data = im.fromarray(raw) 
    data = data.convert("L")
    data.save(output+"_raw.png")

if __name__ == "__main__" :
    main(sys.argv[1],sys.argv[2])
   
