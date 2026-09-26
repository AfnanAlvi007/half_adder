import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('half_adder_results_fixed.txt', skiprows=1)
time = data[:, 0] * 1e9
va = data[:, 1]
vb = data[:, 2]
vsum = data[:, 3]
vcarry = data[:, 4]

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

ax1.plot(time, va, 'b-', label='Input A (va)', linewidth=2)
ax1.plot(time, vb, 'r-', label='Input B (vb)', linewidth=2)
ax1.set_ylabel('Voltage (V)', fontsize=12)
ax1.set_title('Half Adder - Inputs', fontsize=14)
ax1.legend(loc='upper right')
ax1.grid(True, alpha=0.3)
ax1.set_ylim(-0.5, 5.5)

ax2.plot(time, vsum, 'g-', label='SUM', linewidth=2)
ax2.plot(time, vcarry, 'm-', label='CARRY', linewidth=2)
ax2.set_xlabel('Time (ns)', fontsize=12)
ax2.set_ylabel('Voltage (V)', fontsize=12)
ax2.set_title('Half Adder - Outputs', fontsize=14)
ax2.legend(loc='upper right')
ax2.grid(True, alpha=0.3)
ax2.set_ylim(-0.5, 5.5)

plt.tight_layout()
plt.savefig('half_adder_waveforms_FIXED.png', dpi=150)
print("Fixed plot saved!")
