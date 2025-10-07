import numpy as np
import matplotlib.pyplot as plt
from functools import lru_cache
def f(x): return x**3 - 3*x**2 - 24*x - 8
def visualise_dichotomy(iterations, a_end, b_end, min_x):
    """Визуализация итераций метода половинного деления"""
    for i in range(len(iterations) - 1):
        a_prev, b_prev, x1_prev, x2_prev, x3_prev, f1_prev, f2_prev, f3_prev = iterations[i]
        a, b, x1, x2, x3, f1, f2, f3 = iterations[i + 1]
        # График функции
        x = np.linspace(a_prev, b_prev, 1000)
        y = f(x)
        fig, ax = plt.subplots(figsize=(13, 7))
        ax.plot(x, y, 'k-', label='f(x)')

        # Контрольные точки
        ax.plot(x1_prev, f1_prev, 'ro', markersize=6, label=f'y{i} = {x1_prev:.2f}, f(y{i}) = {f1_prev:.2f}')
        ax.plot(x2_prev, f2_prev, 'go', markersize=6, label=f'x_c{i} = {x2_prev:.2f}, f(x_c{i}) = {f2_prev:.2f}')
        ax.plot(x3_prev, f3_prev, 'bo', markersize=6, label=f'z{i} = {x3_prev:.2f}, f(z{i}) = {f3_prev:.2f}')

        # Закраска интервалов
        x_fill_prev = np.linspace(a_prev, b_prev, 1000)
        y_fill_prev = f(x_fill_prev)
        ax.fill_between(x_fill_prev, y_fill_prev, y_fill_prev + (max(f(a_prev), f(b_prev)) - f(min_x)) / 10, alpha=0.2, color='red', label='Текущий интервал')

        x_fill_next = np.linspace(a, b, 1000)
        y_fill_next = f(x_fill_next)
        ax.fill_between(x_fill_next, y_fill_next, y_fill_next + (max(f(a_prev), f(b_prev)) - f(min_x)) / 10, alpha=0.3, color='green', label='Следующий интервал')

        ax.set_xlabel('x')
        ax.set_ylabel('f(x)')
        ax.set_title(f'Итерация {i+1}\nТекущий интервал: [{a_prev:.2f}, {b_prev:.2f}]\nСледующий интервал: [{a:.2f}, {b:.2f}]')
        ax.legend(loc='upper right')
        ax.grid(True)
        plt.show()

    # Финальный график
    x = np.linspace(a_initial - 1, b_initial + 1, 100000)
    y = f(x)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x, y, 'k-', label='f(x)')

    # Вертикальные линии и закраска для конечного интервала
    ax.axvline(a_end, color='g', linestyle='--', label=f'a{len(iterations)} = {a_end:.2f}')
    ax.axvline(b_end, color='g', linestyle='--', label=f'b{len(iterations)} = {b_end:.2f}')
    ax.plot(min_x, f(min_x), 'go', markersize=6, label=f'x* = {min_x:.2f}, f(x*) = {f(min_x):.2f}')

    x_fill_end = np.linspace(a_end, b_end, 1000)
    y_fill_end = f(x_fill_end)
    ax.fill_between(x_fill_end, y_fill_end, y_fill_end + (max(f(a_end), f(b_end)) - f(min_x)) / 10, alpha=0.3, color='green', label='Конечный интервал')

    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.set_title(f'Итерация {len(iterations)}\nКонечный интервал: [{a_end:.2f}, {b_end:.2f}]')
    ax.legend(loc='upper right')
    ax.grid(True)
    plt.show()
