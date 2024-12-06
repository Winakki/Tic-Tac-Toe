
def field_output(field):
# Функция вывода нашего поля в терминал 
# map обращается к str(функции) которая приводит [1, 2, 3] -> ['1', '2', '3'], а join уже в строку без списка
# и преобразует наш [1, 2, 3],[4, 5, 6],[7, 8, 9] --> 1 2 3 4 5 6 7 8 9
    for row in field:
        print(" ".join(map(str,row)))  

def space_check(check):
        # Провека занятости ячейки 
        row = (check - 1) // 3  # вычисляем колонну в который игрок хочет поставить 
        col = (check - 1) % 3   # вычисляем элемент в который игрок хочет поставить
        return isinstance(field[row][col],str)  # проверяем, если элемент является типом str, то место занято, иначе не занято
     
def check_win(list_player, victories):
    # Проверка победы сравниваем каждый элемент victories каждого списка с индексами player_1 или player_2
    # если три элемента сравнятся, то count = 3, то следовательно комбинация собралась и это победа
    count = 0
    for i in victories:
         for j in i:
              if j in list_player:
                    count += 1
              else:
                 count = 0
         if count == 3:
            return True       
         count = 0       
              
def check_draw(fields):
    # двойной цикл для проверки - есть ли тип int в field, для того чтобы если там нет int, то следовательно там всё str, а это ничья 
    return  any(isinstance(item, int) for row in fields for item in row)  

field = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

victories = [[0,1,2],
             [3,4,5],
             [6,7,8],
             [0,3,6],
             [1,4,7],
             [2,5,8],
             [0,4,8],
             [2,4,6]]

player_1 = []
player_2 = []

def game():
    def player_x(x):
            row = (x - 1) // 3
            col = (x - 1) % 3
            field[row][col] = 'X'
    def player_o(o):
            row = (o - 1) // 3
            col = (o - 1) % 3
            if field[row][col] == 'X' or 'O':
                field[row][col] = 'O'
            else:
                 print('Клетка занята')

    while True:
        field_output(field)
        position_x = int(input(f'Введите клетку X: '))

        while space_check(position_x) == True:
             #Проверка занятости ячейки
             print('Ячейка занята')
             field_output(field)
             position_x = int(input(f'Введите клетку X: '))

        player_1.append(position_x-1) # Добавляем индексы чтобы потом сравнить с победными комбинациями
        player_x(position_x) # Рисуем новое поле с поставленным X игрока
        field_output(field) # Показываем поле

        if check_draw(field) == False:
             # проверка ничьи
             print('Ничья')
             break
        
        if len(player_1) >= 3:
            # сравниваем победные комбинации
            if check_win(player_1, victories):
                print('Победа игрока: X')
                break 

        position_o = int(input(f'Введите клетку O: '))

        while space_check(position_o) == True:
             print('Ячейка занята')
             field_output(field)
             position_o = int(input(f'Введите клетку O: '))

        player_2.append(position_o-1)
        player_o(position_o)
        


        if len(player_2) >= 3:
            if check_win(player_2, victories):
                print('Победа игрока: O')
                break
        
        if check_draw(field) == False:
             print('Ничья')
             break

game()