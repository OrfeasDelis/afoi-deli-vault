# run-audit.ps1 — headless, read-only vault audit capture
#
# Runs the /vault-audit skill in PLAN mode (Claude can read everything but
# CANNOT write any file), and captures the report it prints to stdout into a
# dated file under _meta/audits/. Because Claude has zero write access in plan
# mode, the *only* thing that touches disk is this script's redirect — the
# strongest possible proposes-only guarantee for an unattended run.
#
# Usage (on-demand):   & "C:\Users\user\Desktop\afoi-deli-vault\_meta\audits\run-audit.ps1"
# Scheduling:          see the schtasks command in the install summary / STATE.md.

$ErrorActionPreference = 'Stop'

$Vault = 'C:\Users\user\Desktop\afoi-deli-vault'
$Date  = Get-Date -Format 'yyyy-MM-dd'
$Out   = Join-Path $Vault "_meta\audits\$Date-vault-audit.md"

Set-Location $Vault

# --permission-mode plan  -> read-only; Claude writes nothing.
# settings.json already pins the model to claude-opus-4-8; -p runs headless.
& claude -p "/vault-audit" --permission-mode plan | Out-File -FilePath $Out -Encoding utf8

Write-Output "Vault audit report written to: $Out"
