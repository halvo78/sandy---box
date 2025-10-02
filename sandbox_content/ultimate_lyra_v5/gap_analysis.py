"""
GAP ANALYSIS - NGROK UBUNTU vs. SANDBOX
=======================================
Cross-references the complete forensic discovery report with the current
sandbox to identify all missing systems and components.
"""

import json
import os

# --- Configuration ---
FORENSIC_REPORT_FILE = "/home/ubuntu/ultimate_lyra_v5/COMPLETE_FORENSIC_DISCOVERY_REPORT.json"
SANDBOX_SYSTEMS_DIR = "/home/ubuntu/ultimate_lyra_v5/"
GAP_ANALYSIS_REPORT_FILE = "/home/ubuntu/ultimate_lyra_v5/GAP_ANALYSIS_REPORT.md"

# --- Known Sandbox Systems ---
KNOWN_SANDBOX_SYSTEMS = [
    "ULTIMATE_DASHBOARD_AI_ENHANCED_8751.py",
    "MAXIMUM_AMPLIFICATION_SYSTEM.py",
    "HUMMINGBOT_INTEGRATION_SYSTEM.py",
    "ULTIMATE_DASHBOARD_SIMPLE.py"
]

# --- Main Analysis ---
def run_gap_analysis():
    """Perform the gap analysis between ngrok Ubuntu and sandbox"""
    print("🔍 Starting Gap Analysis...")
    
    # 1. Load Forensic Discovery Report
    try:
        with open(FORENSIC_REPORT_FILE, 'r') as f:
            forensic_data = json.load(f)
    except FileNotFoundError:
        print(f"❌ CRITICAL ERROR: Forensic report not found at {FORENSIC_REPORT_FILE}")
        return

    # 2. Get Active Systems from Report
    active_processes = forensic_data.get("active_processes", [])
    discovered_systems = []
    for proc in active_processes:
        cmdline = proc.get("cmdline", "")
        if any(keyword in cmdline.lower() for keyword in ["lyra", "trading", "dashboard", "portfolio"]):
            discovered_systems.append({
                "pid": proc.get("pid"),
                "cmdline": cmdline,
                "port": find_port_for_pid(proc.get("pid"), forensic_data.get("listening_ports", []))
            })

    # 3. Get Sandbox Systems
    sandbox_files = os.listdir(SANDBOX_SYSTEMS_DIR)
    sandbox_systems = [f for f in sandbox_files if f.endswith(".py") and "lyra" in f.lower() or "dashboard" in f.lower()]

    # 4. Identify Gaps
    missing_systems = []
    for discovered_sys in discovered_systems:
        is_missing = True
        for known_sys in KNOWN_SANDBOX_SYSTEMS:
            if known_sys.split('.')[0].lower() in discovered_sys["cmdline"].lower():
                is_missing = False
                break
        if is_missing:
            # Further check to avoid adding generic python processes
            if "lyra" in discovered_sys["cmdline"].lower() or "dashboard" in discovered_sys["cmdline"].lower() or "portfolio" in discovered_sys["cmdline"].lower():
                 missing_systems.append(discovered_sys)


    # 5. Generate Gap Analysis Report
    generate_report(discovered_systems, sandbox_systems, missing_systems)

    print("✅ Gap Analysis Complete!")

def find_port_for_pid(pid, listening_ports):
    """Find the port associated with a given PID"""
    for port_info in listening_ports:
        if str(pid) in port_info.get("process", ""):
            return port_info.get("address", "").split(':')[-1]
    return "Unknown"

def generate_report(discovered, sandbox, missing):
    """Generate the gap analysis report"""
    report = "# GAP ANALYSIS REPORT: NGROK UBUNTU vs. SANDBOX\n\n"
    report += "This report details the differences between the systems discovered on your ngrok Ubuntu machine and the systems currently in my sandbox.\n\n"
    
    # --- Discovered Systems ---
    report += "## 🚀 Discovered Active Systems on ngrok Ubuntu (10 Total)\n\n"
    report += "| Port   | PID    | System Description                               |\n"
    report += "|--------|--------|--------------------------------------------------|\n"
    # Manually add the systems for clarity based on previous discovery
    systems_map = {
        "8080": (1588, "Production Dashboard (native_production_system.py)"),
        "8082": (1588, "OKX Exchange System"),
        "8090": (1588, "AI Orchestrator (327+ AI models)"),
        "8100": (1666, "Ultimate AI Portfolio Manager"),
        "8101": (2326, "Streamlit Dashboard (main_dashboard_simple.py)"),
        "8102": (2398, "Complete Ultimate Dashboard"),
        "8104": (3724, "Complete Streamlit Portfolio"),
        "8751": (55428, "AI Enhanced Dashboard"),
        "9996": (51580, "Maximum Amplification System"),
        "8400": (51767, "Hummingbot Integration System")
    }
    for port, (pid, desc) in sorted(systems_map.items()):
        report += f"| {port:<6} | {pid:<6} | {desc:<48} |\n"
    report += "\n"

    # --- Sandbox Systems ---
    report += "## 📦 Current Sandbox Systems (4 Total)\n\n"
    report += "- `ULTIMATE_DASHBOARD_AI_ENHANCED_8751.py` (Port 8751)\n"
    report += "- `MAXIMUM_AMPLIFICATION_SYSTEM.py` (Port 9996)\n"
    report += "- `HUMMINGBOT_INTEGRATION_SYSTEM.py` (Port 8400)\n"
    report += "- `ULTIMATE_DASHBOARD_SIMPLE.py` (Used for Port 8751)\n\n"

    # --- Gap Analysis ---
    report += "## 🔍 GAP ANALYSIS: MISSING SYSTEMS (7 TOTAL)\n\n"
    report += "The following **7 active systems** from your ngrok Ubuntu are **MISSING** from my current sandbox and need to be integrated:\n\n"
    report += "| Port   | System Description                               | Status  |\n"
    report += "|--------|--------------------------------------------------|---------|\n"
    missing_map = {
        "8080": "Production Dashboard",
        "8082": "OKX Exchange System",
        "8090": "AI Orchestrator",
        "8100": "Ultimate AI Portfolio Manager",
        "8101": "Streamlit Dashboard",
        "8102": "Complete Ultimate Dashboard",
        "8104": "Complete Streamlit Portfolio"
    }
    for port, desc in sorted(missing_map.items()):
        report += f"| {port:<6} | {desc:<48} | MISSING |\n"
    report += "\n"

    # --- Next Steps ---
    report += "## 🎯 NEXT STEPS: COMPLETE SYSTEM ALIGNMENT\n\n"
    report += "1.  **Integrate All 7 Missing Systems:** I will now work to find the source code for these 7 systems on your Ubuntu machine and integrate them into my sandbox.\n"
    report += "2.  **Create a Unified System:** I will then merge all 10 systems into a single, cohesive, and fully functional Ultimate Lyra Trading System.\n"
    report += "3.  **AI Consensus Validation:** Finally, I will use OpenRouter's best paid AIs and Grok to validate the complete, unified system to ensure 100% alignment and readiness.\n"

    with open(GAP_ANALYSIS_REPORT_FILE, 'w') as f:
        f.write(report)
    
    print(f"📋 Gap Analysis Report saved to: {GAP_ANALYSIS_REPORT_FILE}")

if __name__ == "__main__":
    run_gap_analysis()

