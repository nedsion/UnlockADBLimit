import subprocess
import winreg

# Kill the ADB server with elevated privileges
subprocess.run(["powershell", "Start-Process", "adb", "-ArgumentList", "kill-server", "-Verb", "RunAs"])

# Set the variable name and value
variable_name = "ADB_LOCAL_TRANSPORT_MAX_PORT"
variable_value = "6000"

# Add the variable to the user environment
try:
    key_path = r"Environment"
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE) as reg_key:
        winreg.SetValueEx(reg_key, variable_name, 0, winreg.REG_EXPAND_SZ, variable_value)
except Exception as e:
    print(f"Error updating environment variable: {e}")

print(f"Variable added to user environment: {variable_name}={variable_value}")
