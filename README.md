# Python VOR Decoder

This repository contains a pure Python implementation of a VOR (VHF Omnidirectional Range) radio navigation signal decoder. The code is based on and adapted from the work of [martinber](https://github.com/martinber/vor-python-decoder), with additional comments, explanations, and minor modifications for clarity and usability.

## Overview

VOR is a type of radio navigation system for aircraft, allowing pilots to determine their position and bearing relative to a ground-based VOR station. This decoder processes a WAV file recording of a VOR signal and extracts the bearing information using digital signal processing techniques.

## Features

- **Pure Python implementation** using NumPy, SciPy, and Matplotlib
- **Signal processing pipeline** including:
  - Lowpass and bandpass FIR filtering
  - Sample rate decimation
  - FM subcarrier demodulation and phase extraction
  - Cross-correlation for phase comparison
- **Visualization** of signals in both time and frequency domains at each processing step
- **Calibration support** for phase alignment

## Usage

1. **Record a VOR signal** as a WAV file (mono or stereo). The recording should capture both the AM reference and FM variable signals.
2. **Set the `FILENAME` variable** in the notebook or script to point to your WAV file.
3. **Run the notebook or script** to process the signal and extract the bearing.

The processing steps include:

- Loading and displaying audio statistics
- Filtering and decimating the reference and variable signals
- Demodulating the FM subcarrier
- Extracting and filtering the variable signal phase
- Comparing phases to compute the bearing

## Dependencies

- numpy
- scipy
- matplotlib

Install them via pip if needed:

```bash
pip install numpy scipy matplotlib
```

## Attribution

Original code and algorithm by [martinber](https://github.com/martinber/vor-python-decoder).  
This repository provides a cleaned-up and commented version for educational and practical use.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
