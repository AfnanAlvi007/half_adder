This was my first half adder project I created the layout in Magic VLSI, extracted the circuit, and then simulated it using ngspice.

## What I Did

✅ Created the half adder layout using Magic VLSI
✅ Extracted the SPICE netlist (including parasitic effects)
✅ Performed transient simulation with ngspice
✅ Confirmed the logic operation works perfectly

## Results

Input A=0, B=0 → SUM=0, CARRY=0 ✓
Input A=0, B=1 → SUM=1, CARRY=0 ✓
Input A=1, B=0 → SUM=1, CARRY=0 ✓
Input A=1, B=1 → SUM=0, CARRY=1 ✓

Complete rail-to-rail swing (0V to 5V) ✓
All outputs switch correctly ✓

## Tools Used

* Magic VLSI (layout &amp; extraction)
* ngspice (SPICE simulation)
* Python (waveform analysis)

## Quick Start

**Install**
--bash
sudo apt-get install magic ngspice python3-matplotlib


**View Layout**
--bash
magic half_adder.mag


**Run Simulation**
--bash
ngspice half_adder_fixed.cir


**View Waveforms**
--bash
half_adder_waveforms_FIXED.png


**Verify Results**
--bash
python3 verify_results.py


## Project Structure
half_adder/
├── half_adder.mag (layout design)
├── half_adder.ext (extracted netlist)
├── half_adder_clean.spice (SPICE netlist)
├── half_adder_fixed.cir (simulation circuit)
├── half_adder_results_fixed.txt (simulation data)
├── half_adder_waveforms_FIXED.png (waveforms)
├── plot_fixed.py (plotting script)
├── verify_results.py (verification)
