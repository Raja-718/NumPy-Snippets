import numpy as np
import datetime

# Step 1: Show date, time, and day info
now = datetime.datetime.now()
current_day = now.strftime("%A")
current_date = now.strftime("%d %B %Y")
current_time = now.strftime("%I:%M %p")

# Year progress
day_of_year = now.timetuple().tm_yday
year_progress = (day_of_year / 365) * 100

# Greeting & date info
print("📅 Welcome to the Temperature Converter & Date Assistant!")
print(f"Today is {current_day}, {current_date} | Time: {current_time}")
print(f"📈 Year Progress: {year_progress:.1f}%\n")

# Step 2: Get temperature inputs from user
print("🌡️ Enter temperatures in Celsius one by one. Type 'ok' to convert.\n")
temps = []

while True:
    entry = input("Enter temperature (Celsius): ").strip()
    if entry.lower() == 'ok':
        break
    try:
        temps.append(float(entry))
    except ValueError:
        print("⚠️ Please enter a valid number or 'ok'.")

if not temps:
    print("❌ No temperatures provided.")
    exit()

# Step 3: Convert to Fahrenheit using NumPy
celsius = np.array(temps)
fahrenheit = (celsius * 9 / 5) + 32

# Step 4: Display results
print("\n🌤️ Temperature Conversion Results:")
for c, f in zip(celsius, fahrenheit):
    print(f" {c}°C  →  {f:.2f}°F")

# Step 5: Show a random motivational quote
quotes = np.array([
    "Believe you can and you're halfway there.",
    "Start where you are. Use what you have. Do what you can.",
    "Success is not final; failure is not fatal: It is the courage to continue that counts.",
    "Push yourself, because no one else is going to do it for you.",
    "Every day is a second chance."
])

quote = np.random.choice(quotes)
print(f"\n💡 Quote of the Moment:\n\"{quote}\"")
