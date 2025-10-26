#!/usr/bin/env python3
"""
Security Vulnerability Scanner - MVP Demo (45 minutes)
Repurposes IntelliAudit infrastructure for code security scanning
"""

import os
import re
import ast
import pandas as pd
from pathlib import Path
from typing import List, Dict, Any
from datetime import datetime
import json

# Simplified standalone version (no dependencies on sentence_transformers)
class SecuritySearchAgent:
    """Search agent for security vulnerabilities"""
    
    def __init__(self):
        self.load_knowledge_base()
    
    def load_knowledge_base(self):
        """Load security vulnerability patterns"""
        self.knowledge_base = {}
        
        # Common security vulnerability patterns
        vulnerabilities = [
            {
                'vulnerability_id': 'SQL-INJ-001',
                'name': 'SQL Injection',
                'description': 'User input directly concatenated into SQL queries without sanitization',
                'severity': 'CRITICAL',
                'category': 'injection',
                'patterns': ['SELECT.*%s', 'WHERE.*\\+', 'query.*format']
            },
            {
                'vulnerability_id': 'XSS-001',
                'name': 'Cross-Site Scripting',
                'description': 'Unsanitized user input rendered in HTML output',
                'severity': 'HIGH',
                'category': 'xss',
                'patterns': ['innerHTML.*=', 'document.write', 'eval\\(']
            },
            {
                'vulnerability_id': 'CRYPTO-001',
                'name': 'Weak Cryptography',
                'description': 'Use of deprecated or weak cryptographic algorithms',
                'severity': 'MEDIUM',
                'category': 'cryptography',
                'patterns': ['MD5', 'SHA1', 'DES', 'RC4']
            },
            {
                'vulnerability_id': 'AUTH-001',
                'name': 'Weak Authentication',
                'description': 'Hardcoded credentials or weak password policies',
                'severity': 'HIGH',
                'category': 'authentication',
                'patterns': ['password.*=', 'secret.*=', 'api_key.*=']
            },
            {
                'vulnerability_id': 'PATH-001',
                'name': 'Path Traversal',
                'description': 'Unvalidated file path operations',
                'severity': 'HIGH',
                'category': 'path_traversal',
                'patterns': ['open\\(.*\\.\\..*\\)', 'file.*../', 'path.*join']
            }
        ]
        
        self.knowledge_base['vulnerabilities'] = pd.DataFrame(vulnerabilities)
        print(f"✓ Loaded {len(vulnerabilities)} security vulnerability patterns")

class SecurityAuditorAgent:
    """Auditor agent for security scanning"""
    
    def __init__(self, search_agent):
        self.search_agent = search_agent
    
    def scan_code_file(self, file_path: str, code_content: str) -> Dict[str, Any]:
        """Scan a single code file for security vulnerabilities"""
        
        findings = []
        lines = code_content.split('\n')
        
        # Get vulnerability patterns
        vulns_df = self.search_agent.knowledge_base.get('vulnerabilities', pd.DataFrame())
        
        for _, vuln in vulns_df.iterrows():
            for pattern in vuln.get('patterns', []):
                matches = re.finditer(pattern, code_content, re.IGNORECASE)
                for match in matches:
                    # Find line number
                    line_num = code_content[:match.start()].count('\n') + 1
                    
                    findings.append({
                        'vulnerability_id': vuln['vulnerability_id'],
                        'vulnerability_name': vuln['name'],
                        'severity': vuln['severity'],
                        'category': vuln['category'],
                        'file': file_path,
                        'line': line_num,
                        'code_snippet': lines[line_num - 1] if line_num <= len(lines) else '',
                        'pattern_matched': pattern
                    })
        
        # Calculate security score
        critical_count = len([f for f in findings if f['severity'] == 'CRITICAL'])
        high_count = len([f for f in findings if f['severity'] == 'HIGH'])
        medium_count = len([f for f in findings if f['severity'] == 'MEDIUM'])
        
        # Score: 100 - (critical*20 + high*10 + medium*5)
        security_score = max(0, 100 - (critical_count * 20 + high_count * 10 + medium_count * 5))
        
        return {
            'file': file_path,
            'security_score': security_score,
            'findings': findings,
            'total_vulnerabilities': len(findings),
            'critical_count': critical_count,
            'high_count': high_count,
            'medium_count': medium_count
        }

