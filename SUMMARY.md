# Security Scanner Summary

## What This Is

A repurposed version of IntelliAudit that scans code for security vulnerabilities instead of auditing ISO controls.

## Quick Usage

\`\`\`bash
cd security_scanner
python security_scanner_demo.py
\`\`\`

## What Gets Scanned

- SQL Injection
- Hardcoded credentials
- Weak cryptography
- Dangerous code execution
- Path traversal

## Output

Generates JSON reports with:
- Vulnerability counts by severity
- Security scores (0-100)
- File-by-file breakdowns

## Files in This Folder

- `security_scanner_demo.py` - Main scanner
- `demo_code/` - Sample vulnerable code
- `security_report_*.json` - Generated reports
- `README.md` - Full documentation
