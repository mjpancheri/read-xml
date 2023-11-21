import xml.etree.ElementTree as ET
import subprocess
import os
import sys

path = "."
file = "consolidated.xml"
xml_url = f"https://scsanctions.un.org/resources/xml/en/{file}"
file_path = f"{path}/{file}"

if len(sys.argv) > 1 and sys.argv[1] == "help":
    print("Usage: python get_last_update_onu.py [option]")
    print(
        "option: use wget or curl (default) to download new xml or check-only to use previews xml"
    )
    sys.exit()

if len(sys.argv) < 2 or sys.argv[1] != "check-only":
    # delete old file
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"The file at {file_path} has been deleted.")

    # download new file
    if len(sys.argv) > 1 and sys.argv[1] == "wget":
        download_command = f"wget {xml_url} -P {path}"
    else:
        download_command = f"curl {xml_url} > {file}"

    try:
        subprocess.run(download_command, shell=True, check=True)
        print("Download completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

# evaluate xml
print("Evaluating xml from ONU...")

tree = ET.parse(file_path)
root = tree.getroot()

date_generated = root.get("dateGenerated")
last_update = ""  # next(root.iter("LAST_DAY_UPDATED")).find("VALUE").text

# find last day updated
for last_day_updated in root.iter("LAST_DAY_UPDATED"):
    for date in last_day_updated.findall("VALUE"):
        if date.text != None and date.text > last_update:
            last_update = date.text

print(f"Date generated: {date_generated}")
print(f"Last update: {last_update}")
print("Done")
