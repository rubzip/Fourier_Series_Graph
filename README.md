# Fourier_Series_Graph
This week, I studied the Fourier Transform in class and decided to investigate it more. I found [the 3Blue1Brown video](https://www.youtube.com/watch?v=r6sGWTCMz2k) about the Discrete Fourier Series and I decided to implement it.

## Drawer
The drawer application was implemented from scratch only using Tkinter. With it, you can create a drawing without lifting the pencil, and get the list of dots as a `.tsv` file.

### How to Use:
1. Run the Python code `.py`.
2. Left-click and drag on the canvas to draw lines.
3. Right-click to delete the drawing.
4. Use 'z' to undo the last movement, 'Up' and 'Down' arrows to adjust line width, 's' to save the drawing, 'x' to close the program, and 'h' to display help information.


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

$$ f(k) = z_{k} \ \ \ \ \ \forall k \in { 0, 1, 2, ..., T-1 } $$

$$ (w_{n})_{k} = e^{-2 \pi i n \frac{k}{T}} \ \ \ \ \ \forall k \in \{ 0, 1, 2, ..., T-1 \}$$

Every complex coefficient of the Fourier Series:

$$ c_{n} \approx \vec{z} \cdot \vec{w_{n}} \in \mathbb{C} $$

This is implemented, as a possible improvement to this code to vectorize the main for loop:
```python
self.coefs = 1j * np.zeros(2 * N + 1)
for i in range(2 * N + 1):
    n = i - N
    arguments = -2j * np.pi * n * np.arange(self.T) / self.T
    self.coefs[i] = np.dot(signal, np.exp(arguments)) / self.T
```

## Wave prediction







