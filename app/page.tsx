import { Shield, AlertTriangle, CheckCircle2, XCircle, FileCode, Clock } from "lucide-react"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { SecurityScoreCard } from "@/components/security-score-card"
import { VulnerabilityBreakdown } from "@/components/vulnerability-breakdown"
import { VulnerabilityList } from "@/components/vulnerability-list"
import { ScanSummary } from "@/components/scan-summary"

// Mock data from the security report
const mockScanData = {
  timestamp: "2025-10-25T17:51:19.841237",
  overall_status: "HIGH_RISK_ISSUES",
  overall_security_score: 60.0,
  total_files_scanned: 2,
  total_vulnerabilities: 9,
  breakdown: {
    critical: 0,
    high: 7,
    medium: 2,
  },
  vulnerabilities_by_severity: {
    CRITICAL: [],
    HIGH: [
      {
        vulnerability_id: "AUTH-001",
        vulnerability_name: "Weak Authentication",
        severity: "HIGH",
        category: "authentication",
        file: "demo_code/vulnerable_app.py",
        line: 8,
        code_snippet: "    query = f\"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'\"",
        pattern_matched: "password.*=",
      },
      {
        vulnerability_id: "AUTH-001",
        vulnerability_name: "Weak Authentication",
        severity: "HIGH",
        category: "authentication",
        file: "demo_code/vulnerable_app.py",
        line: 18,
        code_snippet: 'SECRET_PASSWORD = "admin123"',
        pattern_matched: "password.*=",
      },
      {
        vulnerability_id: "AUTH-001",
        vulnerability_name: "Weak Authentication",
        severity: "HIGH",
        category: "authentication",
        file: "demo_code/vulnerable_app.py",
        line: 18,
        code_snippet: 'SECRET_PASSWORD = "admin123"',
        pattern_matched: "secret.*=",
      },
      {
        vulnerability_id: "AUTH-001",
        vulnerability_name: "Weak Authentication",
        severity: "HIGH",
        category: "authentication",
        file: "demo_code/vulnerable_app.py",
        line: 17,
        code_snippet: 'API_KEY = "sk-1234567890abcdef"',
        pattern_matched: "api_key.*=",
      },
      {
        vulnerability_id: "AUTH-001",
        vulnerability_name: "Weak Authentication",
        severity: "HIGH",
        category: "authentication",
        file: "demo_code/vulnerable.py",
        line: 7,
        code_snippet: "    query = f\"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'\"",
        pattern_matched: "password.*=",
      },
      {
        vulnerability_id: "AUTH-001",
        vulnerability_name: "Weak Authentication",
        severity: "HIGH",
        category: "authentication",
        file: "demo_code/vulnerable.py",
        line: 11,
        code_snippet: 'password = "admin123"',
        pattern_matched: "password.*=",
      },
      {
        vulnerability_id: "AUTH-001",
        vulnerability_name: "Weak Authentication",
        severity: "HIGH",
        category: "authentication",
        file: "demo_code/vulnerable.py",
        line: 10,
        code_snippet: 'API_KEY = "sk-1234567890"',
        pattern_matched: "api_key.*=",
      },
    ],
    MEDIUM: [
      {
        vulnerability_id: "CRYPTO-001",
        vulnerability_name: "Weak Cryptography",
        severity: "MEDIUM",
        category: "cryptography",
        file: "demo_code/vulnerable_app.py",
        line: 13,
        code_snippet: "    # WEAK CRYPTOGRAPHY - MD5 is broken",
        pattern_matched: "MD5",
      },
      {
        vulnerability_id: "CRYPTO-001",
        vulnerability_name: "Weak Cryptography",
        severity: "MEDIUM",
        category: "cryptography",
        file: "demo_code/vulnerable_app.py",
        line: 14,
        code_snippet: "    return hashlib.md5(password.encode()).hexdigest()",
        pattern_matched: "MD5",
      },
    ],
  },
  files_scanned: ["demo_code/vulnerable_app.py", "demo_code/vulnerable.py"],
}

