#Есть список из случайных чисел и строк. Создайте цикл, итерирующийся до тех пор, пока не встретится число "777". 
# Если в течении 100 попыток число не будет найдено — остановить цикл и вызвать ошибку с соответсвующим сообщением.

#ls = ['2','d','d','v','d','e','5','2','777','2','3','e','e','d','d','d','d','g','g','g','eef','sds','fsf','cxc','vcv','df','dsa','as','ds','sd','sde','wew','wewee','dsds','sdsd','dsd']

def fcount(list_s):
    count = 0
    for i in list_s:
        count +=1
        if i == '777':
            print('777 найдено')
            break
        elif (count == 100):
            print("больше 100 попыток")
#fcount(ls)

