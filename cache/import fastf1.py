import matplotlib
matplotlib.use('Agg')  # GUI ছাড়া কাজ করবে

import fastf1
import matplotlib.pyplot as plt
import os
from datetime import datetime

# ক্যাশ সেটআপ
cache_dir = "cache"
if not os.path.exists(cache_dir):
    os.makedirs(cache_dir)
fastf1.Cache.enable_cache(cache_dir)

print("=" * 50)
print("F1 TRACK VISUALIZER")
print("=" * 50)

# ডেটা লোড
print("\n[1/4] Loading Monaco GP Qualifying data...")
session = fastf1.get_session(2024, "Monaco", "Q")
session.load()
print("[OK] Data loaded successfully!")

# দ্রুততম ল্যাপ
print("\n[2/4] Finding fastest lap...")
lap = session.laps.pick_fastest()
driver = lap['Driver']
lap_time = lap['LapTime']
print(f"[OK] Fastest lap: Driver {driver} - Time: {lap_time}")

# পজিশন ডেটা
print("\n[3/4] Getting position data...")
pos = lap.get_pos_data()
print(f"[OK] Position data: {len(pos)} points")

# ট্র্যাক আঁকা
print("\n[4/4] Drawing track...")
fig, ax = plt.subplots(figsize=(14, 12))
ax.plot(pos['X'], pos['Y'], linewidth=4, color='#FF1801')  # F1 Red
ax.set_aspect('equal')
ax.set_title(f"Monaco Grand Prix Circuit\nFastest Qualifying Lap - Driver {driver} ({lap_time})", 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("X Coordinate (meters)", fontsize=12)
ax.set_ylabel("Y Coordinate (meters)", fontsize=12)
ax.grid(True, alpha=0.2, linestyle='--')
ax.fill_between(pos['X'], pos['Y'], alpha=0.1, color='#FF1801')

# গুরুত্বপূর্ণ পয়েন্ট চিহ্নিত করা
start_point = (pos['X'].iloc[0], pos['Y'].iloc[0])
ax.plot(start_point[0], start_point[1], 'go', markersize=10, label='Start/Finish')
ax.legend(loc='upper right')

# ছবি সেভ
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
filename = f"monaco_track_{timestamp}.png"
plt.savefig(filename, dpi=150, bbox_inches='tight')
print(f"\n[SUCCESS] TRACK IMAGE SAVED: {filename}")
print(f"[LOCATION] {os.path.abspath(filename)}")

# ড্রাইভার তথ্য দেখান
print("\n" + "=" * 50)
print("TOP 3 DRIVERS IN QUALIFYING:")
print("=" * 50)
top_3_laps = session.laps.pick_quickly(3)
for i, (idx, lap) in enumerate(top_3_laps.iterrows(), 1):
    print(f"{i}. Driver {lap['Driver']} - {lap['LapTime']}")

print("\n[DONE] Check the PNG file in your folder")