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

def scale(row):
    s = ((row - 0) / (1025-0))
    s*=300
    s+=400 
    return s

def main(input):

    """
    for i in range(image_array.shape[0]):
        color = spectral_color(i+400)
        for j in range(image_array.shape[1]):

            image_array[i,j]=color
    
    """
    
    


    """
    for i in range(image_array.shape[0]):
        row_color = spectral_color(scale(i))
        for j in range(image_array.shape[1]):            
            for k in range(3):
                image_array[i,j,k]=row_color[k]
    """

    sig, fs = librosa.core.load(input, sr=8000)
    freqs = np.abs(librosa.core.spectrum.stft(sig))
    
    
    print(freqs.shape)
    num_freqs = freqs.shape[0] 
    num_times = freqs.shape[1]


    freqs = np.flip(freqs)
    for i in range(num_freqs):
        freqs[i] = np.flip(freqs[i])
        #for j in range(num_times):
        #   freqs[i,j] = 0.9

    column_colors = np.ndarray(shape=(num_times,3))

    image_array2 = np.ndarray(shape=(num_freqs, num_times,3), dtype=np.uint8)

    for freq in range(num_freqs):
        color_to_add = spectral_color(scale(freq))
        for time in range(num_times):
            magnitude = freqs[freq,time] 
            
            for k in range(3):
                column_colors[time,k] += (magnitude*color_to_add[k])
                image_array2[freq,time,k] = magnitude * color_to_add[k]
    
    #divide for avg
    for time in range(num_times):
        for k in range(3):
            column_colors[time,k] /= num_freqs
    print(column_colors)

    
    #build and save image
    
    image_array = np.ndarray(shape=(50, num_times,3),dtype=np.uint8)

    for i in range(image_array.shape[0]):
        for j in range(image_array.shape[1]):     
            color = column_colors[j]       
            for k in range(3):
                image_array[i,j,k]=color[k]
    

    p = im.fromarray(image_array) 
    input = input.split('.')[0]
    p.save(input+"_color.png")

    p = im.fromarray(image_array2) 
    input = input.split('.')[0]
    p.save(input+"_color2.png")



    """
    for i in range(image_array.shape[0]):
        row_color = spectral_color(scale(i))
        for j in range(image_array.shape[1]):
            magnitude = freqs[i,j]
            
            for k in range(3):
                image_array[i,j,k]+= row_color[k]
    """
    
    """
    for i in range(image_array.shape[0]):
        for j in range(image_array.shape[1]):
            for k in range(3):
                image_array[i,j,k] /= image_array.shape[0]
    """
    
  

    """
    
   
   
   
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
   
