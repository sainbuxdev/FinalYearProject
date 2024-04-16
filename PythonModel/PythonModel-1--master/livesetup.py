import subprocess

# Define your IP camera stream URL
# This is a placeholder URL; you'll need to replace it with your actual IP camera stream URL
ip_camera_url = 'rtsp://192.168.204.191:8080/h264_pcm.sdp'

# Define the command, setting the IP camera stream URL as the source
command = [
    'python', 'yolov5/detect.py',
    '--source', ip_camera_url,  # Using the IP camera stream URL as the source
    '--weights', 'models/best1.pt',
    '--conf', '0.2'
]

# Run the command
subprocess.run(command, check=True)
