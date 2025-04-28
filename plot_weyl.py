import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')  # 使用非交互式后端
data = np.loadtxt("data/Weyl4_mode_20.dat")
time = data[:, 0]
psi4_real = data[:, 1]

plt.figure(figsize=(8, 6))
plt.plot(time, psi4_real, 'b-', label='l=2, m=0')
plt.xlabel('time')
plt.ylabel('Re[Ψ₄]')
plt.title('mode l=2, m=0 (r=20)')
plt.grid(True)
plt.legend()
plt.savefig('weyl_l2_m0.png')
