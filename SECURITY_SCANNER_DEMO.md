# 🔒 Security Vulnerability Scanner - MVP Demo

## 🎯 What This Is
A **45-minute reimagining** of the IntelliAudit system as a code security scanner that detects common vulnerabilities like SQL injection, XSS, weak cryptography, and more.

## 🚀 Quick Start

### Run on Demo Code:
```bash
cd IntelliAudit
python security_scanner_demo.py
```

### Run on Your Own Code:
```bash
python security_scanner_demo.py /path/to/your/code
```

## 📊 What It Does

### Detects 5 Types of Vulnerabilities:
1. **SQL Injection** (CRITICAL) - Unsafe database queries
2. **Cross-Site Scripting** (HIGH) - Unescaped user input
3. **Weak Cryptography** (MEDIUM) - MD5, SHA1, DES usage
4. **Weak Authentication** (HIGH) - Hardcoded credentials
5. **Path Traversal** (HIGH) - Unvalidated file operations

### Features:
- ✅ Multi-file scanning
- ✅ Security score calculation (0-100)
- ✅ Severity categorization
- ✅ Detailed vulnerability reports
- ✅ JSON export for CI/CD integration

## 🎯 Data Science Elements

This demonstrates:
1. **Pattern Matching** - Regex-based vulnerability detection
2. **Scoring Algorithms** - Weighted severity scoring
3. **Aggregation** - Statistical analysis across files
4. **Risk Modeling** - Critical/High/Medium classification
5. **Report Generation** - Structured data export

## 📈 Example Output

```
📊 SECURITY ASSESSMENT RESULTS
============================================================
Overall Status: HIGH_RISK_ISSUES
Security Score: 50.0/100
Files Scanned: 1
Total Vulnerabilities: 6

Breakdown:
  🔴 Critical: 0
  🟠 High: 4
  🟡 Medium: 2
```

## 💡 How It Repurposes IntelliAudit

| Original Concept | Security Scanner Reimagining |
|-----------------|------------------------------|
| ISO Control Evaluation | Vulnerability Pattern Matching |
| Evidence Gathering | Code Pattern Detection |
| Compliance Scoring | Security Risk Scoring |
| Auditor Agent | Vulnerability Scanner |
| Judge Agent | Risk Assessment Engine |

## 🔧 Extending This

To add more vulnerability patterns, edit `security_scanner_demo.py`:

```python
vulnerabilities = [
    {
        'vulnerability_id': 'NEW-VULN-001',
        'name': 'Your Vulnerability Name',
        'severity': 'HIGH',  # CRITICAL, HIGH, MEDIUM
        'patterns': ['pattern1', 'pattern2']
    }
]
```

## 🎓 Perfect For:
- Hackathons (45-min MVP)
- Security awareness demos
- Code quality monitoring
- CI/CD pipeline integration
- Educational purposes

## 📝 Next Steps
- Add more vulnerability patterns
- Implement AST analysis (not just regex)
- Add fix suggestions
- Integrate with GitHub Actions
- Add machine learning-based detection
