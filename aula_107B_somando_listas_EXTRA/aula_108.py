
from validacoes_uteis import is_tuple_or_list

# lista_a = (5,6,9,4,5,20)
# lista_b = (2,4,6,8,10)


lista_a = [5,6,9,4,5,20]
lista_b = [2,4,6,8,10]

def decoration(func):

    def wrapper(*args,**kwargs):

        for v in args:

            is_tuple_or_list(v)

        run_function = func(*args,**kwargs)

        return run_function
    
    return wrapper


@decoration
def sum_asymmetric_lists(first_list,second_list):
    smaller_list_limit = min(len(first_list), len(second_list))
    sum_values_in_lists = [first_list[i] + second_list[i] for i in range(smaller_list_limit)]

    return sum_values_in_lists

print(sum_asymmetric_lists(lista_a,lista_b))
    