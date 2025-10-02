#!/usr/bin/env python3

import json
import re

def analyze_compliance_gap():
    """Analyzes the ISO 27001 compliance gap."""

    # Read the compliance verification report
    with open("/home/ubuntu/ultimate_lyra_systems/logs/compliance_verification_report.json", "r") as f:
        compliance_report = json.load(f)

    # Read the ISO 27001 controls list
    with open("/home/ubuntu/iso_27001_controls.md", "r") as f:
        iso_controls_raw = f.read()

    # Extract control titles from the markdown file
    iso_controls = re.findall(r"\*\*\[(.*?)\]\(\)\*\*", iso_controls_raw)

    # Extract implemented features from the compliance report
    implemented_features = []
    for service in compliance_report["deployed_services"].values():
        implemented_features.extend(service["features"])

    # A simple mapping of keywords in implemented features to ISO controls
    # This is a simplified approach for demonstration purposes
    keyword_to_control = {
        "monitoring": ["Physical security monitoring", "Monitoring activities"],
        "Health checks": ["Information security during disruption"],
        "Service coordination": ["Information security in project management"],
        "Live trading connection": ["Security of network services"],
        "Balance tracking": ["Inventory of information and other associated assets"],
        "Spot trading only": ["Access control"],
        "AI models": ["Use of cryptography"],
        "Consensus system": ["Information security roles and responsibilities"],
        "Portfolio optimization": ["Management responsibilities"],
        "Risk analysis": ["Management of technical vulnerabilities"],
        "Market opportunities": ["Threat intelligence"]
    }

    implemented_controls = set()
    for feature in implemented_features:
        for keyword, controls in keyword_to_control.items():
            if keyword in feature.lower():
                for control in controls:
                    implemented_controls.add(control)

    # Identify missing controls
    missing_controls = [control for control in iso_controls if control not in implemented_controls]

    # Calculate the compliance gap
    total_controls = len(iso_controls)
    if total_controls == 0:
        print("Error: No ISO controls found. Please check the regex and the input file.")
        return

    missing_count = len(missing_controls)
    compliance_gap = (missing_count / total_controls) * 100

    # Generate the report
    report = f"""# ISO 27001 Compliance Gap Analysis

**Total Controls:** {total_controls}
**Implemented Controls:** {total_controls - missing_count}
**Missing Controls:** {missing_count}
**Compliance Gap:** {compliance_gap:.2f}%

## Missing Controls:

"""
    for control in missing_controls:
        report += f"- {control}\n"

    with open("/home/ubuntu/compliance_gap_report.md", "w") as f:
        f.write(report)

    print("Compliance gap analysis complete. Report generated at /home/ubuntu/compliance_gap_report.md")

if __name__ == "__main__":
    analyze_compliance_gap()

