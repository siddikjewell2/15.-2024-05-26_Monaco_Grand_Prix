import matplotlib
matplotlib.use('Agg')
import fastf1
import matplotlib.pyplot as plt
import os

os.makedirs("cache", exist_ok=True)
fastf1.Cache.enable_cache("cache")

session = fastf1.get_session(2024, "Monaco", "Q")
session.load()

fig, ax = plt.subplots(figsize=(14, 12))

# Top 3 দ্রুততম ল্যাপ আঁকুন
colors = ['#FF1801', '#1E5BC6', '#00D2BE']
top_3 = session.laps.pick_quickly(3)

for i, (idx, lap) in enumerate(top_3.iterrows()):
    pos = lap.get_pos_data()
    ax.plot(pos['X'], pos['Y'], linewidth=2.5, color=colors[i], 
            label=f"{lap['Driver']} - {lap['LapTime']}")

ax.set_aspect('equal')
ax.set_title("Top 3 Fastest Laps - Monaco GP Qualifying", 
             fontsize=16, fontweight='bold')
ax.set_xlabel("X Coordinate (meters)")
ax.set_ylabel("Y Coordinate (meters)")
ax.legend(loc='upper right', fontsize=10)
ax.grid(True, alpha=0.2)

plt.savefig('monaco_top3_laps.png', dpi=150, bbox_inches='tight')
print("✅ Top 3 laps comparison saved: monaco_top3_laps.png")