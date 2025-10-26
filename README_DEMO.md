Security Vulnerability Scanner - Demo

Quick Start

bash
cd IntelliAudit
python security_scanner_demo.py


What It Does

Repurposes the IntelliAudit multi-agent audit system for security vulnerability scanning.

Key Features:
-  Scans code for security vulnerabilities
-  Detects SQL injection, hardcoded credentials, weak crypto
-  Multi-file scanning with progress tracking
- Security scoring (0-100)
-  JSON report generation


\`\`\`
 Starting Security Vulnerability Scanner...
============================================================
 Loaded 5 security vulnerability patterns
 Found 2 code files to scan

 Scanning files for vulnerabilities...
  1. vulnerable_app.py: 6 vulnerabilities found (Score: 50/100)
  2. vulnerable.py: 3 vulnerabilities found (Score: 70/100)

 Generating security assessment...

============================================================
 SECURITY ASSESSMENT RESULTS
============================================================
Overall Status: HIGH_RISK_ISSUES
Security Score: 60.0/100
Files Scanned: 2
Total Vulnerabilities: 9

Breakdown:
   Critical: 0
  High: 7
   Medium: 2
\`\`\`

## Repurposing IntelliAudit

| Original | Security Scanner |
|----------|------------------|
| ISO Control Evaluation | Vulnerability Detection |
| Evidence Gathering | Pattern Matching |
| Compliance Scoring | Security Risk Scoring |
| Auditor Agent | Vulnerability Scanner |
| Judge Agent | Risk Assessment |

## Data Science Elements

- Pattern matching algorithms
- Statistical aggregation
- Risk scoring models
- Classification algorithms
- Report generation
