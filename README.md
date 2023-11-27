# Fourier_Series_Graph
This week, I studied the Fourier Transform in class and decided to investigate it more. I found [the 3Blue1Brown video](https://www.youtube.com/watch?v=r6sGWTCMz2k) about the Discrete Fourier Series and I decided to implement it.

## Drawer
Drawer.

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

$$ c_{n} = \frac{1}{T} \int_{0}^{T} f(t) e^{-2 \pi i n \frac{t}{T}} dt 
= \frac{1}{T} \sum_{t=0}^{T-1} \int_{t}^{t+1} f(t) e^{-2 \pi i n \frac{t}{T}} dt $$


## Numerical methods
If we consider the approximation for a discrete function:

$$ \int_{a}^{b} f(x) dx \approx (b - a) \frac{f(a)+f(b)}{2} $$

$$ c_{n} \approx \frac{1}{T} \sum_{t=0}^{T-1} \frac{f(t+1)e^{-2 \pi i n \frac{t+1}{T}}+f(t)e^{-2 \pi i n \frac{t}{T}}}{2} = 
    \frac{1}{T} \sum_{t=0}^{T-1} f(t)e^{-2 \pi i n \frac{t}{T}} $$
    

If we consider the 2 arrays:

$$ f(k) = z_{k} \ \ \ \ \ \forall k \in { 0, 1, 2, ..., T-1 } $$

$$ (w_{n})_{k} = e^{-2 \pi i n \frac{k}{T}} \ \ \ \ \ \forall k \in \{ 0, 1, 2, ..., T-1 \}$$

Every complex coefficient of the Fourier Series:

$$ c_{n} \approx \vec{z} \cdot \vec{w_{n}} \in \mathbb{C} $$


## Wave prediction







