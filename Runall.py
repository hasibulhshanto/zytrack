import subprocess

# List of scripts to run
scripts = ["forget_pass.py", "login_logout.py", "edit_own_profile.py"]

# Start all scripts and store processes in a list
processes = [subprocess.Popen(["python", script]) for script in scripts]

# Wait for all processes to complete
for process in processes:
    process.wait()