def visualise_golden(iterations, a_end, b_end, min_x):
    """Визуализация итераций метода золотого сечения"""
    for i in range(len(iterations) - 1):
        a_prev, b_prev, x1_prev, x2_prev, f1_prev, f2_prev = iterations[i]
        a, b, x1, x2, f1, f2 = iterations[i + 1]
        # График функции
        x = np.linspace(a_prev, b_prev, 1000)
        y = f(x)
        fig, ax = plt.subplots(figsize=(13, 7))
        ax.plot(x, y, 'k-', label='f(x)')

        # Контрольные точки
        ax.plot(x1_prev, f1_prev, 'ro', markersize=6, label=f'y{i} = {x1_prev:.2f}, f(y{i}) = {f1_prev:.2f}')
        ax.plot(x2_prev, f2_prev, 'go', markersize=6, label=f'z{i} = {x2_prev:.2f}, f(z{i}) = {f2_prev:.2f}')

        # Закраска интервалов
        x_fill_prev = np.linspace(a_prev, b_prev, 1000)
        y_fill_prev = f(x_fill_prev)
        ax.fill_between(x_fill_prev, y_fill_prev, y_fill_prev + (max(f(a_prev), f(b_prev)) - f(min_x)) / 10, alpha=0.2, color='red', label='Текущий интервал')

        x_fill_next = np.linspace(a, b, 1000)
        y_fill_next = f(x_fill_next)
        ax.fill_between(x_fill_next, y_fill_next, y_fill_next + (max(f(a_prev), f(b_prev)) - f(min_x)) / 10, alpha=0.3, color='green', label='Следующий интервал')

        ax.set_xlabel('x')
        ax.set_ylabel('f(x)')
        ax.set_title(f'Итерация {i+1}\nТекущий интервал: [{a_prev:.2f}, {b_prev:.2f}]\nСледующий интервал: [{a:.2f}, {b:.2f}]')
        ax.legend(loc='upper right')
        ax.grid(True)
        plt.show()

    # Финальный график
    x = np.linspace(a_initial - 1, b_initial + 1, 100000)
    y = f(x)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x, y, 'k-', label='f(x)')

    # Вертикальные линии и закраска для конечного интервала
    ax.axvline(a_end, color='g', linestyle='--', label=f'a{len(iterations)} = {a_end:.2f}')
    ax.axvline(b_end, color='g', linestyle='--', label=f'b{len(iterations)} = {b_end:.2f}')
    ax.plot(min_x, f(min_x), 'go', markersize=6, label=f'x* = {min_x:.2f}, f(x*) = {f(min_x):.2f}')

    x_fill_end = np.linspace(a_end, b_end, 1000)
    y_fill_end = f(x_fill_end)
    ax.fill_between(x_fill_end, y_fill_end, y_fill_end + (max(f(a_end), f(b_end)) - f(min_x)) / 10, alpha=0.3, color='green', label='Конечный интервал')

    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.set_title(f'Итерация {len(iterations)}\nКонечный интервал: [{a_end:.2f}, {b_end:.2f}]')
    ax.legend(loc='upper right')
    ax.grid(True)
    plt.show()

