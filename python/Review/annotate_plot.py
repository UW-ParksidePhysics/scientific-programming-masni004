import numpy as np
import matplotlib.pyplot as plt
from matplotlib.text import Text
from typing import List


def annotate_plot(annotations: dict) -> List[Text]:
    """
    Takes a dictionary as an input and returns a list of text annotations
    to be displayed in the plot.
    """
    if not isinstance(annotations, dict):
        raise TypeError(f"Input must be a dictionary, got {type(annotations)}")

    ax = plt.gca()
    texts: List[Text] = []

    for label, props in annotations.items():
        if not isinstance(props, dict):
            raise TypeError(f"Properties for '{label}' must be a dictionary")
        try:
            pos = np.asarray(props['position'], dtype=float)
            halign, valign = props['alignment']
            fontsize = float(props['fontsize'])
        except KeyError as e:
            raise KeyError(f"Missing key {e!r} for annotation '{label}'")
        except (TypeError, ValueError):
            raise ValueError(f"Incorrect format for '{label}'")

        if pos.shape != (2,):
            raise ValueError(f"'position' for '{label}' must be shape (2,), got {pos.shape}")

        # Add the text just below the axes
        txt = ax.text(
            pos[0],
            pos[1],
            label,
            horizontalalignment=halign,
            verticalalignment=valign,
            fontsize=fontsize,
            transform=ax.transAxes,
            clip_on=False
        )
        texts.append(txt)

    return texts


if __name__ == "__main__":
    """
    AI Prompt (using Gemini 2.0 flash): picture + fix my label so it isn't covering the graph
    """
    import datetime

    # Create the plot
    x = np.linspace(0, 2 * np.pi, 200)
    y = np.sin(x)
    plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel("sin(x)")

    # Create signature
    today_iso = datetime.date.today().isoformat()
    signature = f"Created by Dan Masnik ({today_iso})"
    annot = {
        signature: {
            'position': np.array([0.05, -0.10]),  # moved down below the numbers
            'alignment': ['left', 'top'],
            'fontsize': 10.0
        }
    }

    annotate_plot(annot)
    plt.show()