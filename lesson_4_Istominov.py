print(
    "Привіт! Це программа нотаток. Для роботи з нотатками використовуй наступні команди:\n\n"
    "add - додати нотатку Користувач вводить текст нотатки, який зберігається у програмі та є дійсним "
    "до її завершення\n"
    "earliest - виводить збережені нотатки у хронологічному порядку - від найстарішої до найновішої\n"
    "latest - виводить збережені нотатки у хронологічному порядку - від найновішої до найстарішої\n"
    "longest - виводить збережені нотатки у порядку їх довжини - від найдовшої до найкоротшої\n"
    "shortest - виводить збережені нотатки у порядку їх довжини - від найкоротшої до найдовшої\n"
    "exit - вихід\n")

notes_list = []
# Починаємо цикл while
while True:
    command = input('Введіть команду: ')
    # додаємо нотатку
    if command == 'add':
        note = input('Введіть текст: ')
        notes_list.append(note)
        print('Нотатку додано!')
    # відображаєм список від самої першої нотатки до останньої
    elif command == 'earliest':
        print(notes_list)
    # відображаєм список від останньої о самої першої нотатки
    elif command == 'latest':
        sorted_list = notes_list
        sorted_list.reverse()
        print(sorted_list)
        # сортуємо від найдовшої до найкоротшої нотатки
    elif command == "longest":
        list_by_length = sorted(notes_list, key=len, reverse=True)
        print(list_by_length)
        # сортуємо від найкоротшої до найдовшої нотатки
    elif command == "shortest":
        list_by_short = sorted(notes_list, key=len)
        print(list_by_short)
        # вихід з програми
    elif command == "exit":
        print("Ви завершили програму")
        break
        # обробка невірно введених даних
    else:
        print("Введіть дійсну команду")
