import pygetwindow as gw

# List all open windows
windows = gw.getAllTitles()

# Display all open windows
print("Open windows:")
for win in windows:
    if win.strip():  # Filter out empty titles
        print(win)

# Example: Find a specific application (e.g., Notepad)
target_app = [win for win in windows if "Notepad" in win]

print(target_app)

# if target_app:
#     print(f"Found application: {target_app[0]}")
# else:
#     print("Application not found.")