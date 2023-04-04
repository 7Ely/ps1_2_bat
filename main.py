file = input("Enter the file path: ")

with open(file, "r", encoding="utf-8", errors="ignore") as f:
    lines = f.readlines()

stripped = [line.strip() for line in lines]
remove_all_empty_lines = [line for line in stripped if line != ""]
replace_all = [
    line.replace("|", "^|")
    .replace(">", "^>")
    .replace("<", "^<")
    .replace("&", "^&")
    .replace("%", "%%")
    for line in remove_all_empty_lines
]

convert_to_bat = file.replace(".ps1", ".bat")

with open(convert_to_bat, "w+", encoding="utf-8", errors="ignore") as f:
    for index, line in enumerate(replace_all):
        if index == 0:
            f.write("@echo off\necho " + line + " > powershell123.ps1\n")
        else:
            f.write("echo " + line + " >> powershell123.ps1\n")
    f.write(
        "powershell Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted -Force\npowershell.exe -executionpolicy bypass -WindowStyle hidden -file powershell123.ps1\ndel powershell123.ps1 /f /q\ntimeout 3 > nul\nexit"
    )
    print("Converted to " + convert_to_bat)
