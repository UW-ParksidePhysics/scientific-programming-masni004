import math

# Define constants
drag_coefficient = 0.2                          # dimensionless
air_density = 1.2                               # kg/m³
ball_radius = 0.11                              # cm
cross_area = math.pi * ball_radius**2           # m^2
ball_velocity_hard_kick = 120 * 1000 / 3600     # m/s
ball_velocity_soft_kick = 10 * 1000 / 3600      # m/s
ball_mass = 0.43                                # kg
gravitational_acceleration = 9.81               # m/s²

def compute_drag_force(v):
    return 0.5 * drag_coefficient * air_density * cross_area * v**2

def compute_gravity_force():
    return ball_mass * gravitational_acceleration

def print_forces(velocity_kmh, velocity_ms):
    drag_force = compute_drag_force(velocity_ms)
    gravitational_force = compute_gravity_force()
    ratio = drag_force / gravitational_force

    print(f"\nVelocity: {velocity_kmh} km/h ({velocity_ms:.2f} m/s)")
    print(f"Drag Force: {drag_force:.1f} N")
    print(f"Gravity Force: {gravitational_force:.1f} N")
    print(f"Drag / Gravity Ratio: {ratio:.2f}")

print_forces(120, ball_velocity_hard_kick)
print_forces(10, ball_velocity_soft_kick)