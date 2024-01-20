f = open('c:/Users/egork/OneDrive/Рабочий стол/задание про переселение/Perepis.txt', 'r')
sum = 0
for i in range (31):
    Stroka = f.readline()
    Stroka_2 = Stroka.split ('  ')
    Stroka_F = Stroka_2[0]
    print (Stroka_F)
    Stroka_D = Stroka_2[3].split ('.')
    if (int(Stroka_D[2]) < 1978):
        sum = sum + 1
        print (Stroka)
print (sum)