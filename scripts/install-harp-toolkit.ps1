# Downloads the Harp.Toolkit dotnet tool CI artifact and installs it as a local (repo-scoped) tool.
gh api repos/harp-tech/toolkit/actions/artifacts/9699790640/zip > artifact.zip
Expand-Archive artifact.zip -DestinationPath .nuget/local-feed -Force
Remove-Item artifact.zip

if (-not (Test-Path .config/dotnet-tools.json)) { dotnet new tool-manifest -o .config }
dotnet tool install Harp.Toolkit --local --add-source .nuget/local-feed --prerelease
