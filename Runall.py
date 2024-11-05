import subprocess

# Run both scripts concurrently
process1 = subprocess.Popen(["python", "Login & Logout.py"])
process2 = subprocess.Popen(["python", "Forget Password.py"])

# Wait for both processes to complete
process1.wait()
process2.wait()
