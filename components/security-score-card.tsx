import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Progress } from "@/components/ui/progress"
import { Shield } from "lucide-react"

interface SecurityScoreCardProps {
  score: number
}

export function SecurityScoreCard({ score }: SecurityScoreCardProps) {
  const getScoreColor = (score: number) => {
    if (score >= 80) return "text-green-500"
    if (score >= 60) return "text-yellow-500"
    if (score >= 40) return "text-orange-500"
    return "text-red-500"
  }

  const getScoreLabel = (score: number) => {
    if (score >= 80) return "Excellent"
    if (score >= 60) return "Good"
    if (score >= 40) return "Fair"
    return "Poor"
  }

  return (
    <Card>
      <CardHeader>
        <CardTitle className="flex items-center gap-2">
          <Shield className="h-5 w-5" />
          Security Score
        </CardTitle>
        <CardDescription>Overall codebase security rating</CardDescription>
      </CardHeader>
      <CardContent>
        <div className="space-y-4">
          <div className="flex items-baseline gap-2">
            <span className={`text-5xl font-bold ${getScoreColor(score)}`}>{score}</span>
            <span className="text-2xl text-muted-foreground">/100</span>
          </div>
          <Progress value={score} className="h-3" />
          <div className="flex items-center justify-between">
            <span className={`text-sm font-medium ${getScoreColor(score)}`}>{getScoreLabel(score)}</span>
            <span className="text-sm text-muted-foreground">{score >= 70 ? "Above threshold" : "Below threshold"}</span>
          </div>
        </div>
      </CardContent>
    </Card>
  )
}
