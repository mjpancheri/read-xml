import xml.etree.ElementTree as ET
import subprocess
import os

path = "."
file = "consolidated.xml"
xml_url = f"https://scsanctions.un.org/resources/xml/en/{file}"
file_path = f"{path}/{file}"

# delete old file
if os.path.exists(file_path):
    os.remove(file_path)
    print(f"The file at {file_path} has been deleted.")

# download new file
wget_command = f"wget {xml_url} -P {path}"

try:
    subprocess.run(wget_command, shell=True, check=True)
    print("Download completed successfully.")
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")

# evaluate xml
print("Evaluating xml from ONU...")

tree = ET.parse(file_path)
root = tree.getroot()

last_update = ""  # next(root.iter("LAST_DAY_UPDATED")).find("VALUE").text

# find last day updated
for last_day_updated in root.iter("LAST_DAY_UPDATED"):
    for date in last_day_updated.findall("VALUE"):
        if date.text != None and date.text > last_update:
            last_update = date.text

print(f"Last update: {last_update}")
print("Done")
