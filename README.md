# Fourier_Series_Graph
This week, I studied the Fourier Transform in class and decided to investigate it more. I found [the 3Blue1Brown video](https://www.youtube.com/watch?v=r6sGWTCMz2k) about the Discrete Fourier Series and I decided to implement it.

## How to
### Drawer
Fourier series graphs need a specific drawing format, in my case we are using drawings generated without leaving blank space between 2 points. So I need to track every point which is drawed and the order between them.

I didn't found any useful aplication for this task, and I implemented it using `Tkinter`. For calling this program you only need to type in terminal:
```
python3 drawer.py
```
Once the program is open, you only need to drag the red point through the screen to draw lines.

Some useful commands: 
- **s**: to save drawing
- **x**: exit
- **z**: undo movement
- **h**: to show help.
- **Right-Click**: to delete all lines.
- **Up key**: to increase line width.
- **Down key**: to decrease line width.

### Fourier Series Image Generator
This script takes a `TSV` file and returns images with the n-degree Fourier Series graph.  
For calling this program you only need to type in terminal:
```
python3 main.py -i input.tsv -n n1 n2 n3 n4 ... -o output
```
- `input.tsv`: File with all points of the drawing sorted.
- `ni`: degree of Fourier Series.
- `output`: name of output file.


## Discrete Fourier Series
Every drawing has 2 mathematical sequences of T dots defined as:

$$ (x_{k}, y_{k}) \ \ \ \ \ \forall k \in { 0, 1, 2, ..., T-1 } $$

So we define a unique complex sequence as:

$$ z_{k} = x_{k} + i \cdot y_{k} \ \ \ \ \ \forall k \in { 0, 1, 2, ..., T-1 } $$

We consider the periodic discrete function defined for every integer value between 0 and T-1:

$$ f(k) = z_{k} \ \ \ \ \ \forall k \in { 0, 1, 2, ..., T-1 } $$

$$ f(t) = f(t + T) $$

The N-degree Fourier series is defined as:

$$ f_{N}(t) = \sum_{n=-N}^{N} c_{n} e^{2 \pi i n \frac{t}{T}} $$

$$ c_{n} = \frac{1}{T} \int_{0}^{T} f(t) e^{-2 \pi i n \frac{t}{T}} dt $$


## Numerical methods
For solving some computational problems I have split the integral in T different integrals:


$$ c_{n} = \frac{1}{T} \sum_{t=0}^{T-1} \int_{t}^{t+1} f(t) e^{-2 \pi i n \frac{t}{T}} dt $$


If we consider the approximation for a discrete function:

$$ \int_{a}^{b} f(x) dx \approx (b - a) \frac{f(a)+f(b)}{2} $$

$$ c_{n} \approx \frac{1}{T} \sum_{t=0}^{T-1} \frac{f(t+1)e^{-2 \pi i n \frac{t+1}{T}}+f(t)e^{-2 \pi i n \frac{t}{T}}}{2} = 
    \frac{1}{T} \sum_{t=0}^{T-1} f(t)e^{-2 \pi i n \frac{t}{T}} $$
    

If we consider the 2 arrays:

$$ z_{k} = f(k)  \ \ \ \ \ \forall k \in { 0, 1, 2, ..., T-1 } $$

$$ (w_{n})_{k} = e^{-2 \pi i n \frac{k}{T}} \ \ \ \ \ \forall k \in \{ 0, 1, 2, ..., T-1 \}$$

Every complex coefficient of the Fourier Series:

$$ c_{n} \approx \vec{z} \cdot \vec{w_{n}} \in \mathbb{C} $$

The following code shows how it is implemented (a possible improvement of this code to vectorize the main for loop):
```python
self.coefs = 1j * np.zeros(2 * N + 1)
for i in range(2 * N + 1):
    n = i - N
    arguments = -2j * np.pi * n * np.arange(self.T) / self.T
    self.coefs[i] = np.dot(signal, np.exp(arguments)) / self.T
```

## Wave prediction
If we have an l-dimension array t, the predicted signal will be an l-dimension array w:
$$ args_{n}\left ( t_{k} \right ) = -2\pi i\frac{t_{k}}{T}n \ \ \ \ \ \forall k \in { 0, 1, 2, ..., l-1 } \ \ \ \forall n \in { -N, ..., -1, 0, 1, ..., N } $$