def dichotomy_minimization(a, b, epsilon=0.1, precision = 3):
    iterations = []
    latex_steps = []
    L = b - a
    k = 0
    # Начальные шаги
    latex_steps.append(
        f"\\textbf{{1.}} Задаем $a_0 = {a}$; $b_0 = {b}$; $\\varepsilon = {epsilon}$.")
    latex_steps.append(f"\\textbf{{2.}} Положим $k = {k}$.")
    # Шаг 3
    x_c = (a + b) / 2
    f_x_c = f(x_c)
    latex_steps.append(
        f"\\textbf{{3}}. $x_{{{k}}}^{{c}} = \\frac{{{a} + {b}}}{{2}} = {x_c:.{precision}f}$; $L_{{{k}}} = {b} - {a} = {L:.{precision}f}$; $f(x_{{{k}}}^{{c}}) = {f_x_c:.{precision}f}$.")
    while True:
        # Шаг 4
        y = a + (L / 4)
        f_y = f(y)
        z = b - (L / 4)
        f_z = f(z)
        latex_steps.append(
            f"\\textbf{{4}}$^{{{k}}}$. $y_{{{k}}} = {a} + \\frac{{{L:.{precision}f}}}{{4}} = {y:.{precision}f}$; $f(y_{{{k}}}) = {f_y:.{precision}f}$.")
        latex_steps.append(
            f"$z_{{{k}}} = {b} - \\frac{{{L:.{precision}f}}}{{4}} = {z:.{precision}f}$; $f(z_{{{k}}}) = {f_z:.{precision}f}$.")
        # Сохраняем данные итерации для визуализации
        iterations.append((a, b, y, x_c, z, f_y, f_x_c, f_z))

        latex_steps.append(
            f"\\textbf{{5}}$^{{{k}}}$. $f(y_{{{k}}}) = {f_y:.{precision}f}$; $f(x_{{{k}}}) = {f_x_c:.{precision}f}$.")
        if f_y < f_x_c: # Шаг 5
            latex_steps.append(
                f"$f(y_{{{k}}}) < f(x_{{{k}}}^{{c}})$: $b_{{{k + 1}}} = x_{{{k}}} = {x_c:.{precision}f}$; $a_{{{k + 1}}} = a_{{{k}}} = {a:.{precision}f}$. Переходим к шагу 7.")
            b = x_c
            x_c = y
            f_x_c = f_y
        else:
            latex_steps.append(f"$f(y_{{{k}}}) \\nleq f(x_{{{k}}})$. Переходим к шагу 6.")
            latex_steps.append(
                f"\\textbf{{6}}$^{{{k}}}$. $f(z_{{{k}}}) = {f_z:.{precision}f}$; $f(x_{{{k}}}) = {f_x_c:.{precision}f}$.")
            if f_z < f_x_c: # Шаг 6
                latex_steps.append(
                    f"а) $f(z_{{{k}}}) < f(x_{{{k}}}^{{c}})$: $a_{{{k + 1}}} = x_{{{k}}}^{{c}} = {x_c:.{precision}f}$; $b_{{{k + 1}}} = b_{{{k}}} = {b:.{precision}f}$. Переходим  к шагу 7.")
                a = x_c
                x_c = z
                f_x_c = f_z
            else:
                latex_steps.append(
                    f"б) $f(z_{{{k}}}) \\geq f(x_{{{k}}}^{{c}})$: $a_{{{k + 1}}} = y_{{{k}}} = {y:.3f}$; $b_{{{k + 1}}} = z_{{{k}}} = {z:.{precision}f}$. Переходим к шагу 7.")
                a = y
                b = z

        # Шаг 7
        L = b - a
        latex_steps.append(
            f"\\textbf{{7}}$^{{{k}}}$. $L_{{{k + 1}}} = {b:.{precision}f} - {a:.{precision}f} = {L:.{precision}f}$.")
        if L <= epsilon:
            latex_steps.append(
                f"$L_{{{k + 1}}} \\leq \\varepsilon$: $x^* = \\frac{{{a:.{precision}f} + {b:.{precision}f}}}{{2}} = {(a+b)/2:.{precision}f}$.")
            # Возвращаем середину конечного интервала и данные итераций

            latex_code = "\\begin{enumerate}[label={}, left=0pt, itemindent=0pt, itemsep=3pt, topsep=5pt]\n"
            for step in latex_steps:
                if step.startswith("\\textbf{"):
                    latex_code += "  \\item " + step + "\n"
                else:
                    latex_code += "  \\item[] " + step + "\n"
            latex_code += "\\end{enumerate}"
            return (a + b) / 2, iterations, a, b, latex_code
        latex_steps.append(
            f"$L_{{{k + 1}}} > \\varepsilon$: $k = {k + 1}$. Переходим к шагу 4.")
        k += 1

def golden_ratio_minimization(a, b, epsilon=0.1):
    iterations = []
    L = b - a

    # Шаг 3
    y = a + ((3 - 5**0.5) / 2) * L
    z = a + b - y

    # Шаг 4
    f_y = f(y)
    f_z = f(z)
    while True:
        # Сохраняем данные итерации для визуализации
        iterations.append((a, b, y, z, f_y, f_z))

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
            # Возвращаем середину конечного интервала и данные итераций
            return (a + b) / 2, iterations, a, b
@lru_cache(maxsize=128)
def fibonacci(n):
    if n <= 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
def fib_minimization(a, b, epsilon=0.1):
    # Сохраняем данные итерации для визуализации
    iterations = []
    L = b - a

    # Шаг 2
    N = 1
    fib = fibonacci(N)
    while not (fib >= (L / epsilon)):
        N += 1
        fib = fibonacci(N)

    # Шаг 4
    y = a + (fibonacci(N - 2) / fibonacci(N)) * L
    z = a + (fibonacci(N - 1) / fibonacci(N)) * L
    # Шаг 5
    f_y = f(y)
    f_z = f(z)
    while True:
        iterations.append((a, b, y, z, f_y, f_z))


# Шаг 1
a_initial = 3
b_initial = 6
epsilon = 0.3

# Запуск оптимизации
min_x, iterations, a_end, b_end, latex = dichotomy_minimization(a_initial, b_initial, epsilon)
visualise_dichotomy(iterations, a_end, b_end, min_x)
print(latex)
"""
print(f"Найденный минимум находится на отрезке [{a_end}, {b_end}]: x* = {min_x:.3f}, f(x*) = {f(min_x):.3f}")
min_x, iterations, a_end, b_end = golden_ratio_minimization(a_initial, b_initial, epsilon)
visualise_golden(iterations, a_end, b_end, min_x)
print(f"Найденный минимум находится на отрезке [{a_end}, {b_end}]: x* = {min_x:.3f}, f(x*) = {f(min_x):.3f}")
fib_minimization(a_initial, b_initial, epsilon)"""
