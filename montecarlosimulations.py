import numpy as np
import matplotlib.pyplot as plt

lamda_1 = float(input("the decay constant for N_A:"))# probability per unit time that the A atom decays to B units: sec^-1
lamda_2 = float(input("the decay constant for N_B:"))# probability per unit time that the B atom decays to C units: sec^-1
N_O = float(input("the number of A particles at time=0 seconds:"))

t = np.linspace(0,50,500)

N_A =( N_O*np.exp(-lamda_1*t))
N_B =( N_O*lamda_1*((np.exp(-lamda_1*t))-(np.exp(-lamda_2*t)))/(lamda_2-lamda_1))
N_C =((N_O)-(N_A)-(N_B))

plt.figure(figsize=(10,6))
plt.plot(t, N_A, label='N_A (A atoms)')
plt.plot(t, N_B, label='N_B (B atoms)')
plt.plot(t, N_C, label='N_C (C atoms)')
plt.xlabel('Time')
plt.ylabel('Number of Atoms')
plt.title('Decay Chain: A(unstable) → B(unstable) → C(stable)')
plt.grid(True)
plt.legend()
plt.show()
# this is a very basic one with one 2 unstable nuclei and chain reactions