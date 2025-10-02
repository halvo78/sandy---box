"""
Ultimate Lyra Trading System - Commissioning Audit Phase 1: Deep System Inspection
wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEYwJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY====
Verifies the integrity and completeness of all system components.
"""

import os
import json
import subprocess

# --- Configuration ---
SYSTEM_COMPONENTS = {
    "AI Enhanced Dashboard": {
        "port": 8751,
        "process_name": "ULTIMATE_DASHBOARD_SIMPLE.py",
        "files": [
            "ULTIMATE_DASHBOARD_SIMPLE.py",
            ".env.production",
            "nginx.conf",
        ],
    },
    "Maximum Amplification System": {
        "port": 9996,
        "process_name": "MAXIMUM_AMPLIFICATION_SYSTEM.py",
        "files": [
            "MAXIMUM_AMPLIFICATION_SYSTEM.py",
            ".env.production",
        ],
    },
    "Hummingbot Integration System": {
        "port": 8400,
        "process_name": "HUMMINGBOT_INTEGRATION_SYSTEM.py",
        "files": [
            "HUMMINGBOT_INTEGRATION_SYSTEM.py",
            ".env.production",
        ],
    },
}

REPORT_FILE = "/home/ubuntu/ultimate_lyra_v5/commissioning_phase1_report.md"

def run_command(command):
    """Run a shell command and return the output."""
    try:
        result = subprocess.run(
            command, shell=True, check=True, capture_output=True, text=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr.strip()}"

def verify_processes():
    """Verify that all system processes are running."""
    report = "### Process Verification\n\n"
    for name, details in SYSTEM_COMPONENTS.items():
        process_name = details["process_name"]
        output = run_command(f"ps aux | grep {process_name} | grep -v grep")
        if process_name in output:
            report += f"- ✅ **{name}:** Running\n"
        else:
            report += f"- ❌ **{name}:** Not running\n"
    return report + "\n"

def verify_ports():
    """Verify that all system ports are listening."""
    report = "### Port Verification\n\n"
    for name, details in SYSTEM_COMPONENTS.items():
        port = details["port"]
        output = run_command(f"netstat -tulpn | grep {port}")
        if f":{port}" in output:
            report += f"- ✅ **Port {port} ({name}):** Listening\n"
        else:
            report += f"- ❌ **Port {port} ({name}):** Not listening\n"
    return report + "\n"

def verify_files():
    """Verify that all system files exist."""
    report = "### File Verification\n\n"
    for name, details in SYSTEM_COMPONENTS.items():
        report += f"**{name}:**\n"
        for file_path in details["files"]:
            full_path = f"/home/ubuntu/ultimate_lyra_v5/{file_path}"
            if os.path.exists(full_path):
                report += f"- ✅ {file_path}\n"
            else:
                report += f"- ❌ {file_path} (Missing)\n"
    return report + "\n"

def generate_report():
    """Generate the final verification report."""
    report = "# Commissioning Audit Phase 1: Deep System Inspection Report\n\n"
    report += "**Verification Date:** $(date +'%Y-%m-%d %H:%M:%S')\n"
    report += "**Status:** In Progress\n\n"

    report += verify_processes()
    report += verify_ports()
    report += verify_files()

    with open(REPORT_FILE, "w") as f:
        f.write(report)

    print(f"📋 Phase 1 verification report saved to: {REPORT_FILE}")

if __name__ == "__main__":
    generate_report()

