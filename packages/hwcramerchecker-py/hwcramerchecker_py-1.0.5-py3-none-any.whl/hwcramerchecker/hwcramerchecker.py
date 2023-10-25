import nbformat
from nbconvert import PythonExporter
import numpy as np
import pandas as pd
import time
import seaborn as sns
import math
import os
import nbformat
import seaborn as sns
import sys
from io import StringIO
import io
import re


def my_check_DZ_1(fil):

    checks = {
        "Task 1": lambda env: 1 if (env.get('number1') is not None and env.get('number2') is not None and isinstance(env['number1'], int) and isinstance(env['number2'], int) and env.get('num1') is not None and env['num1'] == env['number1'] + env['number2']) else 0,

        "Task 2": lambda env: 1 if (env.get('number1') is not None and env.get('number2') is not None and isinstance(env['number1'], int) and isinstance(env['number2'], int) and env.get('num2') is not None and env['num2'] == env['number1'] // env['number2']) else 0,

        "Task 3": lambda env: 1 if (env.get('number1') is not None and env.get('number2') is not None and isinstance(env['number1'], int) and isinstance(env['number2'], int) and env.get('num3') is not None and env['num3'] == env['number1'] % env['number2']) else 0,

        "Task 4": lambda env: 1 if (env.get('float_num1') is not None and env.get('float_num2') is not None and env.get('float_num3') is not None and env.get('num4') is not None and env['num4'] == env['float_num1'] * env['float_num2'] / env['float_num3']) else 0,

        "Task 5": lambda env: 1 if (env.get('num') is not None and env.get('num5') is not None and env['num5'] == round(env['num']**3 / 2, 1)) else 0,

        "Task 6": lambda env: 1 if (env.get('number1') is not None and env.get('number2') is not None and env.get('num6') is not None and env['num6'] == math.floor(env['number1'] - env['number2'])) else 0,

        "Task 7": lambda env: 1 if (env.get('number1') is not None and env.get('number2') is not None and env.get('num7') is not None and env['num7'] == math.ceil(env['number1'] - env['number2'])) else 0,

        "Task 8": lambda env: 1 if (env.get('a') is not None and env.get('b') is not None and env.get('num8') is not None and round(env['num8'], 1) in [round((env['a']**2 + env['b']**2)**.5, 1), round((env['a']**2 + env['b']**2)**.25, 1)]) else 0,

        "Task 9": lambda env: 1 if (env.get('pos_num') is not None and env.get('neg_num') is not None and env.get('num9') is not None and round(env['num9'], 1) in [round(abs(env['pos_num']) + abs(env['neg_num']), 1)]) else 0,

        "Task 10": lambda env: 1 if (env.get('temp') is not None and env.get('num10') is not None and round(5/9*(env['temp']-32), 2) == env['num10']) else 0,

        "Task 11": lambda env: 1 if (env.get('num11') is not None and round(((6 + 7/12 - 3 - 17/36)*2.5 - (4+1/3)/.65) / (16-.5), 5) == round(env['num11'], 5)) else 0,

        "Task 12": lambda env: 1 if (env.get('num12') is not None and round((11/4/1.1 + 3 + 1/3)/(2.5 - .4*10/3)/(5/7) - ((13/6+4.5)*.375)/(2.75-3/2), 3) == round(env['num12'], 3)) else 0,

        "Task 13": lambda env: 1 if (env.get('num13') is not None and round(11+ 2/5 + 15/2*(285.6/14 - 1-23/30 + 13/50)/(24.4 - 10.23), 3) == round(env['num13'], 3)) else 0,

        "Task 14": lambda env: 1 if (env.get('num14') is not None and round(((9-5-3/8)*(4+5/12 - 4/(2+2/3)) + (.3 - .5/4)*4/7) / (1/24 + .25/(40/3)), 3) == round(env['num14'], 3)) else 0,

        "Task 15": lambda env: 1 if (env.get('num15') is not None and round(5.75/.025) == round(env['num15'], 3)) else 0,

        "Task 16": lambda env: 1 if (env.get('num16') is not None and round(((.16*(3.2 - 3/40) + 25/11 * 4.125 / (3+3/4)) / (31/6*.3 - .3*4.5 + .3/3))*.4, 3) == round(env['num16'], 3)) else 0,

    }

    with open(fil, 'r', encoding='utf-8') as file:
        hw = nbformat.read(file, nbformat.NO_CONVERT)
        student_check = {}
        for row in hw.cells:
            if row.cell_type == 'markdown':
                if 'Task' in row['source'].split('\n')[0].replace('# ', ''):
                    task = row['source'].split('\n')[0].replace('# ', '')
                    student_check[task] = []
                else:
                    continue
            elif row.cell_type == 'code':
                student_check[task].append(row.source)

    student_result = []
    for task, codes in student_check.items():
        environment = {}
        for code in codes:
            environment = {"math": math, 'mt': math, 'ceil': math.ceil, 'sqrt': math.sqrt, 'floor': math.floor}
            try:
                exec(code, environment)
            except Exception as e:
                print(f"Ошибка при выполнении кода для {task}: {e}")

        try:
            checker = checks.get(task, lambda env: 0)
            student_result.append(checker(environment))
        except Exception:
            student_result.append(0)
    print(fil)
    print()
    return pd.Series(student_result, index=['Task_'+str(i) for i in range(1, 17)])


def my_check_DZ_2(file_):

    variables=['number', 'mark', 'x', 'y', 'z', 'a', 'b', 'c', ]

    def reformat_code(code, variables):
        # Для одиночного присваивания:
        single_var_pattern = r'^([a-zA-Z_][a-zA-Z0-9_]*)\s*='
        
        # Для множественного присваивания:
        multi_var_pattern = r'^(([a-zA-Z_][a-zA-Z0-9_]*\s*,\s*)+[a-zA-Z_][a-zA-Z0-9_]*)\s*='

        lines = code.split("\n")
        for i, line in enumerate(lines):
            # Если это одиночное присваивание:
            match = re.match(single_var_pattern, line.strip())
            if match:
                var_name = match.group(1)
                if var_name in variables:
                    lines[i] = f'{var_name} = int(input())'
                    continue

            # Если это множественное присваивание:
            match = re.match(multi_var_pattern, line.strip())
            if match:
                var_names = [var.strip() for var in match.group(1).split(',')]
                if all(var in variables for var in var_names):
                    left_side = ', '.join(var_names)
                    right_side = ', '.join(['int(input())'] * len(var_names))
                    lines[i] = f'{left_side} = {right_side}'
                    continue

        return '\n'.join(lines)


    with open(file_, 'r', encoding='utf-8') as file:
            hw = nbformat.read(file, nbformat.NO_CONVERT)
            dict_ = {}
            for row in hw.cells:
                if row.cell_type == 'markdown':
                    if 'Task' in row['source'].split('\n')[0].replace('# ', ''):
                        task = row['source'].split('\n')[0].replace('# ', '')
                        dict_[task] = []
                    else:
                        continue
                elif row.cell_type == 'code':
                    dict_[task].append(reformat_code(row.source, variables))


    def preprocess_student_code(student_code):

        # Разбиваем код студента на строки
        lines = student_code.split("\n")
        
        # Находим переменную, которую студент использует (в данном случае 'g')
        variable_name = lines[0].split('=')[0].strip()
        
        # Меняем первую строку на строку с input()
        lines[0] = f"{variable_name} = int(input())"
        
        # Собираем код обратно в единую строку
        modified_code = "\n".join(lines)
        
        return modified_code

    def run_student_code(student_code, input_values):
        # Создаем итератор из значений ввода
        input_iter = iter(input_values.splitlines())
        
        # Переопределение функции input()
        def mock_input(*args):
            # Каждый раз, когда вызывается mock_input, он возвращает следующее значение из input_values
            return next(input_iter)

        # Создание временного буфера для перехвата вывода
        buffer = io.StringIO()
        original_input = __builtins__.input
        original_stdout = sys.stdout

        __builtins__.input = mock_input
        sys.stdout = buffer

        try:
            for row in student_code:
                exec(row)
            return buffer.getvalue().strip()
        except Exception as e:
            return f"Error: {e}"
        finally:
            # Возвращение функции input() и sys.stdout к оригинальным значениям
            __builtins__.input = original_input
            sys.stdout = original_stdout



    def check_task_1(student_code):
        test_values = ["10", "-5"]
        
        results = []
        outputs = []

        for test_value in test_values:
            # Запускаем код студента с подставленным значением для number
            output = run_student_code(student_code, test_value)
            
            # Ожидаемый результат
            expected_output = "True" if int(test_value) > 0 else "False"
            
            results.append(output == expected_output)
            outputs.append(output)

        return results, outputs

    def check_task_2(student_code):
        # Все тестовые значения
        test_values = [91, 80, 70, 60, 55]
        
        results = []
        outputs = []

        for mark in test_values:
            # Определение ожидаемого результата на основе ввода
            if mark >= 90:
                expected_output = "Отлично, Ваша оценка 5!"
            elif 80 <= mark < 90:
                expected_output = "Здорово, Ваша оценка 4!"
            elif 70 <= mark < 80:
                expected_output = "Хорошо, Ваша оценка 3!"
            elif 60 <= mark < 70:
                expected_output = "Вам стоит подучить материал"
            else:
                expected_output = "Вы не сдали экзамен"
            
            # Запускаем код студента с подставленным значением для mark
            output = run_student_code(student_code, str(mark))
            
            results.append(output == expected_output)
            outputs.append(output)

        return results, outputs

    def check_task_3(student_code):
        test_sets = [
            ('1', '2', '3'),
            ("-1", "0", "1"),
            ("100", "10", "1"),
            ("-5", "-6", "-7"),
            ("0", "0", "0")
        ]

        results = []
        outputs = []

        for x, y, z in test_sets:
            # Определение ожидаемого минимального значения
            x, y, z = int(x), int(y), int(z) # Преобразовываем строки обратно в числа
            if x <= y and x <= z:
                expected_output = str(x)
            elif y <= x and y <= z:
                expected_output = str(y)
            else:
                expected_output = str(z)
            
            # Подставляем значения для input и выполняем код студента
            input_data = f"{x}\n{y}\n{z}\n"
            output = run_student_code(student_code, input_data)
            
            results.append(output.strip() == expected_output)
            outputs.append(output)

        return results, outputs

    def check_task_4(student_code):
        test_sets = [
            (10, 2),   # Делится без остатка, ожидаемый результат 5
            (15, 4),   # Не делится, ожидаемый результат 19
            (6, 3),    # Делится без остатка, ожидаемый результат 2
            (7, 5),    # Не делится, ожидаемый результат 12
        ]

        results = []
        outputs = []

        for x, y in test_sets:
            # Определение ожидаемого результата
            if x % y == 0:
                expected_output = str(x / y)
            else:
                expected_output = str(x + y)
            
            # Подставляем значения для input и выполняем код студента
            input_data = f"{x}\n{y}\n"
            output = run_student_code(student_code, input_data)
            
            results.append(output.strip() == expected_output)
            outputs.append(output)

        return results, outputs

    def check_task_5(student_code):
        test_sets = [
            (3, 4, 5),   # Может существовать, ожидаемый результат "yes"
            (1, 2, 4),   # Не может существовать, ожидаемый результат "no"
            (10, 6, 5),  # Может существовать, ожидаемый результат "yes"
            (10, 6, 17), # Не может существовать, ожидаемый результат "no"
        ]

        results = []
        outputs = []

        for a, b, c in test_sets:
            # Определение ожидаемого результата
            if (a + b > c) and (a + c > b) and (b + c > a):
                expected_output = "yes"
            else:
                expected_output = "no"
            
            # Подставляем значения для input и выполняем код студента
            input_data = f"{a}\n{b}\n{c}\n"
            output = run_student_code(student_code, input_data)
            
            results.append(output.strip() == expected_output)
            outputs.append(output)

        return results, outputs


    def check_task_6(student_code):
        test_sets = [
            (10, 20, 30),   # True
            (15, 25, 45),   # False
            (30, 40, 70),   # True
            (15, 45, 50),   # False
        ]

        results = []
        outputs = []

        for a, b, c in test_sets:
            # Определение ожидаемого результата
            expected_output = str(a + b == c)
            
            # Подставляем значения для input и выполняем код студента
            input_data = f"{a}\n{b}\n{c}\n"
            output = run_student_code(student_code, input_data)
            
            results.append(output.strip().lower() == expected_output.lower())
            outputs.append(output)

        return results, outputs

    def check_task_7(student_code):
        student_code[0] = preprocess_student_code(student_code[0])
        test_values = [
            2,      # True
            5,      # True
            9,    # True
            10,     # False
            15,    # False
            11      # False
        ]

        results = []
        outputs = []

        for value in test_values:
            # Определение ожидаемого результата
            expected_output = "True" if 2 <= value < 10 else "False"
            
            # Запускаем код студента с подставленным значением
            output = run_student_code(student_code, str(value))
            
            results.append(output.strip().lower() == expected_output.lower())
            outputs.append(output)

        return results, outputs

    def check_task_8(student_code):
        student_code[0] = preprocess_student_code(student_code[0])
        test_values = [
            2,      # True
            5,      # True
            9,    # True
            10,     # False
            15,    # False
            11      # False
        ]

        results = []
        outputs = []

        for value in test_values:
            # Определение ожидаемого результата
            expected_output = "True" if (value<4) or (value >=5) else "False"
            
            # Запускаем код студента с подставленным значением
            output = run_student_code(student_code, str(value))
            
            results.append(output.strip().lower() == expected_output.lower())
            outputs.append(output)

        return results, outputs


    def check_task_9(student_code):
        student_code[0] = preprocess_student_code(student_code[0])
        test_values = [
            2,      # True
            5,      # True
            9,    # True
            10,     # False
            15,    # False
            11      # False
        ]

        results = []
        outputs = []

        for value in test_values:
            # Определение ожидаемого результата
            expected_output = "True" if value in [2, 4, 6, 8, 10] else "False"
            
            # Запускаем код студента с подставленным значением
            output = run_student_code(student_code, str(value))
            
            results.append(output.strip().lower() == expected_output.lower())
            outputs.append(output)

        return results, outputs


    def check_task_10(student_code):
        student_code[0] = preprocess_student_code(student_code[0])
        test_values = [
            -20,      # True
            -5,      # True
            5,    # True
            7,     # False
            8,    # False
            11      # False
        ]

        results = []
        outputs = []

        for value in test_values:
            # Определение ожидаемого результата
            expected_output = "True" if (-10<value<5) or (5<value<=7) or (value>8) else "False"
            
            # Запускаем код студента с подставленным значением
            output = run_student_code(student_code, str(value))
            
            results.append(output.strip().lower() == expected_output.lower())
            outputs.append(output)

        return results, outputs

    def check_task_11(student_code):
        student_code[0] = preprocess_student_code(student_code[0])
        test_values = [
            -20,      # True      # True
            5,    # Tru     # False
            8,    # False
            11      # False
        ]

        results = []
        outputs = []

        for value in test_values:
            # Определение ожидаемого результата
            expected_output = "True" if ((value**2 - 3*value)/(value+5)) >= ((value-3)/(7-value)) else "False"
            
            # Запускаем код студента с подставленным значением
            output = run_student_code(student_code, str(value))
            
            results.append(output.strip().lower() == expected_output.lower())
            outputs.append(output)

        return results, outputs

    def check_task_12(student_code):
        student_code[0] = preprocess_student_code(student_code[0])
        test_values = [
            -20,
            1,# True      # True
            5,    # Tru     # False
            8,    # False
            11      # False
        ]

        results = []
        outputs = []

        for value in test_values:
            # Определение ожидаемого результата
            expected_output = "True" if (value**2 - 3*value) <=0 and (value**2 -6*value + 8)>0 else "False"
            
            # Запускаем код студента с подставленным значением
            output = run_student_code(student_code, str(value))
            
            results.append(output.strip().lower() == expected_output.lower())
            outputs.append(output)

        return results, outputs

    def check_task_13(student_code):
        student_code[0] = preprocess_student_code(student_code[0])
        test_values = [
            -20,
            1,# True      # True
            5,    # Tru     # False
            8,    # False
            11      # False
        ]

        results = []
        outputs = []

        for value in test_values:
            # Определение ожидаемого результата
            expected_output = "True" if (value -3) > 5 or value<=2 else "False"
            
            # Запускаем код студента с подставленным значением
            output = run_student_code(student_code, str(value))
            
            results.append(output.strip().lower() == expected_output.lower())
            outputs.append(output)

        return results, outputs



    result1, output1 = check_task_1(dict_['Task 1'])
    print("Task 1 - Is correct?", result1)
    print("Task 1 - Output:", output1)

    result2, output2 = check_task_2(dict_['Task 2'])
    print("Task 2 - Is correct?", result2)
    print("Task 2 - Output:", output2)

    result3, output3 = check_task_3(dict_['Task 3'])
    print("Task 3 - Is correct?", result3)
    print("Task 3 - Output:", output3)

    result4, output4 = check_task_4(dict_['Task 4'])
    print("Task 4 - Is correct?", result4)
    print("Task 4 - Output:", output4)

    result5, output5 = check_task_5(dict_['Task 5'])
    print("Task 5 - Is correct?", result5)
    print("Task 5 - Output:", output5)

    result6, output6 = check_task_6(dict_['Task 6'])
    print("Task 6 - Is correct?", result6)
    print("Task 6 - Output:", output6)

    result7, output7 = check_task_7(dict_['Task 7'])
    print("Task 7 - Is correct?", result7)
    print("Task 7 - Output:", output7)

    result8, output8 = check_task_8(dict_['Task 8'])
    print("Task 8 - Is correct?", result8)
    print("Task 8 - Output:", output8)

    result9, output9 = check_task_9(dict_['Task 9'])
    print("Task 9 - Is correct?", result9)
    print("Task 9 - Output:", output9)

    result10, output10 = check_task_10(dict_['Task 10'])
    print("Task 10 - Is correct?", result10)
    print("Task 10 - Output:", output10)

    result11, output11 = check_task_11(dict_['Task 11'])
    print("Task 11 - Is correct?", result11)
    print("Task 11 - Output:", output11)

    result12, output12 = check_task_12(dict_['Task 12'])
    print("Task 12 - Is correct?", result12)
    print("Task 12 - Output:", output12)

    result13, output13 = check_task_13(dict_['Task 13'])
    print("Task 13 - Is correct?", result13)
    print("Task 13 - Output:", output13)
    print()
    print('YOUR FINAL REASULT', '\n')
    print('Task_1:', np.array(result1).all())
    print('Task_2:', np.array(result2).all())
    print('Task_3:', np.array(result3).all())
    print('Task_4:', np.array(result4).all())
    print('Task_5:', np.array(result5).all())
    print('Task_6:', np.array(result6).all())
    print('Task_7:', np.array(result7).all())
    print('Task_8:', np.array(result8).all())
    print('Task_9:', np.array(result9).all())
    print('Task_10:', np.array(result10).all())
    print('Task_11:', np.array(result11).all())
    print('Task_12:', np.array(result12).all())
    print('Task_13:', np.array(result13).all())











        