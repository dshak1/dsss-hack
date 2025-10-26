import { Card, CardContent } from "@/components/ui/card"
import { type LucideIcon, TrendingUp, TrendingDown } from "lucide-react"

interface ScanSummaryProps {
  title: string
  value: string
  icon: LucideIcon
  trend?: "up" | "down"
}

export function ScanSummary({ title, value, icon: Icon, trend }: ScanSummaryProps) {
  return (
    <Card>
      <CardContent className="p-6">
        <div className="flex items-center justify-between">
          <div className="space-y-1">
            <p className="text-sm text-muted-foreground">{title}</p>
            <p className="text-3xl font-bold text-foreground">{value}</p>
          </div>
          <div className="flex flex-col items-end gap-2">
            <div className="rounded-lg bg-primary/10 p-3">
              <Icon className="h-6 w-6 text-primary" />
            </div>
            {trend && (
              <div className={`flex items-center gap-1 ${trend === "up" ? "text-green-500" : "text-red-500"}`}>
                {trend === "up" ? <TrendingUp className="h-3 w-3" /> : <TrendingDown className="h-3 w-3" />}
              </div>
            )}
          </div>
        </div>
      </CardContent>
    </Card>
  )
}
