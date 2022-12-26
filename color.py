import librosa
import soundfile
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import librosa.display
from PIL import Image as im
import sys

def spectral_color(l): # RGB <0,1> <- lambda l <400,700> [nm]
    t = 0 
    r=0.0 
    g=0.0 
    b=0.0
    if ((l>=400.0) and (l<410.0)):
        t=(l-400.0)/(410.0-400.0)
        r=    +(0.33*t)-(0.20*t*t)
    elif ((l>=410.0)and (l<475.0)):
        t=(l-410.0)/(475.0-410.0)
        r=0.14 - (0.13*t*t)
    elif ((l>=545.0)and (l<595.0)):
        t=(l-545.0)/(595.0-545.0)
        r=    +(1.98*t)-(     t*t)
    elif ((l>=595.0)and (l<650.0)):
        t=(l-595.0)/(650.0-595.0)
        r=0.98+(0.06*t)-(0.40*t*t)
    elif ((l>=650.0)and (l<700.0)):
        t=(l-650.0)/(700.0-650.0)
        r=0.65-(0.84*t)+(0.20*t*t)
    
    if ((l>=415.0)and (l<475.0)):
        t=(l-415.0)/(475.0-415.0)
        g=             +(0.80*t*t)
    elif ((l>=475.0)and (l<590.0)):
        t=(l-475.0)/(590.0-475.0)
        g=0.8 +(0.76*t)-(0.80*t*t)
    elif ((l>=585.0)and (l<639.0)):
        t=(l-585.0)/(639.0-585.0)
        g=0.84-(0.84*t)         
    
    if ((l>=400.0)and (l<475.0)):
        t=(l-400.0)/(475.0-400.0)
        b=    +(2.20*t)-(1.50*t*t)
    elif ((l>=475.0)and (l<560.0)):
        t=(l-475.0)/(560.0-475.0)
        b=0.7 -(     t)+(0.30*t*t)
    
    return [r*255, g*255, b*255]
    

def main(input):
    
  
    image_array = np.ndarray(shape=(500,500,3),dtype=np.uint8)
    
    for i in range(image_array.shape[0]):
        color = spectral_color(500)
        for j in range(image_array.shape[1]):

            image_array[i,j]=color
    print(image_array)

    p = im.fromarray(image_array) 
  
    p.save("color.png")

    """
    sig, fs = librosa.core.load(input, sr=8000)
    #stft! 
    raw = np.abs(librosa.core.spectrum.stft(sig))
   
   
   
    pretty = raw.copy()
    pretty = np.flip(pretty)
    print(type(pretty))
    for i in range(pretty.shape[0]):
        pretty[i]=np.flip(pretty[i])
        for j in range(pretty.shape[1]):
            pretty[i,j]=pretty[i,j]*10
    
    for i in range(raw.shape[0]):
        for j in range(pretty.shape[1]):
            raw[i,j]=raw[i,j]*10
            


    input = input.split('.')
    input = input[0]
    print(input)

    p = im.fromarray(pretty[700:]) 
    p = p.convert("L")
    p.save(input+"_to_pretty_img.png")

    data = im.fromarray(raw) 
    data = data.convert("L")
    data.save(input+"_to_raw_img.png")"""

if __name__ == "__main__" :
    main(sys.argv[1])
   