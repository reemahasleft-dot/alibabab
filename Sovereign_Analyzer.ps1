param($FilePath)
$Content = Get-Content $FilePath -Raw
$Body = @{
    model = "llama3"
    prompt = "Analyze the following code/text for security vulnerabilities, tracking scripts, or malicious intent. Provide a risk score from 1-10: 

 $Content"
    stream = $false
} | ConvertTo-Json
Invoke-RestMethod -Uri "http://localhost:11434/api/generate" -Method Post -Body $Body -ContentType "application/json"
