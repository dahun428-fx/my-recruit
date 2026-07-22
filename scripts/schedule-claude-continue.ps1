[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [int[]] $Pids,

    [Parameter(Mandatory = $true)]
    [datetime] $At,

    [int] $Port = 27183
)

$now = Get-Date
$delay = ($At - $now).TotalSeconds
if ($delay -lt 0) {
    throw "실행 시간이 이미 지났습니다: $At"
}

Write-Host ("{0}에 PID [{1}]에 입력하도록 예약했습니다." -f $At, ($Pids -join ', '))
Start-Sleep -Seconds ([math]::Ceiling($delay))

$payload = @{ pids = $Pids } | ConvertTo-Json -Compress
try {
    $result = Invoke-RestMethod `
        -Method Post `
        -Uri ("http://127.0.0.1:{0}/continue" -f $Port) `
        -ContentType 'application/json; charset=utf-8' `
        -Body ([Text.Encoding]::UTF8.GetBytes($payload))

    $result.results | Format-Table -AutoSize
} catch {
    throw "VS Code 확장에 연결하지 못했습니다. VS Code가 실행 중이고 확장이 활성화됐는지 확인하세요. 원인: $($_.Exception.Message)"
}
