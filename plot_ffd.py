import pathlib
import matplotlib.pyplot as plt

filepath = pathlib.Path(__file__).parent.absolute() / 'simulations' / 'FFD_TB.txt'

time = []
clk = []
d = []
q = []
r = []

with open(filepath) as fp:
    next(fp)
    for line in fp:
        time.append(float(line.split('\t')[0])*1e9)
        clk.append(float(line.split('\t')[1]))
        d.append(float(line.split('\t')[2]))
        q.append(float(line.split('\t')[3]))
        r.append(float(line.split('\t')[4]))

plt.figure(figsize=(50,20))
plt.suptitle('Simulación FFD', fontsize=20)

clk_ax = plt.subplot(4,1,1)
clk_ax.plot(time, clk, 'b')
clk_ax.set_title('Clock', fontsize=20)
clk_ax.set_ylabel('Tensión [V]', fontsize=20)
clk_ax.set_xlabel('Tiempo [ns]', fontsize=20)

r_ax = plt.subplot(4,1,2)
r_ax.plot(time, r, 'r')
r_ax.set_title('Reset', fontsize=20)
r_ax.set_ylabel('Tensión [V]', fontsize=20)
r_ax.set_xlabel('Tiempo [ns]', fontsize=20)

d_ax = plt.subplot(4,1,3)
d_ax.plot(time, d, 'g')
d_ax.set_title('D', fontsize=20)
d_ax.set_ylabel('Tensión [V]', fontsize=20)
d_ax.set_xlabel('Tiempo [ns]', fontsize=20)

q_ax = plt.subplot(4,1,4)
q_ax.plot(time, q, 'b')
q_ax.set_title('Q', fontsize=20)
q_ax.set_ylabel('Tensión [V]', fontsize=20)
q_ax.set_xlabel('Tiempo [ns]', fontsize=20)

plt.savefig('FFD_results.png')
plt.show()
