# FPGA-Based FIR Filter for Audio Noise Removal

##  Project Overview

This project aims to design and implement an **FPGA-based Finite Impulse Response (FIR) filter** for removing unwanted high-frequency noise from audio signals.

The audio signal is first converted into digital samples. Controlled noise is added to the signal for testing, and the noisy samples are then processed using an FIR filter implemented using **Verilog HDL**. The design will be verified through **Xilinx Vivado simulation** and the filtered output will be compared with the original and noisy signals.

---

##  Objectives

* Design a digital FIR filter for audio noise removal.
* Use a **Low-Pass FIR filter** to reduce high-frequency noise.
* Implement the FIR filter using **Verilog HDL**.
* Verify the design using **Vivado simulation**.
* Process audio samples using Python.
* Compare the original, noisy, and filtered audio signals.
* Analyze the performance of the FPGA-based implementation.

---

##  Proposed System Architecture

```text
             Original Audio
                   │
                   ▼
             Audio Samples
                   │
                   ▼
              Add Noise
                   │
                   ▼
             Noisy Samples
                   │
                   ▼
        ┌────────────────────┐
        │    FIR FILTER      │
        │                    │
        │ Delay Registers    │
        │        ↓           │
        │ Multipliers        │
        │        ↓           │
        │ Adder              │
        └─────────┬──────────┘
                  │
                  ▼
          Filtered Samples
                  │
                  ▼
             Audio Output
                  │
                  ▼
        Performance Analysis
```

---

##  FIR Filter Principle

The FIR filter output is calculated using:

$$
y[n] = \sum_{k=0}^{N-1} h[k]x[n-k]
$$

Where:

* `x[n]` → Input audio sample
* `h[k]` → FIR filter coefficient
* `N` → Number of filter taps
* `y[n]` → Filtered output sample

The filter uses previous input samples along with predetermined coefficients to produce the filtered output.

---

##  Hardware Architecture

The FIR filter will contain:

```text
Input Sample
     │
     ▼
┌─────────────┐
│ Delay Line  │
└──────┬──────┘
       │
       ▼
┌─────────────────┐
│ Multiplication  │
│ x[n-k] × h[k]   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│     Adder       │
│ Sum of Products │
└────────┬────────┘
         │
         ▼
    Filtered Output
```

---

##  Tools & Technologies

| Component            | Technology       |
| -------------------- | ---------------- |
| Hardware Description | Verilog HDL      |
| FPGA Design Tool     | Xilinx Vivado    |
| Audio Processing     | Python           |
| Filter Design        | Python / NumPy   |
| Simulation           | Vivado Simulator |
| Version Control      | Git & GitHub     |

---

##  Planned Repository Structure

```text
FPGA-FIR-Audio-Filter/
│
├── README.md
│
├── python/
│   ├── generate_audio.py
│   ├── add_noise.py
│   ├── design_filter.py
│   └── analyze_results.py
│
├── verilog/
│   ├── fir_filter.v
│   └── fir_filter_tb.v
│
├── data/
│   ├── original_audio.wav
│   ├── noisy_audio.wav
│   └── filtered_audio.wav
│
├── results/
│   ├── waveforms/
│   └── plots/
│
└── docs/
    └── project_notes.md
```

---

##  Current Progress

### Phase 1 — Project Planning 

* [x] Project topic finalized
* [x] Problem statement identified
* [x] FIR filter concept studied
* [x] Low-pass filtering approach selected
* [x] FPGA implementation approach identified
* [x] Python + Verilog + Vivado workflow planned

### Phase 2 — Filter Design 

* [ ] Generate sample audio signal
* [ ] Add controlled high-frequency noise
* [ ] Determine sampling frequency
* [ ] Select filter cutoff frequency
* [ ] Calculate FIR coefficients
* [ ] Verify filter behavior using Python

### Phase 3 — FPGA Implementation 

* [ ] Develop FIR filter RTL
* [ ] Develop delay-line structure
* [ ] Implement multiplier and accumulator
* [ ] Develop Verilog testbench
* [ ] Run Vivado simulation
* [ ] Analyze RTL waveform

### Phase 4 — Audio Verification 

* [ ] Generate filtered samples
* [ ] Reconstruct filtered audio
* [ ] Compare original/noisy/filtered signals
* [ ] Analyze noise reduction
* [ ] Document results

---

##  Current Work

The initial stage of the project focuses on understanding the FIR filtering process and establishing the complete hardware-software workflow.

The planned workflow is:

```text
Audio
  ↓
Sampling
  ↓
Noise Addition
  ↓
FIR Coefficient Generation
  ↓
Verilog FIR Implementation
  ↓
Vivado Simulation
  ↓
Filtered Samples
  ↓
Audio Reconstruction
  ↓
Performance Analysis
```

---

## Expected Outcome

The final system is expected to demonstrate that an FIR filter implemented using FPGA-oriented RTL design can reduce unwanted high-frequency components from a noisy audio signal.

The project will include:

* FIR filter RTL design
* Verilog testbench
* Vivado simulation waveforms
* Audio signal plots
* Original vs noisy vs filtered comparison
* FPGA implementation analysis

---

##  Team

**Project:** FPGA-Based FIR Filter for Audio Noise Removal

**Domain:** FPGA / Digital Signal Processing / Audio Processing

---

##  Project Status

**Status:**  In Progress

Current focus: **FIR filter design, coefficient generation, and preparation for Verilog RTL implementation.**
