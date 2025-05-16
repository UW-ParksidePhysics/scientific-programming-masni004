import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Rectangle, Circle

# Data given
planets = [
    "Mercury",
    "Venus",
    "Earth",
    "Mars",
    "Ceres",
    "Jupiter",
    "Saturn",
    "Uranus",
    "Neptune",
    "Pluto",
]

# Temperature data in Kelvin
mins_K = np.array([89, 644, 184, 120, 180, 110, 82, 59, 50, 35])
maxs_K = np.array([723, 755, 330, 293, 235, 152, 143, 68, 53, 45])


def c_to_f(celsius):
    return celsius * 9.0 / 5.0 + 32.0


# Axes limits
C_MIN = -239
C_MAX = 482

# Line widths
TUBE_LINE_WIDTH = 3      # Thickness of the thermometer tube
BULB_LINE_WIDTH = 3      # Thickness of the bulb outline
OUTER_FRAME_WIDTH = 6    # Thickness of the outer frame around entire plot
MARKER_LINE_WIDTH = 4    # Thickness of the marker line


def plot_single_thermometer(planet, temp_min_c, temp_max_c, cmap):
    """
    Creates the thermometer for a single planet.
    """
    fig, ax = plt.subplots(figsize=(3, 8))

    # Thicken outer frame (axes spines)
    for spine in ax.spines.values():
        spine.set_linewidth(OUTER_FRAME_WIDTH)

    # Tube and bulb dimensions
    tube_width = 0.3
    bulb_radius = tube_width

    # Draw tube outline
    ax.add_patch(
        Rectangle(
            (0.5 - tube_width / 2, temp_min_c),
            tube_width,
            temp_max_c - temp_min_c,
            fill=False,
            linewidth=TUBE_LINE_WIDTH,
            zorder=5,
        )
    )

    # Draw bulb outline
    ax.add_patch(
        Circle(
            (0.5, temp_min_c),
            radius=bulb_radius,
            fill=False,
            linewidth=BULB_LINE_WIDTH,
            zorder=5,
        )
    )

    # Gradient fill
    grad = np.linspace(0.0, 1.0, 256).reshape(-1, 1)
    ax.imshow(
        grad,
        extent=[
            0.5 - tube_width / 2,
            0.5 + tube_width / 2,
            temp_min_c,
            temp_max_c,
        ],
        aspect="auto",
        cmap=cmap,
        origin="lower",
        zorder=1,
    )

    # Axis formatting
    ax.set_xlim(0.3, 0.7)
    ax.set_ylim(C_MIN, C_MAX)
    ax.set_xticks([])

    # Tick labels every 100 °C
    ticks_c = np.arange(C_MIN, C_MAX + 1, 100)
    ax.set_yticks(ticks_c)
    ax.set_yticklabels([f"{c:.0f}°C" for c in ticks_c])
    ax.tick_params(axis="y", labelsize=14)

    # Right y-axis: Fahrenheit
    ax_f = ax.twinx()
    ax_f.set_ylim(C_MIN, C_MAX)
    ax_f.set_yticks(ticks_c)
    ax_f.set_yticklabels([f"{c_to_f(c):.0f}°F" for c in ticks_c])
    ax_f.tick_params(axis="y", labelsize=14)

    # Marker line at the maximum temperature, spanning full frame width
    x0, x1 = ax.get_xlim()
    ax.hlines(
        temp_max_c,
        x0,
        x1,
        colors="black",
        linewidth=MARKER_LINE_WIDTH,
        zorder=20,
    )

    # Save and show
    file_name = f"Temperature_Icon_{planet}_Color.png"
    plt.tight_layout()
    plt.savefig(file_name)
    plt.show()


if __name__ == "__main__":
    # Colored gradient
    cmap_color = LinearSegmentedColormap.from_list("blue_red", ["blue", "red"])
    # Greyscale gradient
    cmap_gray = LinearSegmentedColormap.from_list("black_white", ["black", "white"])

    # Plot and save coloured thermometers
    for planet, min_k, max_k in zip(planets, mins_K, maxs_K):
        plot_single_thermometer(
            planet,
            min_k - 273.15,
            max_k - 273.15,
            cmap_color,
        )

    # Plot greyscale thermometers (without saving)
    for planet, min_k, max_k in zip(planets, mins_K, maxs_K):
        plot_single_thermometer(
            planet,
            min_k - 273.15,
            max_k - 273.15,
            cmap_gray,
        )