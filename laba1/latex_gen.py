from main import f

def bisection_latex(a, b, epsilon=0.1, precision = 3):
    latex_steps = []
    L = b - a
    k = 0
    latex_steps.append(
        f"\\textbf{{1.}} Задаем $a_0 = {a}$; $b_0 = {b}$; $\\varepsilon = {epsilon}$.")
    latex_steps.append(f"\\textbf{{2.}} Положим $k = {k}$.")
    # Шаг 3
    x_c = (a + b) / 2
    f_x_c = f(x_c)
    latex_steps.append(
        f"\\textbf{{3}}. $x_{{{k}}}^{{c}} = \\frac{{{a} + {b}}}{{2}} = {x_c:.{precision}f}$;"
        f" $L_{{{k}}} = {b} - {a} = {L:.{precision}f}$; $f(x_{{{k}}}^{{c}}) = {f_x_c:.{precision}f}$.")
    while True:
        # Шаг 4
        y = a + (L / 4)
        f_y = f(y)
        z = b - (L / 4)
        f_z = f(z)
        latex_steps.append(
            f"\\textbf{{4}}$^{{{k}}}$. $y_{{{k}}} = {a} + \\frac{{{L:.{precision}f}}}{{4}}"
            f" = {y:.{precision}f}$; $f(y_{{{k}}}) = {f_y:.{precision}f}$.")
        latex_steps.append(
            f"$z_{{{k}}} = {b} - \\frac{{{L:.{precision}f}}}{{4}}"
            f" = {z:.{precision}f}$; $f(z_{{{k}}}) = {f_z:.{precision}f}$.")

        latex_steps.append(
            f"\\textbf{{5}}$^{{{k}}}$. $f(y_{{{k}}}) = {f_y:.{precision}f}$; $f(x_{{{k}}}) = {f_x_c:.{precision}f}$.")
        if f_y < f_x_c: # Шаг 5
            latex_steps.append(
                f"$f(y_{{{k}}}) < f(x_{{{k}}}^{{c}})$: $b_{{{k + 1}}} = x_{{{k}}}"
                f" = {x_c:.{precision}f}$; $a_{{{k + 1}}} = a_{{{k}}} = {a:.{precision}f}$. Переходим к шагу 7.")
            b = x_c
            x_c = y
            f_x_c = f_y
        else:
            latex_steps.append(f"$f(y_{{{k}}}) \\nless f(x_{{{k}}})$. Переходим к шагу 6.")
            latex_steps.append(
                f"\\textbf{{6}}$^{{{k}}}$. $f(z_{{{k}}}) = {f_z:.{precision}f}$;"
                f" $f(x_{{{k}}}) = {f_x_c:.{precision}f}$.")
            if f_z < f_x_c: # Шаг 6
                latex_steps.append(
                    f"а) $f(z_{{{k}}}) < f(x_{{{k}}}^{{c}})$: $a_{{{k + 1}}} = x_{{{k}}}^{{c}}"
                    f" = {x_c:.{precision}f}$; $b_{{{k + 1}}} = b_{{{k}}} = {b:.{precision}f}$. Переходим  к шагу 7.")
                a = x_c
                x_c = z
                f_x_c = f_z
            else:
                latex_steps.append(
                    f"б) $f(z_{{{k}}}) \\geq f(x_{{{k}}}^{{c}})$: $a_{{{k + 1}}} = y_{{{k}}} = {y:.3f}$;"
                    f" $b_{{{k + 1}}} = z_{{{k}}} = {z:.{precision}f}$. Переходим к шагу 7.")
                a = y
                b = z

        # Шаг 7
        L = b - a
        latex_steps.append(
            f"\\textbf{{7}}$^{{{k}}}$. $L_{{{k + 1}}} = {b:.{precision}f} - {a:.{precision}f} = {L:.{precision}f}$.")
        if L <= epsilon:
            latex_steps.append(
                f"$L_{{{k + 1}}} \\leq \\varepsilon$: $x^* = \\frac{{{a:.{precision}f}"
                f" + {b:.{precision}f}}}{{2}} = {(a+b)/2:.{precision}f}; f(x^*) = {{{f((a+b)/2):.{precision}f}}}$.")
            latex_code = "\\begin{enumerate}[label={}, left=0pt, itemindent=0pt, itemsep=3pt, topsep=5pt]\n"
            for step in latex_steps:
                if step.startswith("\\textbf{"):
                    latex_code += "  \\item " + step + "\n"
                else:
                    latex_code += "  \\item[] " + step + "\n"
            latex_code += "\\end{enumerate}"
            return latex_code
        latex_steps.append(
            f"$L_{{{k + 1}}} > \\varepsilon$: $k = {k + 1}$. Переходим к шагу 4.")
        k += 1
def golden_ratio_latex(a, b, epsilon=0.1, precision = 3):
    latex_steps = []
    L = b - a
    latex_steps.append(
        f"\\textbf{{1.}} Задаем $a_0 = {a:.{precision}f}$; $b_0 = {b}$; $\\varepsilon = {epsilon}$.")
    latex_steps.append(f"\\textbf{{2.}} Положим $k = {k}$.")
    # Шаг 3
    y = a + ((3 - 5**0.5) / 2) * L
    z = a + b - y
    latex_steps.append(f"\\textbf{{3.}} $y_{{0}} = {a} + \\frac{{3 - \\sqrt{{5}}}}{{2}} * (b_{{0}} - a_{{0}})$;"
                       f" z_{{0}} = a")
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