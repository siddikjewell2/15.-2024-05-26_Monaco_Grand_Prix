import matplotlib
matplotlib.use('Agg')
import fastf1
import matplotlib.pyplot as plt
import os

os.makedirs("cache", exist_ok=True)
fastf1.Cache.enable_cache("cache")

session = fastf1.get_session(2024, "Monaco", "Q")
session.load()

lap = session.laps.pick_fastest()
pos = lap.get_pos_data()
telemetry = lap.get_car_data()

fig, ax = plt.subplots(figsize=(14, 12))
scatter = ax.scatter(pos['X'], pos['Y'], c=telemetry['Speed'], 
                     cmap='plasma', s=20, alpha=0.8)
ax.set_aspect('equal')
ax.set_title("Monaco GP - Speed Map (Fastest Lap)", fontsize=16, fontweight='bold')
ax.set_xlabel("X Coordinate (meters)")
ax.set_ylabel("Y Coordinate (meters)")
cbar = plt.colorbar(scatter)
cbar.set_label('Speed (km/h)', fontsize=12)

plt.savefig('monaco_speed_map.png', dpi=150, bbox_inches='tight')
print("✅ Speed map saved: monaco_speed_map.png")