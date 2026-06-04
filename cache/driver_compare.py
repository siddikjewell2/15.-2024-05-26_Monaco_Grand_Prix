import matplotlib
matplotlib.use('Agg')
import fastf1
import matplotlib.pyplot as plt
import os

os.makedirs("cache", exist_ok=True)
fastf1.Cache.enable_cache("cache")

session = fastf1.get_session(2024, "Monaco", "Q")
session.load()

# VER vs HAM
ver_lap = session.laps.pick_driver('1').pick_fastest()   # Verstappen
ham_lap = session.laps.pick_driver('44').pick_fastest()  # Hamilton

fig, ax = plt.subplots(figsize=(14, 12))

ver_pos = ver_lap.get_pos_data()
ham_pos = ham_lap.get_pos_data()

ax.plot(ver_pos['X'], ver_pos['Y'], linewidth=3, color='#1E5BC6', label='Verstappen (VER)')
ax.plot(ham_pos['X'], ham_pos['Y'], linewidth=3, color='#00D2BE', label='Hamilton (HAM)')

ax.set_aspect('equal')
ax.set_title("Driver Comparison: Verstappen vs Hamilton\nMonaco GP Qualifying", 
             fontsize=16, fontweight='bold')
ax.set_xlabel("X Coordinate (meters)")
ax.set_ylabel("Y Coordinate (meters)")
ax.legend(loc='upper right', fontsize=12)
ax.grid(True, alpha=0.2)

plt.savefig('monaco_ver_vs_ham.png', dpi=150, bbox_inches='tight')
print("✅ Driver comparison saved: monaco_ver_vs_ham.png")