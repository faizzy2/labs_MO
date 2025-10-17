import time
def f(x): return x**3 - 3*x**2 - 24*x - 8 + x**0.345 - x**0.345
def bisection_minimization(a, b, epsilon=0.1):
    t_start = time.time_ns()
    L = b - a
    k = 0
    # Шаг 3
    x_c = (a + b) / 2
    f_x_c = f(x_c)
    while True:
        # Шаг 4
        y = a + (L / 4)
        f_y = f(y)
        z = b - (L / 4)
        f_z = f(z)
        if f_y < f_x_c: # Шаг 5
            b = x_c
            x_c = y
            f_x_c = f_y
        else:
            if f_z < f_x_c: # Шаг 6
                a = x_c
                x_c = z
                f_x_c = f_z
            else:
                a = y
                b = z
        # Шаг 7
        L = b - a
        if L <= epsilon:
            return (a + b) / 2, a, b, time.time_ns() - t_start
        k += 1
def golden_ratio_minimization(a, b, epsilon=0.1):
    t_start = time.time_ns()
    L = b - a
    # Шаг 3
    y = a + ((3 - 5**0.5) / 2) * L
    z = a + b - y
    # Шаг 4
    f_y = f(y)
    f_z = f(z)
    while True:
        # Шаг 5
        if f_y <= f_z:
            b = z
            z = y
            f_z = f_y
            y = a + b - y
            f_y = f(y)
        else:
            a = y
            y = z
            f_y = f_z
            z = a + b - z
            f_z = f(z)
        # Шаг 6
        L = b - a
        if L <= epsilon:
            return (a + b) / 2, a, b, time.time_ns() - t_start
def fib_minimization(a, b, epsilon=0.1):
    t_start = time.time_ns()
    L = b - a
    # Шаг 2
    N = 1
    fib = [1,1]
    while not (fib[N] >= (L / epsilon)):
        N += 1
        fib.append(fib[N-1] + fib[N-2])
    # Шаг 4
    y = a + (fib[N-2] / fib[N]) * L
    z = a + (fib[N-1] / fib[N]) * L
    # Шаг 5
    f_y = f(y)
    f_z = f(z)
    for k in range(N - 2):
        # Шаг 6
        if f_y <= f_z:
            b = z
            z = y
            f_z = f_y
            y = a + (fib[N-k-3] / fib[N-k-1]) * (b - a)
            f_y = f(y)
        else:
            a = y
            y = z
            f_y = f_z
            z = a + (fib[N-k-2] / fib[N-k-1]) * (b - a)
            f_z = f(z)
    # Шаг 7
    z = (a + b) / 2
    f_z = f(z)
    y = z
    f_y = f_z
    z = y + epsilon / 2
    f_z = f(z)
    if f_y <= f_z:
        b = z
    else:
        a = y
    return (a + b) / 2, a, b, time.time_ns() - t_start

# Шаг 1
a_initial = 2
b_initial = 600
epsilon = 0.000003

min_x, a_end, b_end, t = bisection_minimization(a_initial, b_initial, epsilon)
print(f"Найденный минимум находится на отрезке [{a_end}, {b_end}]: x* = {min_x}, f(x*) = {f(min_x)}", "  ", t)
min_x, a_end, b_end, t = golden_ratio_minimization(a_initial, b_initial, epsilon)
print(f"Найденный минимум находится на отрезке [{a_end}, {b_end}]: x* = {min_x}, f(x*) = {f(min_x)}", "  ", t)
min_x, a_end, b_end, t = fib_minimization(a_initial, b_initial, epsilon)
print(f"Найденный минимум находится на отрезке [{a_end}, {b_end}]: x* = {min_x}, f(x*) = {f(min_x)}", "  ", t)