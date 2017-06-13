import matplotlib.pyplot as plt
def points():
    f = open(input('Введите имя файла:'))
    plt.figure("задание Андрея")                     #'ЗА.txt'
    for line in f:
        l,i = line.split(',')
        plt.plot([l], [i], 'ro')
        plt.axis([0, 20, 0, 50])
    plt.show()