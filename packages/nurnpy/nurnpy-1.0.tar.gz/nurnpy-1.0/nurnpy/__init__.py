def sqrt(name):
    if 'amhgqn' in name:
        print(
            '''import numpy as np
from scipy.stats import *

scores = [90, 79, 53, 62, 66, 68, 75, 0, 82, 29, 0, 29, 68, 90, 0, 60, 44, 44, 70, 68, 70, 89, 0, 68, 0, 66, 0, 59, 70]

positive_scores = [score for score in scores]
A = np.mean(positive_scores)

M = np.median(positive_scores)

high_scores = [score for score in positive_scores if score >= M]
H = hmean(high_scores)
G = gmean(high_scores)

Q = np.median(high_scores)

count_between_H_and_Q = len([score for score in positive_scores if Q <= score <= H])

print("1) Средняя положительная оценка (A):", round(A, 2))
print("2) Медиана положительных оценок (M):", M)
print("3) Среднее гармоническое (H):", round(H, 2))
print("   Среднее геометрическое (G):", round(G, 2))
print("4) Медиана оценок >= M (Q):", Q)
print("5) Количество студентов между H и Q (N):", count_between_H_and_Q)
''')
    if 'pd' in name:
        print(
            '''data = np.array([-9, 9, -138, -145, 186, 78, 34, -37, -19, -68, -82, 158, 96, 
                 -189, 24, 84, -99, 125, -39, 26, 62, -91, 239, -211, 2, 129, 2, -16])

mean_pd = np.mean(data)

std_dev_pd = np.std(data)

L = norm.ppf(0.25, loc=mean_pd, scale=std_dev_pd)
H = norm.ppf(0.75, loc=mean_pd, scale=std_dev_pd)

count_in_range = len([d for d in data if L <= d <= H])

def func(x, lst):
    return  len(lst[lst <= x])/len(lst)

sup = max(np.abs( [func(x, data) for x in sorted(data)] - norm(data.mean(),data.std()).cdf(sorted(data))))
print("1) Среднее арифметическое ПД:", round(mean_pd, 2))
print("2) Эмпирическое стандартное отклонение ПД:", round(std_dev_pd, 2))
print("3) Квартиль L:", round(L, 2))
print("   Квартиль H:", round(H, 2))
print("4) Количество ПД, попавших в интервал от L до H:", count_in_range)
print(f'Расстояние между функциями F^(x) и F(x): {sup:.3}')
''')
    if 'xy' in name:
        print(
            '''xy = .......
sample=np.array(list(map(lambda x: (int(x[0].split('=')[1]), int(x[1].split('=')[1])),\
list(map(lambda x: x.split(','), xy.split('x')))[1:])))

mask = sample >= 50
x,y =sample[mask[:, 0] & mask[:, 1]].T

print(f' Ковариация: {np.cov(x,y,bias=True)[0][1]}')
print(f' Корреляция: {np.corrcoef(x,y)[0][1]}')
''')
    if 'potok' in name:
        print(
            '''n_values = np.array([24, 26, 30])
x_values = np.array([70, 76, 77])
σ_values = np.array([4, 6, 8])

X_Ω = np.average(x_values, weights=n_values)

variance_Ω = np.average((σ_values**2 + (x_values - X_Ω)**2), weights=n_values)
σ_Ω = np.sqrt(variance_Ω)

print("1) Среднее значение X на потоке Ω:", round(X_Ω, 2))
print("2) Стандартное отклонение X на потоке Ω:", round(σ_Ω, 3))
''')
    if 'mu3' in name:
        print(
            '''scores = [100, 86, 51, 100, 95, 100, 12, 61, 0, 0, 12, 86, 0, 52, 62, 76, 91, 91, 62, 91, 65, 91, 9, 83, 67, 58, 56]
n = 7 # Количество выборок

mean_X = np.mean(scores)
mean_X2 = np.mean([x**2 for x in scores])

variance_X = (mean_X2 - mean_X**2)/n

mu3_X = (np.mean([(x - mean_X)**3 for x in scores]))/n**2

print("1) Дисперсия Var(X):", round(variance_X, 3))
print("2) Центральный момент μ3(X):", round(mu3_X, 4))
''')
    if '100b' in name:
        print(
            '''scores =[100, 78, 77, 51, 82, 100, 73, 53, 78, 55, 7, 0, 81, 15, 96, 12, 71, 70, 53, 0, 73, 100, 55, 100, 59, 89, 81]
N = len(scores)
n = 6
N_n_coef = (N-n)/(N-1)
mean_X = np.mean(scores)
mean_X2 = np.mean([x**2 for x in scores])

variance_X = (mean_X2 - mean_X**2)/n *N_n_coef
print(f'E_X {round(mean_X,3)}')
print(f'var_X {round(variance_X,3)}')
''')
    if 'prepod' in name:
        print(
            '''scores = np.array([2]*7 + [3]*48 + [4]*8 + [5]*105)
N = len(scores)
n = N / 6 

N_n_coef = (N-n)/(N-1)

mean_X = np.mean(scores)
mean_X2 = np.mean([x**2 for x in scores])

E_X = round(mean_X,3)

var_X = (mean_X2 - mean_X**2)/n* N_n_coef
std_X = var_X**0.5

print(f'E_X = {E_X}')
print(f'Станд.откл {round(std_X,3)}')
''')
    if 'dice' in name:
        print(
            '''N = 36
n = 19
E_x_dice = 3.5
Var_x_dice = 35/12
N_n_coef = (N-n)/(N-1)
E_X  = 11*E_x_dice - 9*E_x_dice

Var_X = (121 * Var_x_dice  + 81*Var_x_dice)/n
Var_X = Var_X *N_n_coef
std_X = Var_X **0.5

print(f'E_X {round(E_X,1)}')
print(f'std_X {round(std_X,3)}')
''')

    if 'moneta' in name:
        print(
            '''def moneta():
    return tuple(np.random.randint(0, 2, size=11))

answ = []
for i in range(10000):
    cnt = 0
    diction = set()
    arr = []
    while cnt < 257:
        comb = moneta()
        if comb not in diction:
            diction.add(comb)
            arr.append(sum(comb))
            cnt += 1
            
    answ.append(np.mean(arr))
            
np.var(answ)
''')
    if 'evarp' in name:
        print(
            '''n_X1 = 11+32+11
n_X2 = 24+11+11
n_Y1 = 11+24
n_Y2 = 32+11
n_Y3 = 11+11
n = 7
N = 100
N_n_coef = (N-n)/(N-1)
xn_values = np.array([n_X1, n_X2])
x_values = np.array([100, 400])
yn_values = np.array([n_Y1,n_Y2,n_Y3])
y_values = np.array([1,2,3])


E_X = np.average(x_values, weights=xn_values)
E_Y = np.average(y_values,weights=yn_values)
E_Y2 = np.average(y_values**2,weights=yn_values)
E_X2 = np.average(x_values**2,weights=xn_values)
Var_Y = (E_Y2 - E_Y**2)/n*N_n_coef
Var_X = (E_X2 - E_X**2)/n*N_n_coef
cov_xy = 1*(1*11+2*32+3*11)+4*(1*24+2*11+3*11)- E_X*E_Y
cov_xy_ = cov_xy/n*N_n_coef
corr_xy = cov_xy_/(Var_Y**0.5*Var_X**0.5)

print(f'E_X {E_X:}')
print(f'E_Y {E_Y:.3}')
print(f'Var_X {Var_X:}')
print(f'Var_Y {Var_Y:.3}')
print(f'Cov_xy_ {cov_xy_:.3}')
print(f'Corr_xy {corr_xy:.3}')
print(f'std_y {Var_Y**0.5:.3}')
print(f'std_x {Var_X**0.5:.3}')
''')
    if 'eocov' in name:
        print(
            '''n_X1 = 21+17+12
n_X2 = 10+27+13
n_Y1 = 21+10
n_Y2 = 17+27
n_Y3 = 12+13
n = 6
N = 100
N_n_coef = (N-n)/(N-1)
xn_values = np.array([n_X1, n_X2])
x_values = np.array([100, 300])
yn_values = np.array([n_Y1,n_Y2,n_Y3])
y_values = np.array([1,2,4])


E_X = np.average(x_values, weights=xn_values)
E_Y = np.average(y_values,weights=yn_values)
E_Y2 = np.average(y_values**2,weights=yn_values)
E_X2 = np.average(x_values**2,weights=xn_values)
Var_Y = (E_Y2 - E_Y**2)/n*N_n_coef
Var_X = (E_X2 - E_X**2)/n*N_n_coef
cov_xy = 1*(1*21+2*17+4*12)+3*(1*10+2*27+4*13)- E_X*E_Y
cov_xy_ = cov_xy/n*N_n_coef
corr_xy = cov_xy_/(Var_Y**0.5*Var_X**0.5)

print(f'E_X {E_X:}')
print(f'E_Y {E_Y:.3}')
print(f'Var_X {Var_X:}')
print(f'Var_Y {Var_Y:.3}')
print(f'Cov_xy_ {cov_xy_:.3}')
print(f'Corr_xy {corr_xy:.3}')
print(f'std_y {Var_Y**0.5:.3}')
print(f'std_x {Var_X**0.5:.3}')
''')  
def keys():
    print(['amhgqn', 'pd', 'xy', 'potok', 'mu3', '100b', 'prepod', 'dice', 'moneta', 'evarp', 'eocov'])

