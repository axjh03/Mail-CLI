import pyfiglet
import time

# Define the frames of your ASCII GIF
frames = [
    pyfiglet.figlet_format("Frame 1"),
    pyfiglet.figlet_format("Frame 2"),
    pyfiglet.figlet_format("Frame 3"),
    pyfiglet.figlet_format("Frame 4")
]

# Set the delay between frames (in seconds)
delay = 0.5

# Print each frame in a loop
for frame in frames:
    # Clear the terminal screen
    print("\033c", end="")
    # Print the frame
    print(frame)
    # Wait for the specified delay
    time.sleep(delay)
