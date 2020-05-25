def delete_space():
    with open('test.txt', 'r') as file_to_read:
        oper_string = file_to_read.read()
    print(oper_string.replace(' ', ''))


delete_space()
