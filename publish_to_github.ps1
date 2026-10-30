# publish_to_github.ps1
# Run in PowerShell from D:\testlab\Kurdistan_Flag_Emoji\font
# Prerequisites: git and GitHub CLI (gh) installed; run "gh auth login" once.
$ErrorActionPreference = "Stop"
$repo = "kurdistan-emoji-font"
$desc = "Open-source Kurdistan Region (IQ-KR) flag glyph and OpenType ligature (OFL-1.1). Draft: geometry pending verification."

gh auth status
if (-not (Test-Path ".git")) { git init -b main }
@("*.ttf", "__pycache__/", ".venv/") | Set-Content -Encoding utf8 .gitignore
git add features.fea build_test_font.py verify.py .gitignore
git commit -m "Add IQ-KR tag-sequence ligature test (placeholder geometry)"
gh repo create $repo --public --source . --remote origin --push --description $desc
gh repo view $repo
