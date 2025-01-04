
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(7, 'abcde')
print_params( 9,None, False)
print_params(34)
print_params()

print_params(b=25)
print('Функция print_params(b=25) работает')
print_params(c = [1,2,3])
print('Функция print_params(c = [1,2,3]) работает')

values_list = [12345, None, 'abcdef']
values_dict = {'a': 5 , 'b': 'не b', 'c': False}
# (* для списка и ** для словаря).
print_params(*values_list)
print_params(**values_dict)
# 3.Распаковка + отдельные параметры:
# Создайте список values_list_2 с двумя элементами разных типов
values_list_2 = ['Nevskii-', 51]
# Проверьте, работает ли print_params(*values_list_2, 42)
print_params(*values_list_2, 42)
print('Функция print_params(*values_list_2, 42) работает')
