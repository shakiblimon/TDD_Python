def hello_world():
    return "hello world!"

#   create a number list
def creat_num_list(length):
    return [x for x in range (length)]

#   custom function
def custom_func_x(x, const, power):
    return const * (x) ** power

#   Custom non linear number list
def custom_non_lin_num_list(length , const, power):
    return [custom_func_x(x,const,power) for x in range (length)]