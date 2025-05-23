import numpy as np
import matplotlib.pyplot as plt

kxky = np.loadtxt("k_vals.txt")
energies = np.loadtxt("eig_vals.txt")

kx = kxky[:, 0]
ky = kxky[:, 1]
k_norm = np.sqrt(kx**2 + ky**2)

idx_sorted = np.argsort(k_norm)
k_sorted = k_norm[idx_sorted]
e_sorted = energies[idx_sorted, :]

plt.figure(figsize=(8,6))
for i in range(e_sorted.shape[1]):
    plt.plot(k_sorted, e_sorted[:, i], label=f'Band {i+1}')
plt.xlabel("||k||")
plt.ylabel("Energy")
plt.title("Graphene Energy Bands")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("graphene_bands.png", dpi=300)
plt.show()
