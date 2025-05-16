import sys
import numpy as np
import matplotlib.pyplot as plt
from datetime import date

from generate_matrix import generate_matrix
from calculate_lowest_eigenvectors import calculate_lowest_eigenvectors
from annotate_plot import annotate_plot

# Spatial domain for all wavefunctions
MIN_X = -10.0
MAX_X =  10.0

# Default parameters
NDIM_DEFAULT      = 100
POTENTIAL_DEFAULT = "harmonic"
PARAM_DEFAULT     = 1.0
EIG_INDICES = [2, 3, 4]


def main(Ndim: int, potential_name: str, potential_parameter: float):
    """
    Computes eigenfunctions #2, #3 & #4, plot them together
    on one axes from inputs of Ndim, potential_name and potential_parameter.
    Labels and annotates the graph, and saves it as a PNG file.
    """
    H = generate_matrix(MIN_X, MAX_X, Ndim, potential_name, potential_parameter)
    needed = max(EIG_INDICES) + 1
    energies, wavefuncs = calculate_lowest_eigenvectors(
        H, number_of_eigenvectors=needed
    )

    x = np.linspace(MIN_X, MAX_X, Ndim)
    max_amp = np.max(np.abs(wavefuncs))

    # Creates axes
    fig, ax = plt.subplots(figsize=(6, 4))

    # Plots the eigenfunctions
    for idx in EIG_INDICES:
        psi = wavefuncs[idx].copy()
        if psi[0] < 0:
            psi *= -1

        ax.plot(
            x, psi, '-',
            label=rf"$\psi_{{{idx}}},\ E_{{{idx}}} = {energies[idx]:.3f}\ \mathrm{{a.u.}}$"
        )

    # Axes labels
    ax.set_xlabel("x [a.u.]")
    ax.set_ylabel(r"$\psi_n(x)$ [a.u.]")

    # Limits
    ax.set_ylim(-2 * max_amp, 2 * max_amp)
    ax.axhline(0, color="k", linewidth=1)

    # Legend
    ax.legend(loc="upper right")

    # Signature annotation
    sig = f"Created by Dan Masnik ({date.today().isoformat()})"
    annotations = {
        sig: {
            "position": np.array([0.02, -0.10]),
            "alignment": ["left", "top"],
            "fontsize": 8.0
        }
    }
    annotate_plot(annotations)

    # Sets title
    ax.set_title(
        f"Select Wavefunctions ψ_{EIG_INDICES[0]},{EIG_INDICES[1]},{EIG_INDICES[2]} "
        f"for a {potential_name} Potential on a Spatial Grid of {Ndim} Points"
    )
    plt.subplots_adjust(bottom=0.2)

    # Saves to PNG
    indices_str = "".join(str(i) for i in EIG_INDICES)
    outname = f"Masnik.{potential_name}.Eigenvectors{indices_str}.png"
    fig.savefig(outname, dpi=300)
    print(f"Saved plot to {outname}")


if __name__ == "__main__":
    if len(sys.argv) == 4:
        Ndim = int(sys.argv[1])
        pot  = sys.argv[2]
        param = float(sys.argv[3])
    else:
        print("Usage: python visualize_wavefunctions.py <Ndim> <potential_name> <potential_parameter>")
        print("Falling back to defaults: Ndim=100, potential='harmonic', parameter=1.0")
        Ndim, pot, param = NDIM_DEFAULT, POTENTIAL_DEFAULT, PARAM_DEFAULT

    main(Ndim, pot, param)