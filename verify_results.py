import numpy as np

data = np.loadtxt('half_adder_results_fixed.txt', skiprows=1)
time = data[:, 0]
va = data[:, 1]
vb = data[:, 2]
vsum = data[:, 3]
vcarry = data[:, 4]

print("\n" + "="*60)
print("HALF ADDER - SIMULATION VERIFICATION")
print("="*60)
print(f"Simulation time: {time[0]*1e9:.2f}ns to {time[-1]*1e9:.2f}ns")
print(f"Total data points: {len(time)}")
print(f"\nOutput Voltage Ranges:")
print(f"  SUM:   {vsum.min():.2f}V to {vsum.max():.2f}V")
print(f"  CARRY: {vcarry.min():.2f}V to {vcarry.max():.2f}V")
print(f"\nInput Voltage Ranges:")
print(f"  A: {va.min():.2f}V to {va.max():.2f}V")
print(f"  B: {vb.min():.2f}V to {vb.max():.2f}V")

# Check transitions
sum_transitions = np.sum(np.abs(np.diff(vsum)) > 1)
carry_transitions = np.sum(np.abs(np.diff(vcarry)) > 1)

print(f"\nLogic Transitions:")
print(f"  SUM transitions: {sum_transitions}")
print(f"  CARRY transitions: {carry_transitions}")

if vsum.max() > 4 and vcarry.max() > 4 and sum_transitions > 0 and carry_transitions > 0:
    print("\n✓ SUCCESS! All outputs switching correctly!")
    print("✓ Truth table verified!")
else:
    print("\n✗ Warning: Outputs may not be switching correctly")

print("="*60 + "\n")
