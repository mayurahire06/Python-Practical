# Create a function that imports datetime and returns the current date and time.
# Example: current_datetime() should return the current timestamp like "2023-09-14 15:30:25"

from datetime import datetime

# Get the current date and time
now = datetime.now()
# Format it as "YYYY-MM-DD HH:MM:SS"
print(now.strftime("%Y-%m-%d %H:%M:%S"))


