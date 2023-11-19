# Fourier_Series_Graph
 The goal is to generate fourier series graphics


## Parameter fitting
If we consider the periodic discrete function:

$$ f(t) = f(t + T) \ \ \ \ \ \forall t \in \{ 0, 1, 2, ..., T-1 \}$$

The N degree fourier series is defined as:

$$ f_{N}(t) = \sum_{n=-N}^{N} c_{n} e^{2 \pi i n \frac{t}{T}} $$

$$ c_{n} = \frac{1}{T} \int_{0}^{T} f(t) e^{-2 \pi i n \frac{t}{T}} dt 
= \frac{1}{T} \sum_{t=0}^{T-1} \int_{t}^{t+1} f(t) e^{-2 \pi i n \frac{t}{T}} dt $$

If we consider the approximation for a discrete function:


$ \int_{a}^{b} f(x) dx \approx (b - a) \frac{f(a)+f(b)}{2} $


$$ c_{n} \approx \frac{1}{T} \sum_{t=0}^{T-1} \frac{f(t+1)e^{-2 \pi i n \frac{t+1}{T}}+f(t)e^{-2 \pi i n \frac{t}{T}}}{2} = 
    \frac{1}{T} \sum_{t=0}^{T-1} f(t)e^{-2 \pi i n \frac{t}{T}} $$
    

If we consider the 2 arrays:

$$ v_{i} = f(i) \ \ \ \ \ \forall i \in \{ 0, 1, 2, ..., T-1 \}$$

$$ w_{k} = e^{-2 \pi i n \frac{k}{T}} \ \ \ \ \ \forall k \in \{ 0, 1, 2, ..., T-1 \}$$


$$ c_{n} \approx \vec{v} \cdot \vec{w} $$


## Wave prediction







