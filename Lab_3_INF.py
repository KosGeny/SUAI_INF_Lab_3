flag = True
while (flag):
    text_array = input().split()
    if len(text_array) != 0:
        flag = False
        swap_bool = True
        while swap_bool:
            swap_bool = False
            for i in range(len(text_array) - 1):
                if text_array[i] > text_array[i + 1]:
                    text_array[i], text_array[i + 1] = text_array[i + 1], text_array[i]
                    swap_bool = True
        for word in text_array:
            print(word)
    else:
        print('Ой, что-то пошло не так! Попробуйте ещё раз.')



