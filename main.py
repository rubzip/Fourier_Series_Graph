import numpy as np

from FourierSeries import FourierSeries, load_signal, draw_signal
import argparse
import os

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input')
    parser.add_argument('-n', '--n', nargs='*', default=[20])
    parser.add_argument('-o', '--output')
    parser.add_argument('-f', '--folder', default="imgs")
    parser.add_argument('-c', '--color', default="black")

    args = parser.parse_args()

    filename = args.input
    ns = list(map(int, args.n))
    output = args.output
    folder = args.folder
    color = args.color
    
    if output is None:
        output = '.'.join(filename.split('.')[:-1])
    
    folder = "imgs"
    if not os.path.exists(folder):
        os.makedirs(folder)
    path = os.path.join(folder, output)

    signal = load_signal(filename)
    for n in ns:
        fourier = FourierSeries(N=n, signal=signal)
        w = fourier.predict(np.arange(len(signal)+1))
        draw_signal(signal=w, fname=path+f'-fourier-n{n}.png', color=color)

    draw_signal(signal=signal, fname=path+'-original.png', color=color)