export default function SecurityDashboard() {
  const statusConfig = {
    CRITICAL_ISSUES_FOUND: {
      icon: XCircle,
      color: "text-red-500",
      bgColor: "bg-red-500/10",
      label: "Critical Issues Found",
    },
    HIGH_RISK_ISSUES: {
      icon: AlertTriangle,
      color: "text-orange-500",
      bgColor: "bg-orange-500/10",
      label: "High Risk Issues",
    },
    MEDIUM_RISK_ISSUES: {
      icon: AlertTriangle,
      color: "text-yellow-500",
      bgColor: "bg-yellow-500/10",
      label: "Medium Risk Issues",
    },
    NO_CRITICAL_ISSUES: {
      icon: CheckCircle2,
      color: "text-green-500",
      bgColor: "bg-green-500/10",
      label: "No Critical Issues",
    },
  }

  const status = statusConfig[mockScanData.overall_status as keyof typeof statusConfig]
  const StatusIcon = status.icon

  return (
    <div className="min-h-screen bg-background">
      {/* Header */}
      <header className="border-b border-border bg-card">
        <div className="container mx-auto px-6 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-3">
              <div className="flex h-10 w-10 items-center justify-center rounded-lg bg-primary">
                <Shield className="h-6 w-6 text-primary-foreground" />
              </div>
              <div>
                <h1 className="text-xl font-semibold text-foreground">Security Scanner</h1>
                <p className="text-sm text-muted-foreground">Vulnerability Detection System</p>
              </div>
            </div>
            <div className="flex items-center gap-2">
              <Clock className="h-4 w-4 text-muted-foreground" />
              <span className="text-sm text-muted-foreground">{new Date(mockScanData.timestamp).toLocaleString()}</span>
            </div>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="container mx-auto px-6 py-8">
        {/* Status Banner */}
        <div className={`mb-8 rounded-lg border ${status.bgColor} border-border p-6`}>
          <div className="flex items-center gap-4">
            <StatusIcon className={`h-8 w-8 ${status.color}`} />
            <div className="flex-1">
              <h2 className={`text-2xl font-semibold ${status.color}`}>{status.label}</h2>
              <p className="text-sm text-muted-foreground mt-1">
                Scan completed on {mockScanData.total_files_scanned} files with {mockScanData.total_vulnerabilities}{" "}
                vulnerabilities detected
              </p>
            </div>
          </div>
        </div>

        {/* Top Stats Grid */}
        <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-4 mb-8">
          <ScanSummary
            title="Security Score"
            value={`${mockScanData.overall_security_score}/100`}
            icon={Shield}
            trend={mockScanData.overall_security_score >= 70 ? "up" : "down"}
          />
          <ScanSummary title="Files Scanned" value={mockScanData.total_files_scanned.toString()} icon={FileCode} />
          <ScanSummary
            title="Total Issues"
            value={mockScanData.total_vulnerabilities.toString()}
            icon={AlertTriangle}
            trend="down"
          />
          <ScanSummary
            title="Critical Issues"
            value={mockScanData.breakdown.critical.toString()}
            icon={XCircle}
            trend={mockScanData.breakdown.critical === 0 ? "up" : "down"}
          />
        </div>

        {/* Main Grid */}
        <div className="grid gap-6 lg:grid-cols-3">
          {/* Left Column - Score and Breakdown */}
          <div className="space-y-6">
            <SecurityScoreCard score={mockScanData.overall_security_score} />
            <VulnerabilityBreakdown breakdown={mockScanData.breakdown} />
          </div>

          {/* Right Column - Vulnerability List */}
          <div className="lg:col-span-2">
            <VulnerabilityList vulnerabilities={mockScanData.vulnerabilities_by_severity} />
          </div>
        </div>

        {/* Files Scanned */}
        <Card className="mt-6">
          <CardHeader>
            <CardTitle>Scanned Files</CardTitle>
            <CardDescription>Files analyzed in this security scan</CardDescription>
          </CardHeader>
          <CardContent>
            <div className="space-y-2">
              {mockScanData.files_scanned.map((file, index) => (
                <div key={index} className="flex items-center gap-3 rounded-lg border border-border bg-muted/30 p-3">
                  <FileCode className="h-4 w-4 text-muted-foreground" />
                  <span className="font-mono text-sm text-foreground">{file}</span>
                </div>
              ))}
            </div>
          </CardContent>
        </Card>
      </main>
    </div>
  )
}
