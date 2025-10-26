#!/usr/bin/env python3
"""
Security Vulnerability Scanner Orchestrator
Repurposes IntelliAudit multi-agent system for code security scanning
"""

import os
import sys
from datetime import datetime
from typing import List, Dict, Any
from pathlib import Path










# Set up environment for LangSmith tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
# Add your LangSmith API key here
# os.environ["LANGCHAIN_API_KEY"] = "your-api-key-here"





# Import existing agents (will be modified for security)
from search_agent import SearchAgent
from auditor_agent import AuditorAgent
from defender_agent import DefenderAgent
from judge_agent import JudgeAgent







class SecurityOrchestrator:
    """Orchestrator for security vulnerability scanning"""
    
    def __init__(self):
        print(" Initializing Security Vulnerability Scanner...")
        
        # Initialize agents with security focus
        self.search_agent = SearchAgent(output_dir="")
        self.auditor_agent = AuditorAgent(self.search_agent)
        self.defender_agent = DefenderAgent(self.search_agent)
        self.judge_agent = JudgeAgent(self.search_agent, self.auditor_agent, self.defender_agent)
        
        print("Security scanner init success.  ")
    
    def scan_directory(self, directory: str) -> Dict[str, Any]:
        """Scan a directory for security vulnerabilities"""
        
        print(f"\n{'='*60}")
        print(f"scanning : {directory}")
        print(f"{'='*60}\n")
        
        # Find code files
        code_files = self._find_code_files(directory)
        








        if not code_files:
            print(" No code files found to scan")
            return {}
        
        print(f"Found {len(code_files)} code files to scan\n")
        
        # Scan files
        scan_results = []
        for i, file_path in enumerate(code_files, 1):
            print(f"[{i}/{len(code_files)}] Scanning: {file_path.name}")
            
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                # Use auditor agent to scan
                result = self._scan_file(str(file_path), content)
                scan_results.append(result)
                
                if result.get('vulnerabilities_found', 0) > 0:
                    print(f"    ⚠ Found {result['vulnerabilities_found']} vulnerabilities")
                else:
                    print(f"    ✓ No vulnerabilities found")
            
            except Exception as e:
                print(f" Error: {e}")
        
        # Generate assessment
        print(f"Generating security assessment...")
        assessment = self._generate_assessment(scan_results)
        
        # Print results
        self._print_results(assessment)
        
        return assessment
    
    def _find_code_files(self, directory: str) -> List[Path]:
        """Find all code files in directory"""
        code_extensions = {'.py', '.js', '.java', '.cpp', '.c', '.cs', '.php', '.rb', '.go', '.rs'}
        code_files = []
        
        for ext in code_extensions:
            code_files.extend(Path(directory).rglob(f'*{ext}'))
        
        return code_files
    
    def _scan_file(self, file_path: str, content: str) -> Dict[str, Any]:
        """Scan a single file using auditor agent logic"""
        
        # Simple vulnerability detection using auditor's evaluation framework
        vulnerabilities = []
        
        # Check for SQL injection patterns
        if 'SELECT' in content.upper() and ('%s' in content or '+' in content):
            vulnerabilities.append({
                'type': 'SQL Injection',
                'severity': 'CRITICAL',
                'description': 'Potential SQL injection vulnerability'
            })




        
        # Check for hardcoded credentials
        if any(keyword in content for keyword in ['password =', 'api_key =', 'secret =']):
            vulnerabilities.append({
                'type': 'Hardcoded Credentials',
                'severity': 'HIGH',
                'description': 'Potential hardcoded credentials'
            })
        
        # Check for weak cryptography
        if any(crypto in content for crypto in ['MD5', 'SHA1', 'DES']):
            vulnerabilities.append({
                'type': 'Weak Cryptography',
                'severity': 'MEDIUM',
                'description': 'Use of weak cryptographic algorithms'
            })
        # Check for eval usage
        if 'eval(' in content:
            vulnerabilities.append({
                'type': 'Dangerous Code Execution',
                'severity': 'CRITICAL',
                'description': 'Use of eval() can lead to code injection'
            })
        


        return {
            'file': file_path,
            'vulnerabilities_found': len(vulnerabilities),
            'vulnerabilities': vulnerabilities,
            'security_score': max(0, 100 - (len(vulnerabilities) * 25))
        }
    


    #make an acutal assessement 
    def _generate_assessment(self, scan_results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Generate security assessment using judge agent logic"""
        
        total_vulnerabilities = sum(r['vulnerabilities_found'] for r in scan_results)
        avg_score = sum(r['security_score'] for r in scan_results) / len(scan_results) if scan_results else 0
        


        all_vulns = []
        for result in scan_results:
            all_vulns.extend(result.get('vulnerabilities', []))
        
        by_severity = {
            'CRITICAL': [v for v in all_vulns if v['severity'] == 'CRITICAL'],
            'HIGH': [v for v in all_vulns if v['severity'] == 'HIGH'],
            'MEDIUM': [v for v in all_vulns if v['severity'] == 'MEDIUM']
        }





        # basic rundown of issues
        
        if by_severity['CRITICAL']:
            status = 'CRITICAL_ISSUES_FOUND'
        elif by_severity['HIGH']:
            status = 'HIGH_RISK_ISSUES'
        elif by_severity['MEDIUM']:
            status = 'MEDIUM_RISK_ISSUES'
        else:
            status = 'NO_CRITICAL_ISSUES'
        
        return {
            'timestamp': datetime.now().isoformat(),
            'status': status,
            'security_score': round(avg_score, 2),
            'files_scanned': len(scan_results),
            'total_vulnerabilities': total_vulnerabilities,
            'breakdown': {
                'critical': len(by_severity['CRITICAL']),
                'high': len(by_severity['HIGH']),
                'medium': len(by_severity['MEDIUM'])
            },
            'details': by_severity,
            'files': scan_results


        }
    
    def _print_results(self, assessment: Dict[str, Any]):
        """Print assessment results"""
        
        print(f"\n{'='*60}")
        print(" SECURITY ASSESSMENT RESULTS")
        print(f"{'='*60}")
        print(f"Status: {assessment['status']}")
        print(f"Security Score: {assessment['security_score']}/100")
        print(f"Files Scanned: {assessment['files_scanned']}")
        print(f"Total Vulnerabilities: {assessment['total_vulnerabilities']}")
        print(f"\nBreakdown:")
        print(f"   Critical: {assessment['breakdown']['critical']}")
        print(f"   High: {assessment['breakdown']['high']}")
        print(f"   Medium: {assessment['breakdown']['medium']}")
        
        if assessment['details']['CRITICAL']:
            print(f"\nCRITICAL VULNERABILITIES:")
            for vuln in assessment['details']['CRITICAL'][:5]:
                print(f"  - {vuln['type']}: {vuln['description']}")
        
        print(f"\n{'='*60}")


def main():
    """Main execution"""
    import sys
    
    print(" Security Vulnerability Scanner")
    print("Repurposed from IntelliAudit Multi-Agent System")
    print("=" * 60)
    
    # Get directory to scan
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        # Default to current directory
        directory = "."
    
    # Initialize orchestrator
    orchestrator = SecurityOrchestrator()
    
    # Run scan
    results = orchestrator.scan_directory(directory)
    
    print("\n Scan complete!")


if __name__ == "__main__":
    main()
