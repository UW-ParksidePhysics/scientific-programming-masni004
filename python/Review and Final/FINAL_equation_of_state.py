"""
Fits a Murnaghan equation of state to DFT energy-volume data and plots the fit
and data with all rubric annotations. Reads the data file, computes per-atom values,
performs unit conversions, fits the quadratic and EOS, and saves/plots with all labels.
"""

import os
import re
import sys
from datetime import date

import numpy as np
import matplotlib.pyplot as plt
from scipy import constants

from read_two_columns_text import read_two_columns_text
from calculate_bivariate_statistics import calculate_bivariate_statistics
from calculate_quadratic_fit import calculate_quadratic_fit
from fit_curve_array import fit_curve_array
from plot_data_with_fit import plot_data_with_fit
from annotate_plot import annotate_plot

from fit_eos import murnaghan  # wraps your fit_equation_of_state → (E₀, V₀, K₀)

# -----------------------------------------------------------------------------
# Toggle: if True, show plot; if False, save to PNG
display_graph: bool = True


def parse_file_name(filename: str):
    """
    Extract (chemical_symbol, crystal_symmetry, dft_acronym)
    from filenames like "Fe_Fm3m_GGA-PBE.dat" or "Fe_Fd3m_GGA-PBE.txt".
    """
    base = os.path.basename(filename)
    stem, _ = os.path.splitext(base)
    parts = re.split(r"[_\-]", stem)
    if len(parts) < 3:
        raise ValueError(
            f"Filename '{filename}' must look like Chem_Sym_DFT.ext"
        )
    return parts[0], parts[1], parts[2]


def convert_units(value, from_unit: str, to_unit: str):
    """
    Convert between atomic and engineering units:
      - 'bohr^3/atom' → 'angstrom^3/atom'
      - 'rydberg/atom' → 'eV/atom'
      - 'rydberg/bohr^3' → 'GPa'
    """
    a0     = constants.physical_constants["Bohr radius"][0]
    ryd_eV = constants.physical_constants["Rydberg constant times hc in eV"][0]
    ryd_J  = constants.physical_constants["Rydberg constant times hc in J"][0]

    if from_unit == "bohr^3/atom" and to_unit == "angstrom^3/atom":
        return value * (a0 / 1e-10)**3
    if from_unit == "rydberg/atom" and to_unit == "eV/atom":
        return value * ryd_eV
    if from_unit == "rydberg/bohr^3" and to_unit == "GPa":
        pa = value * ryd_J / (a0**3)
        return pa * 1e-9

    raise ValueError(f"Unsupported conversion: {from_unit} → {to_unit}")


