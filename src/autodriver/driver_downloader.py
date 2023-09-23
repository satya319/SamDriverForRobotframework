import requests
import browser_version_check
import sys
import zipfile
import os


python_path = sys.executable
folder_location = python_path[:-10]
print("Python Installation Path:", folder_location)

# URL of the zip file to download
chrome_driver_url = "https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/"+ browser_version_check.chrome_browser_version + "/win32/chromedriver-win32.zip"
edge_driver_url = "https://msedgedriver.azureedge.net/"+ browser_version_check.edge_browser_version+"/edgedriver_win64.zip"
# Desired folder where you want to save the zip file
folder_path = folder_location

# Set the filename for the saved zip file
chrome_driver_file_name = "chromedriver_win32.zip"
# edge_driver_file_name = "edgedriver_win64.zip"

# Create the full path for the saved file
file_path = folder_path + chrome_driver_file_name

# Send a GET request to the URL to download the zip file
response = requests.get(chrome_driver_url, stream=True)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Open the file in binary write mode and save the downloaded content
    with open(file_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    
    print(f"Zip file downloaded and saved to {file_path}")
else:
    print("Failed to download the zip file")

# Path to the zip file you want to extract
zip_file_path = folder_location+"chromedriver_win32.zip"
print("zip file path is: ", zip_file_path)
try:
    # Get the directory containing the zip file
    zip_dir = os.path.dirname(zip_file_path)

    # Open the zip file for reading
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        # Extract all the contents to the directory containing the zip file
        zip_ref.extractall(folder_location)
    
    print(f"Zip file '{zip_file_path}' has been successfully extracted to '{folder_location}'.")
except Exception as e:
    print(f"An error occurred: {str(e)}")