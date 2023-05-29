from List import List, Singly_linked_list



def main():
    # 1 задание
    print('задача 1')
    list_os = List() # создание листа

    list_os.add_head(5) # добавление элементов в начало
    list_os.add_head(6)
    list_os.add_head(7)
    list_os.add_head(11)

    list_os.print_l()   # Печать списка
    
    print('Применение функции разворота списка....')
    list_os.reversely() # Функция разворота

    list_os.print_l()  # Печать списка
    # ===============================================================================
    # 2 задание

    s_list_os = Singly_linked_list()
    s_list_os.add_tail(2)
    s_list_os.add_tail(3)
    s_list_os.add_tail(6)
    s_list_os.add_tail(88)
    s_list_os.add_tail(92)
    s_list_os.add_tail(36)
    s_list_os.add_tail(61)
    s_list_os.add_tail(887)
    s_list_os.add_tail(9)

    print('----------------------------------------------------------------------------------------')
    print("задача 2")
    s_list_os.print_l()

    reversed_element = 8        # число n с конца списка
    currentNode = s_list_os.head
    flag = False
    while flag != True:
        c = currentNode
        for i in range(reversed_element):
            c = c.next
        if c.next == None:
            flag = True
        currentNode = currentNode.next
    print(' ' * 30 + '|')
    print(f'|-{reversed_element}- элемент с конца односвязного списка = {currentNode.value} |')



if __name__ == '__main__':
    main()