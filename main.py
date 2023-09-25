import math

# Step 1: Define Variables
focal_length = float(input("Enter the Focal Length (in mm): "))
sensor_size = float(input("Enter the Sensor Size (in mm): "))
aperture = float(input("Enter the Aperture (f-number): "))
resolution_x = int(input("Enter the Resolution (width in pixels): "))
resolution_y = int(input("Enter the Resolution (height in pixels): "))
object_distance = float(input("Enter the Object Distance (in mm): "))

# Step 2: Calculate Angle of View
angle_of_view = 2 * math.atan(sensor_size / (2 * focal_length)) * (180 / math.pi)

# Step 3: Calculate Smallest Detail Size
smallest_detail_size = (object_distance * sensor_size) / (focal_length * resolution_x)

# Step 4: Display Results
print(f"Angle of View: {angle_of_view} degrees")
print(f"Smallest Detail Size: {smallest_detail_size} mm")