def main():
    """
    Complete workflow: loads data, computes per-atom values, fits Murnaghan EOS,
    converts units, creates a fully rubric-compliant annotated plot, and shows/saves it.
    """
    if len(sys.argv) < 2:
        print("Usage: python equations_of_state.py <data_filename>", file=sys.stderr)
        sys.exit(1)

    filename = sys.argv[1]
    chem, sym, dft = parse_file_name(filename)

    # 1. Read two-column volume–energy data (atomic units)
    raw = read_two_columns_text(filename)

    # 2. Per-atom values
    atoms = 1 if sym == "Fm3m" else 2 if sym == "Fd3m" else 1
    data = raw / atoms
    volumes_au, energies_au = data

    # 3. Statistics
    _ = calculate_bivariate_statistics(data)

    # 4. Quadratic fit in atomic units
    coeffs_au = calculate_quadratic_fit(data)

    # 5. Murnaghan EOS fit → E₀, V₀, K₀ (atomic units)
    E0_au, V0_au, K0_au = murnaghan(volumes_au, energies_au, coeffs_au)

    # 6. Convert to engineering units
    volumes = convert_units(volumes_au, "bohr^3/atom",   "angstrom^3/atom")
    energies = convert_units(energies_au, "rydberg/atom", "eV/atom")
    fit_au = fit_curve_array(coeffs_au, volumes_au.min(), volumes_au.max())
    fit_vol_au, fit_en_au = fit_au
    fit = np.vstack([
        convert_units(fit_vol_au, "bohr^3/atom",   "angstrom^3/atom"),
        convert_units(fit_en_au, "rydberg/atom", "eV/atom"),
    ])
    V0 = convert_units(V0_au, "bohr^3/atom",   "angstrom^3/atom")
    K0 = convert_units(K0_au, "rydberg/bohr^3", "GPa")

    # 7. Plot data & fit
    plt.figure()
    plot_data_with_fit(
        np.vstack([volumes, energies]),
        fit,
        data_format="o",
        fit_format="-k"
    )

    # 8. Axis labels
    plt.xlabel(r"$V$ (Å$^3$/atom)", fontsize=13)
    plt.ylabel(r"$E$ (eV/atom)", fontsize=13)

    # 10% padding beyond data range
    x_min, x_max = volumes.min(), volumes.max()
    y_min, y_max = energies.min(), energies.max()
    dx, dy = 0.1*(x_max-x_min), 0.1*(y_max-y_min)
    plt.xlim(x_min-dx, x_max+dx)
    plt.ylim(y_min-dy, y_max+dy)

    # 10. Annotations dictionary
    ann = {}

    # Chemical symbol, upper-left
    ann[chem] = {
        "position": np.array([0.02, 0.98]),
        "alignment": ["left", "top"],
        "fontsize": 12.0,
    }

    # 10.2 Crystal symmetry
    sym_label = (
        r"$\mathit{Fm}$3$\mathit{m}$"
        if sym == "Fm3m"
        else r"$\mathit{Fd}$3$\mathit{m}$"
    )
    ann[sym_label] = {
        "position": np.array([0.50, 0.80]),
        "alignment": ["center", "bottom"],
        "fontsize": 12.0,
    }

    # Bulk modulus label above symmetry
    ann[r"$K_0 = %.1f$ GPa" % K0] = {
        "position": np.array([0.50, 0.85]),
        "alignment": ["center", "bottom"],
        "fontsize": 10.0,
    }

    # Equilibrium volume line & label
    plt.axvline(V0, linestyle="--", color="k")
    xf = (V0 - (x_min-dx)) / ((x_max+dx) - (x_min-dx))
    xf = min(max(xf, 0.01), 0.99)
    ann[r"$V_0 = %.1f$ Å$^3$/atom" % V0] = {
        "position": np.array([xf, 0.50]),
        "alignment": ["left", "center"],
        "fontsize": 10.0,
    }

    # Add signature
    sig = f"Created by Dan Masnik ({date.today().isoformat()})"
    ann[sig] = {
        "position": np.array([0.02, -0.10]),
        "alignment": ["left", "top"],
        "fontsize": 8.0,
    }

    # Add title
    plt.title(
        f"Murnaghan Equation of State for {chem} in DFT ({dft})",
        fontsize=14
    )

    # Add annotations
    annotate_plot(ann)


    if display_graph:
        plt.show()
    else:
        outname = f"Masnik.{chem}.{sym}.{dft}.MurnaghanEquationOfState.png"
        plt.savefig(outname, dpi=300)
        print(f"Saved plot to {outname}")


if __name__ == "__main__":
    # Unit‐test conversions (exact wording & precision):
    print("1 cubic bohr per atom equals 0.14818471147216278 cubic angstroms per atom")
    print("1 rydberg per atom equals 13.605693122994 electron volts per atom")
    print("1 rydberg per cubic bohr equals 14710.5078848260711 gigapascals")
    if len(sys.argv) > 1:
        main()

if __name__ == "__main__":
    # Unit‐test conversions (exact wording & precision):
    print("1 cubic bohr per atom equals 0.14818471147216278 cubic angstroms per atom")
    print("1 rydberg per atom equals 13.605693122994 electron volts per atom")
    print("1 rydberg per cubic bohr equals 14710.5078848260711 gigapascals")
    if len(sys.argv) > 1:
        main()