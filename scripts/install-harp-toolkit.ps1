# Downloads the Harp.Toolkit dotnet tool CI artifact and installs it as a local (repo-scoped) tool.
# Uses Invoke-WebRequest -OutFile instead of `gh api ... > file` because PowerShell's
# `>` redirection re-encodes stdout as text, corrupting the binary zip content.
$token = gh auth token
Invoke-WebRequest -Uri "https://api.github.com/repos/harp-tech/toolkit/actions/artifacts/9836533617/zip" `
    -Headers @{ Authorization = "Bearer $token"; Accept = "application/vnd.github+json" } `
    -OutFile artifact.zip
Expand-Archive artifact.zip -DestinationPath .nuget/local-feed -Force
Remove-Item artifact.zip

if (-not (Test-Path .config/dotnet-tools.json)) { dotnet new tool-manifest -o .config }
dotnet tool install Harp.Toolkit --local --add-source .nuget/local-feed --prerelease