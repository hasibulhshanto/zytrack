import subprocess

# Run both scripts concurrently
process1 = subprocess.Popen(["python", "forget_pass.py"])
process2 = subprocess.Popen(["python", "login_logout.py"])

# Wait for both processes to complete
process1.wait()
process2.wait()
####Suman