class SecurityJudgeAgent:
    """Judge agent that evaluates overall codebase security"""
    
    def __init__(self, auditor_agent):
        self.auditor_agent = auditor_agent
    
    def evaluate_codebase(self, scan_results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Evaluate overall codebase security"""
        
        # Aggregate results
        total_files = len(scan_results)
        total_findings = sum(r['total_vulnerabilities'] for r in scan_results)
        avg_security_score = sum(r['security_score'] for r in scan_results) / total_files if total_files > 0 else 0
        
        all_findings = []
        for result in scan_results:
            all_findings.extend(result['findings'])
        
        # Categorize by severity
        by_severity = {
            'CRITICAL': [f for f in all_findings if f['severity'] == 'CRITICAL'],
            'HIGH': [f for f in all_findings if f['severity'] == 'HIGH'],
            'MEDIUM': [f for f in all_findings if f['severity'] == 'MEDIUM']
        }
        
        # Determine overall security status
        if by_severity['CRITICAL']:
            overall_status = 'CRITICAL_ISSUES_FOUND'
        elif by_severity['HIGH']:
            overall_status = 'HIGH_RISK_ISSUES'
        elif by_severity['MEDIUM']:
            overall_status = 'MEDIUM_RISK_ISSUES'
        else:
            overall_status = 'NO_CRITICAL_ISSUES'
        
        return {
            'timestamp': datetime.now().isoformat(),
            'overall_status': overall_status,
            'overall_security_score': round(avg_security_score, 2),
            'total_files_scanned': total_files,
            'total_vulnerabilities': total_findings,
            'breakdown': {
                'critical': len(by_severity['CRITICAL']),
                'high': len(by_severity['HIGH']),
                'medium': len(by_severity['MEDIUM'])
            },
            'vulnerabilities_by_severity': by_severity,
            'files_scanned': [r['file'] for r in scan_results]
        }

def scan_directory(directory: str) -> Dict[str, Any]:
    """Scan a directory for security vulnerabilities"""
    
    print("🔒 Starting Security Vulnerability Scanner...")
    print("=" * 60)
    
    # Initialize agents
    search_agent = SecuritySearchAgent()
    auditor_agent = SecurityAuditorAgent(search_agent)
    judge_agent = SecurityJudgeAgent(auditor_agent)
    
    # Find all code files
    code_extensions = {'.py', '.js', '.java', '.cpp', '.c', '.cs', '.php', '.rb'}
    code_files = []
    
    for ext in code_extensions:
        code_files.extend(Path(directory).rglob(f'*{ext}'))
    
    if not code_files:
        print("⚠ No code files found to scan")
        return {}
    
    print(f"📁 Found {len(code_files)} code files to scan")
    print("\n🔍 Scanning files for vulnerabilities...")
    
    scan_results = []
    for i, file_path in enumerate(code_files, 1):
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            result = auditor_agent.scan_code_file(str(file_path), content)
            scan_results.append(result)
            
            if result['total_vulnerabilities'] > 0:
                print(f"  {i}. {file_path.name}: {result['total_vulnerabilities']} vulnerabilities found (Score: {result['security_score']}/100)")
            else:
                print(f"  {i}. {file_path.name}: ✓ No vulnerabilities (Score: {result['security_score']}/100)")
        
        except Exception as e:
            print(f"  {i}. {file_path.name}: Error - {e}")
    
    # Judge evaluation
    print("\n⚖️ Generating security assessment...")
    assessment = judge_agent.evaluate_codebase(scan_results)
    
    # Display results
    print("\n" + "=" * 60)
    print("📊 SECURITY ASSESSMENT RESULTS")
    print("=" * 60)
    print(f"Overall Status: {assessment['overall_status']}")
    print(f"Security Score: {assessment['overall_security_score']}/100")
    print(f"Files Scanned: {assessment['total_files_scanned']}")
    print(f"Total Vulnerabilities: {assessment['total_vulnerabilities']}")
    print(f"\nBreakdown:")
    print(f"  🔴 Critical: {assessment['breakdown']['critical']}")
    print(f"  🟠 High: {assessment['breakdown']['high']}")
    print(f"  🟡 Medium: {assessment['breakdown']['medium']}")
    
    if assessment['vulnerabilities_by_severity']['CRITICAL']:
        print("\n🚨 CRITICAL VULNERABILITIES:")
        for vuln in assessment['vulnerabilities_by_severity']['CRITICAL'][:5]:
            print(f"  - {vuln['vulnerability_name']} in {vuln['file']}:{vuln['line']}")
    
    # Save report
    report_file = f"security_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(report_file, 'w') as f:
        json.dump(assessment, f, indent=2)
    
    print(f"\n✅ Report saved to: {report_file}")
    
    return assessment

def create_sample_vulnerable_code():
    """Create sample code with vulnerabilities for demo"""
    os.makedirs('demo_code', exist_ok=True)
    
    # Sample vulnerable Python code
    vulnerable_code = '''
# Vulnerable application - DO NOT USE IN PRODUCTION
import sqlite3
import hashlib

def login(username, password):
    # SQL INJECTION VULNERABILITY
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    conn = sqlite3.connect('users.db')
    return conn.execute(query).fetchone()

def hash_password(password):
    # WEAK CRYPTOGRAPHY - MD5 is broken
    return hashlib.md5(password.encode()).hexdigest()

# HARDCODED CREDENTIALS
API_KEY = "sk-1234567890abcdef"
SECRET_PASSWORD = "admin123"

def render_user_input(user_input):
    # XSS VULNERABILITY
    return f"<div>Welcome {user_input}!</div>"

def read_file(filename):
    # PATH TRAVERSAL VULNERABILITY
    with open(filename, 'r') as f:
        return f.read()
'''
    
    with open('demo_code/vulnerable_app.py', 'w') as f:
        f.write(vulnerable_code)
    
    print("✓ Created demo vulnerable code file: demo_code/vulnerable_app.py")

def main():
    """Main execution"""
    import sys
    
    print("🔒 Security Vulnerability Scanner MVP")
    print("=" * 60)
    
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        # Use demo code
        create_sample_vulnerable_code()
        directory = 'demo_code'
    
    scan_directory(directory)

if __name__ == "__main__":
    main()
