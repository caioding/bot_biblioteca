$exclude = @("venv", "bot_biblio.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot_biblio.zip" -Force