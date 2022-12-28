def function(*p):
    s_strok =(' ')
    s_list = []
    s_numbers = 0
    # p = ([1,2,3,'a','bc8?'])
    for i in (p):
        if isinstance(i, str):
           s_strok += i
        elif isinstance(i,list):
            s_list += i
        elif isinstance((i,(int, float) )):
            s_numbers += i
        print('Букв', len(s_strok)-1)
        print('чисел', len(list(filter(lambda x: type(x) in (int, float), p))))
    #
    #     print('букв', len(p))
    # else:
    #     print('Неизвестный тип')
function([1,2,3,'a','bc8?'])
# function((1, 2, 3, 'a', 'bc8?', 7, 8, 9))
# function(788)
function('788')