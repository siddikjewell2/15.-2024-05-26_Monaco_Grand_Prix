import matplotlib
matplotlib.use('Agg')
import fastf1
import matplotlib.pyplot as plt
import os

os.makedirs("cache", exist_ok=True)
fastf1.Cache.enable_cache("cache")

print("Loading data...")
session = fastf1.get_session(2024, "Monaco", "Q")
session.load()

lap = session.laps.pick_fastest()
driver = lap['Driver']
print(f"Fastest lap: Driver {driver}")

pos = lap.get_pos_data()

print("Drawing track...")
plt.figure(figsize=(12, 10))
plt.plot(pos['X'], pos['Y'], linewidth=4, color='red')
plt.axis('equal')
plt.title(f"Monaco GP Track - Fastest Lap ({driver})")
plt.xlabel("X (meters)")
plt.ylabel("Y (meters)")
plt.grid(True, alpha=0.3)

filename = "monaco_track.png"
plt.savefig(filename, dpi=150)
print(f"SUCCESS! Image saved: {filename}")
print(f"Location: {os.path.abspath(filename)}")

# ড্রাইভার তথ্য
print("\nTop 3 Drivers:")
top_3 = session.laps.nsmallest(3, 'LapTime')
for i, (idx, lap) in enumerate(top_3.iterrows(), 1):
    print(f"{i}. Driver {lap['Driver']} - {lap['LapTime']}")