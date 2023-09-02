from matplotlib import pyplot as plt

def show():
    fig = plt.gca()
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
    plt.show()


plt.figure(figsize=(10, 10))

plt.text(0.01, 0.9, "У нас 5 альпинистов с электронными часами, одновременно", fontsize=15)
plt.text(0.01, 0.8, "заряжеными до полной зараядки. Вероятность выхода из строя", fontsize=15)
plt.text(0.01, 0.7, "батарейки = 0,2.", fontsize=15)
plt.text(0.01, 0.6, "Найти вероятность, что у 3-х сломаются часы из-за батарейки.", fontsize=15)
plt.text(0.01, 0.5, "Вероятность что часы не сломаются = p = 1-0,2 = 0,8", fontsize=15)
plt.text(0.01, 0.4, "Для решения используем схему Бернулли:", fontsize=15)
form = r"$P_n(m) = C_n^m*p^m*(1-p)^{n-m}$"
plt.text(0.01, 0.3, form, fontsize=15)
form = r"$P_5(3) = C_5^3*p^3*(1-p)^{5-3} = \frac{5!}{3! 2!}*0,8^3*0,2^2 = 10*0,512*0,04 =$"
plt.text(0.01, 0.2, form, fontsize=15)
form = r"$= 0,2048*100 = 20,48$"
plt.text(0.01, 0.1, form, fontsize=15)
plt.text(0.01, 0.01, "Вероятность = 20,48 %", fontsize=15)

show()