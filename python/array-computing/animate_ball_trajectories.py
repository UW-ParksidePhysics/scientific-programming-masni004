import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

initial_conditions = [
    (0.0, 10.0, 45.0),
    (5.0, 20.0, 60.0),
    (2.0, 15.0, 30.0),
]

g = 9.81

def time_of_flight(y0, v0, θ):
    term = v0 * math.sin(θ)
    return (term + math.sqrt(term**2 + 2*g*y0)) / g

def max_height(y0, v0, θ):
    return y0 + (v0 * math.sin(θ))**2 / (2*g)

tfs = [time_of_flight(y0, v0, math.radians(θ))
       for y0, v0, θ in initial_conditions]
t_max = max(tfs)
frames = 200
dt = t_max / (frames - 1)

trajectories = []
labels = []
for y0, v0, θ_deg in initial_conditions:
    θ = math.radians(θ_deg)
    tf = time_of_flight(y0, v0, θ)
    xs, ys = [], []
    for i in range(frames):
        t = i * dt
        x = v0 * math.cos(θ) * t
        y = y0 + v0 * math.sin(θ) * t - 0.5 * g * t*t
        ys.append(max(y, 0.0))
        xs.append(x)
    trajectories.append((xs, ys))
    labels.append(f"y₀={y0}, v₀={v0}, θ={θ_deg}°")

fig, ax = plt.subplots()
x_maxes = [v0*math.cos(math.radians(θ))*tf for (y0,v0,θ), tf in zip(initial_conditions, tfs)]
ax.set_xlim(0, max(x_maxes))
ax.set_ylim(0, 1.1*max(max_height(y0, v0, math.radians(θ))
                       for y0, v0, θ in initial_conditions))
ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")
ax.set_title("Projectile trajectories (animated)")
colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

lines = []
for idx, (y0, v0, θ_deg) in enumerate(initial_conditions):
    line, = ax.plot([], [], color=colors[idx], label=labels[idx])
    lines.append(line)
    h = max_height(y0, v0, math.radians(θ_deg))
    ax.axhline(y=h, color=colors[idx], linestyle='--')

ax.legend()

def init():
    for line in lines:
        line.set_data([], [])
    return lines

def animate(frame):
    for idx, line in enumerate(lines):
        xs, ys = trajectories[idx]
        line.set_data(xs[:frame+1], ys[:frame+1])
    return lines

ani = FuncAnimation(
    fig, animate, init_func=init,
    frames=frames, interval=50, blit=True
)

plt.show()