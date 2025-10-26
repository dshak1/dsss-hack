# 🔒 Security Vulnerability Scanner

## Overview

This security scanner repurposes the IntelliAudit multi-agent system for code security vulnerability detection. It demonstrates how the same core infrastructure can be applied to completely different domains.

## Quick Start

\`\`\`bash
cd security_scanner
python security_scanner_demo.py
\`\`\`

This will:
1. Create demo vulnerable code
2. Scan it for security issues
3. Generate a security report

## Files

### Core Files
- **`security_scanner_demo.py`** - Main security scanner with multi-agent architecture
- **`security_orchestrator.py`** - Orchestrator for security scanning (alternative implementation)

### Demo Files
- **`demo_code/`** - Sample vulnerable code for testing
- **`security_report_*.json`** - Generated security reports

## What It Does

The scanner detects common security vulnerabilities in code:
- SQL Injection vulnerabilities
- Hardcoded credentials
- Weak cryptography (MD5, SHA1)
- Dangerous code execution (eval, exec)
- Path traversal vulnerabilities

## Key Features

- ✅ Multi-file scanning
- ✅ Security scoring (0-100)
- ✅ Severity classification (CRITICAL, HIGH, MEDIUM)
- ✅ JSON report generation
- ✅ Progress tracking
- ✅ No external dependencies required
