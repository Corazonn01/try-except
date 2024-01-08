def user_stuff():
    user_input = []
    while True:
        try:
            for _ in range(3):
                write_smth = int(input("Введите любые три последовательных числа: "))
                user_input.append(write_smth)

                if not all(x + 1 == y for x, y in zip(user_input, user_input[1:])):
                    raise ValueError("Числа не являются последовательными.")

            break
        except (ValueError, NameError, TypeError):
            print("Введите корректное число!")
    while True:
        try:
            index_w = int(input("а сейчас введите индекс для числа: "))
            break
        except (ValueError, TypeError):
            print("Введите число!")

    index_w = user_input[index_w]

    print(f"{index_w} > {user_input[0]} = {index_w > user_input[0]}")
    print(f"{index_w} > {user_input[1]} = {index_w > user_input[1]}")
    print(f"{index_w} > {user_input[2]} = {index_w > user_input[2]}")


user_stuff()
