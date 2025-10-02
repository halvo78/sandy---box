"""
Ultimate Lyra Trading System - Commissioning Audit Phase 5: Security & Compliance
================================================================================
Verifies all security settings and compliance documentation.
"""

import os
from dotenv import load_dotenv

# --- Configuration ---
ENV_FILE = "/home/ubuntu/ultimate_lyra_v5/.env.production"
REPORT_FILE = "/home/ubuntu/ultimate_lyra_v5/commissioning_phase5_report.md"
LOGS_DIR = "/home/ubuntu/ultimate_lyra_v5/logs"

# Expected security settings
EXPECTED_SECURITY_SETTINGS = {
    'ENCRYPTION_ENABLED': ('true', 'boolean'),
    'MFA_REQUIRED': ('true', 'boolean'),
    'SESSION_TIMEOUT': (3600, 'integer'),
    'AUDIT_LOGGING': ('true', 'boolean'),
}

# Expected compliance and security files
EXPECTED_FILES = {
    "ISO 27001 Compliance Document": "/home/ubuntu/ultimate_lyra_v5/iso_27001_compliance.md",
    "NGINX Configuration": "/home/ubuntu/ultimate_lyra_v5/nginx.conf",
}

def load_env():
    """Load environment variables from .env.production file."""
    load_dotenv(dotenv_path=ENV_FILE)

def verify_security_env_vars():
    """Verify that security environment variables are correctly set."""
    report = "### Security Parameter Verification (.env)\n\n"
    all_ok = True
    for key, (expected_value, value_type) in EXPECTED_SECURITY_SETTINGS.items():
        env_value_str = os.getenv(key)
        if env_value_str is None:
            report += f"- ❌ **{key}:** Not found in .env file\n"
            all_ok = False
            continue

        try:
            if value_type == 'boolean':
                env_value = env_value_str.lower() == 'true'
                expected_value = str(expected_value).lower() == 'true'
            elif value_type == 'integer':
                env_value = int(env_value_str)
            else:
                env_value = env_value_str

            if env_value == expected_value:
                report += f"- ✅ **{key}:** Correctly set to `{env_value}`\n"
            else:
                report += f"- ❌ **{key}:** Incorrectly set to `{env_value}` (Expected: `{expected_value}`)\n"
                all_ok = False
        except (ValueError, TypeError):
            report += f"- ❌ **{key}:** Invalid value format (`{env_value_str}`)\n"
            all_ok = False
            
    return report + "\n", all_ok

def verify_compliance_files():
    """Verify the existence of critical compliance and security files."""
    report = "### Compliance & Security File Verification\n\n"
    for name, path in EXPECTED_FILES.items():
        if os.path.exists(path):
            report += f"- ✅ **{name}:** Found at `{path}`\n"
        else:
            report += f"- ❌ **{name}:** Not found at `{path}`\n"
    return report + "\n"

def verify_audit_logging():
    """Verify that audit logs are being generated."""
    report = "### Audit Logging Verification\n\n"
    if not os.path.isdir(LOGS_DIR):
        report += f"- ❌ **Log Directory:** Not found at `{LOGS_DIR}`\n"
        return report + "\n"

    log_files = [f for f in os.listdir(LOGS_DIR) if f.endswith('.log')]
    if not log_files:
        report += f"- ❌ **Log Files:** No `.log` files found in `{LOGS_DIR}`.\n"
    else:
        report += f"- ✅ **Log Directory:** Found at `{LOGS_DIR}`.\n"
        report += f"- ✅ **Log Files:** Found {len(log_files)} log file(s). Example: `{log_files[0]}`\n"
        # Check if a recent log has content
        try:
            latest_log = max([os.path.join(LOGS_DIR, f) for f in log_files], key=os.path.getctime)
            if os.path.getsize(latest_log) > 0:
                report += f"- ✅ **Log Content:** The latest log file (`{os.path.basename(latest_log)}`) is not empty.\n"
            else:
                report += f"- 🟡 **Log Content:** The latest log file (`{os.path.basename(latest_log)}`) is empty.\n"
        except Exception as e:
            report += f"- ❌ **Log Content Check Failed:** {str(e)}\n"
            
    return report + "\n"

def generate_report():
    """Generate the final verification report for Phase 5."""
    load_env()
    report = "# Commissioning Audit Phase 5: Security & Compliance Report\n\n"
    report += f"**Verification Date:** $(date +'%Y-%m-%d %H:%M:%S')\n"
    report += "**Status:** In Progress\n\n"

    env_report, _ = verify_security_env_vars()
    report += env_report
    
    files_report = verify_compliance_files()
    report += files_report

    logs_report = verify_audit_logging()
    report += logs_report

    with open(REPORT_FILE, "w") as f:
        f.write(report)

    print(f"📋 Phase 5 verification report saved to: {REPORT_FILE}")

if __name__ == "__main__":
    generate_report()

