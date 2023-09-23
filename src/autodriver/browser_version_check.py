import subprocess
import re


# Replace the command below with the one you want to run
command_for_chrome = '''reg query "HKEY_CURRENT_USER\Software\Google\Chrome\BLBeacon" /v version'''  # Example: Running the "dir" command on Windows
command_for_firefox = '''reg query "HKEY_CURRENT_USER\Software\Mozilla" /s | findstr /i firefox | more'''  # Example: Running the "dir" command on Windows
command_for_edge = '''reg query HKCU\Software\Microsoft\Edge\BLBeacon /v version'''  # Example: Running the "dir" command on Windows

try:
    # Run the command and capture chrome version output
    chrome_version = subprocess.check_output(command_for_chrome, shell=True, text=True)
    global chrome_browser_version
    chrome_browser_version = re.sub(r'[^0-9.]', '', chrome_version)
    # Run the command and capture firefox version output
    # firefox_version = subprocess.check_output(command_for_firefox, shell=True, text=True)
    # firefox_browser_version = firefox_version[-7:]
    # Run the command and capture edge version output
    edge_version = subprocess.check_output(command_for_edge, shell=True, text=True)
    global edge_browser_version
    edge_browser_version = re.sub(r'[^0-9.]', '', edge_version)
    # Print the output to the console
    print("chrome version is ", chrome_browser_version)
    # print("firefox version is ", firefox_browser_version)
    print("edge version is ", edge_browser_version)

except subprocess.CalledProcessError as e:
    # Handle any errors, such as command not found
    print("Error:", e)
