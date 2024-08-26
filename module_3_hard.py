def calculate_structure_sum(*args):
    sum_structure = 0
    for arg in args:
        if isinstance(arg, (int, float)):
            sum_structure += arg
        elif isinstance(arg, str):
            sum_structure += len(arg)
        elif isinstance(arg, (set, list, tuple)):
            sum_structure += calculate_structure_sum(*arg)
        elif isinstance(arg, dict):
            sum_structure += calculate_structure_sum(*arg.items())

    return sum_structure


data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
