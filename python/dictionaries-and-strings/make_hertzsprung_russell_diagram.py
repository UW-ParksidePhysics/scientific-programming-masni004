import os
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, Normalize

# Constants
astronomical_unit = 1.495978707e11
meters_to_parsec = 1.0 / (648000.0 * astronomical_unit / math.pi)
M_SUN = 4.83

# Five brightest stars in the sky
brightest = {
    '32349': 'Sirius',
    '30438': 'Canopus',
    '71683': 'Rigil Kent',
    '69673': 'Arcturus',
    '91262': 'Vega',
}


def read_file(filename):
    """
    Reads a file (in this case hipparcos_data.txt) and returns a dictionary
    """
    hip_dict = {}
    base = os.path.dirname(__file__)
    path = os.path.join(base, filename)

    with open(path) as fp:
        for line in fp:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            cols = line.split()
            hip = cols[0]
            hip_dict[hip] = {
                'parallax': float(cols[1]),
                'Vmag': float(cols[2]),
                'BV': float(cols[3]),
            }
    return hip_dict


def parallax_to_distance(p_mas):
    """
    Converts parallax mass to distance
    """
    p_rad = (p_mas / 1000 / 3600) * (2 * math.pi / 360)
    return astronomical_unit / math.tan(p_rad)


def apparent_to_absolute_magnitude(V, d_m):
    """
    Converts apparent magnitude to absolute magnitude.
    """
    d_pc = d_m * meters_to_parsec
    return V - 5 * math.log10(d_pc) + 5


def star_colormap(BV):
    """
    Creation of star colormap based on BV.
    """
    bv_min, bv_max = -0.33, 1.40
    control_bv = np.array([-0.33, 0.0, 0.3, 0.6, 1.0, 1.4])
    control_colors = ['#9bb0ff', '#ffffff', '#fff4e8',
                      '#ffd2a1', '#ffae8a', '#ff0000']

    # Set control points to [0,1]
    pts = (control_bv - bv_min) / (bv_max - bv_min)
    cmap = LinearSegmentedColormap.from_list('bv_cmap',
                                             list(zip(pts, control_colors)))
    norm = Normalize(vmin=bv_min, vmax=bv_max)
    return norm(BV), cmap


def main():
    """
    Reads data, constructs arrays, and plots the colored map.
    Two axes are created and scaled appropriately, complete with a signature.

    """
    hip = read_file('hipparcos_data.txt')

    BVs = []
    Mvs = []
    hips = []
    for hipid, data in hip.items():
        d = parallax_to_distance(data['parallax'])
        M = apparent_to_absolute_magnitude(data['Vmag'], d)
        BVs.append(data['BV'])
        Mvs.append(M)
        hips.append(hipid)
    BVs = np.array(BVs)
    Mvs = np.array(Mvs)

    colors_norm, cmap = star_colormap(BVs)

    fig, ax = plt.subplots(figsize=(6, 8))
    sc = ax.scatter(BVs, Mvs,
                    c=colors_norm,
                    cmap=cmap,
                    s=8, edgecolors='none')

    ax.invert_yaxis()  # brighter (smaller Mv) at top
    ax.set_xlabel('B–V color index')
    ax.set_ylabel('Absolute magnitude $M_V$')
    ax.set_title('Hertzsprung–Russell Diagram')
    ax.grid(True, linestyle=':', alpha=0.3)

    # Brightest stars
    for hipid, name in brightest.items():
        if hipid in hip:
            bv = hip[hipid]['BV']
            d = parallax_to_distance(hip[hipid]['parallax'])
            M = apparent_to_absolute_magnitude(hip[hipid]['Vmag'], d)
            ax.annotate(name,
                        xy=(bv, M),
                        xytext=(5, -5),
                        textcoords='offset points',
                        fontsize=8,
                        color='black',
                        weight='bold')

    # 6) Right y-axis: luminosity L/L_sun
    def mv_to_lum(mv):  return 10**(0.4*(M_SUN - mv))
    def lum_to_mv(l):   return M_SUN - 2.5*math.log10(l)

    ax2 = ax.twinx()
    ax2.set_ylim(ax.get_ylim())
    mv_ticks = np.arange(math.floor(min(Mvs)),
                         math.ceil(max(Mvs)) + 1, 2)
    ax.set_yticks(mv_ticks)
    lum_ticks = [mv_to_lum(m) for m in mv_ticks]
    ax2.set_yticks(mv_ticks)
    ax2.set_yticklabels([f"{l:.1e}" for l in lum_ticks])
    ax2.set_ylabel(r'Luminosity $L/L_\odot$')

    # Top axis: spectral class + T_eff
    bv_ticks = np.array([-0.33, -0.02, 0.15,
                         0.44, 0.58, 0.81, 1.40])
    classes = ['O', 'B', 'A', 'F', 'G', 'K', 'M']
    # approximated T_eff formula
    def bv_to_temp(bv):
        return 4600 * (1/(0.92*bv+1.7) + 1/(0.92*bv+0.62))

    temps = [int(bv_to_temp(bv)) for bv in bv_ticks]
    top_labels = [f"{cl}\n{t}" for cl, t in zip(classes, temps)]

    ax_top = ax.twiny()
    ax_top.set_xlim(ax.get_xlim())
    ax_top.set_xticks(bv_ticks)
    ax_top.set_xticklabels(top_labels)
    ax_top.set_xlabel('Spectral class     $T_{eff}$ (K)')

    # Signature
    ax.text(0.02, 0.02,
            'Created by Dan Masnik',
            transform=ax.transAxes,
            fontsize=8, color='gray', va='bottom')

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()