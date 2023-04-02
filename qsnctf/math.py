import sympy  # 解方程需要


def gcd(a, b):
    """
    求最大公约数
    """
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """
    求最小公倍数
    """
    return a * b // gcd(a, b)


def Solving_equations1(eq_str):
    """
    解方程，需要用Python的数学方式传入方程表达式
    注意：需要用x设置未知数
    """
    x = sympy.symbols('x')
    lhs_str, rhs_str = eq_str.split("=")
    lhs_expr = sympy.sympify(lhs_str.strip())
    rhs_expr = sympy.sympify(rhs_str.strip())
    eq = sympy.Eq(lhs_expr, rhs_expr)
    solution = sympy.solve(eq, sympy.Symbol('x'))
    return solution[0]


def Solving_equations2(eq_str1, eq_str2):
    """
    解方程，需要用Python的数学方式传入方程表达式(两个方程组，也就是二元一次)
    注意：需要用x和y设置未知数
    """
    x, y = sympy.symbols('x y')
    lhs_str1, rhs_str1 = eq_str1.split("=")
    lhs_str2, rhs_str2 = eq_str2.split("=")
    lhs_expr1 = sympy.sympify(lhs_str1.strip())
    rhs_expr1 = sympy.sympify(rhs_str1.strip())
    lhs_expr2 = sympy.sympify(lhs_str2.strip())
    rhs_expr2 = sympy.sympify(rhs_str2.strip())
    eq1 = sympy.Eq(lhs_expr1, rhs_expr1)
    eq2 = sympy.Eq(lhs_expr2, rhs_expr2)
    solution = sympy.solve((eq1, eq2), (x, y))
    # Print the solution
    return solution


def calculate_discounted_value(future_value, growth_rate):
    """
    基期计算 基期量=现期量/（1+增长率）
    """
    current_value = future_value / (1 + growth_rate)
    return str(current_value)
