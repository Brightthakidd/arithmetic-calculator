def arithmetic_arranger(problems, show_result=False):
    if len(problems) > 8:
        return "Error: Too many problems."

    arranged_problems = []
    for problem in problems:
        num1, operator, num2 = problem.split()
        if operator not in "+-":
            return "Error: Operator must be '+' or '-'."
        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits."
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        max_len = max(len(num1), len(num2))
        arranged_problem = f"{num1:>{max_len}}\n{operator} {num2:>{max_len}}"
        line = '-' * (max_len + 2)
        result = eval(problem) if show_result else ""
        arranged_problems.append((arranged_problem, line, str(result).rjust(max_len + 2)))

    arranged = '    '.join(arranged_problems)
    if show_result:
        return arranged + '\n' + '    '.join([line for _, line, _ in arranged_problems])
    else:
        return arranged

print (arithmetic_arranger('32 + 45',True))