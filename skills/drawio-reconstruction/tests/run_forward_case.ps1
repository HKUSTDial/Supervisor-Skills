param(
    [Parameter(Mandatory = $true)]
    [string]$CaseRoot,

    [Parameter(Mandatory = $true)]
    [string]$ReferencePath
)

$ErrorActionPreference = "Stop"

$case = (Resolve-Path -LiteralPath $CaseRoot).Path
$reference = (Resolve-Path -LiteralPath $ReferencePath).Path
$workspace = Join-Path $case "workspace"
$codex = (Get-Command codex -ErrorAction Stop).Source

$env:CODEX_HOME = Join-Path $case "codex-home"
$env:HOME = $case
$env:USERPROFILE = $case
$env:AGENTS_HOME = Join-Path $case ".agents"

$referenceName = [System.IO.Path]::GetFileName($reference)
$prompt = 'Use $drawio-reconstruction to reconstruct ' + $referenceName + ' into an editable Draw.io file and PNG preview in this folder. Preserve the wording and match the reference as closely as possible.'

# Windows PowerShell promotes any native stderr output to ErrorRecord objects.
# Codex emits harmless warnings on stderr, so do not let those warnings abort the
# launcher before Codex can write its own exit code.
$ErrorActionPreference = "Continue"
$prompt | & $codex exec `
    --model gpt-5.5 `
    -c 'model_reasoning_effort="xhigh"' `
    -c 'approval_policy="never"' `
    --enable multi_agent `
    --sandbox danger-full-access `
    --skip-git-repo-check `
    --ephemeral `
    --ignore-user-config `
    --ignore-rules `
    --json `
    -C $workspace `
    -i $reference `
    -o (Join-Path $case "last-message.txt") `
    - 1> (Join-Path $case "events.jsonl") 2> (Join-Path $case "stderr.log")

$code = $LASTEXITCODE
Set-Content -LiteralPath (Join-Path $case "exit-code.txt") -Value $code
exit $code
