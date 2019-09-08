#Assignment@17MCMC40
#frequency distribution #Zipf's law #exponent #log-log
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

def fit_func(x, a, c):
    return c * (x ** -a)

f = open("blackouts.txt")
data = f.readlines()
r = 1
x = []
y = []
for i in data:
    x.append(r)
    y.append(int(i))
    r += 1
y.sort(reverse = True)
#exponent calculation
popt, pcov = curve_fit(fit_func, x, y)
popt1, pcov1 = curve_fit(fit_func, x[:4], y[:4])
popt2, pcov2 = curve_fit(fit_func, x[40:200], y[40:200])
popt3, pcov3 = curve_fit(fit_func, x[140:], y[140:])
plt.figure(1)
plt.title("PDF")
plt.xlabel("words")
plt.ylabel("Frequency")
plt.plot(x, y, 'r', label='actual data')
plt.plot(x, fit_func(x, *popt), label = 'fitted curve\nalpha = %.3f' %popt[0])
plt.legend()
plt.figure(2)
plt.title("Log-log representation")
plt.xlabel("log(words)")
plt.ylabel("log(Frequency)")
plt.plot(x, y, 'r', label='actual data')
plt.plot(x, fit_func(x, *popt), 'b', label = 'fitted curve 1\nalpha = %.3f' %popt[0])
plt.plot(x[:4], fit_func(x[:4], *popt1), 'g', label = 'fitted curve 2\nalpha = %.3f' %popt1[0])
plt.plot(x[40:], fit_func(x[40:], *popt2), 'y', label = 'fitted curve 3\nalpha = %.3f' %popt2[0])
plt.plot(x[140:], fit_func(x[140:], *popt3), 'm', label = 'fitted curve 4\nalpha = %.3f' %popt3[0])
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.show()
