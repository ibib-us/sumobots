# PowerShell script to write code files to MakerPi. Run after code changes to flash them to the board.

# Source directory path on the C drive. Set your own path here.
$sourceDirectory = "C:\Users\graha\Development\sumobot\sumobots\Builders\Graham_Home\code\*"

# Destination folder. If your MakerPi is mounted under a different drive, enter it here.
$destinationDirectory = "D:\"

# Perform the copy operation for all files and subdirectories in the source directory
try {
    $ErrorActionPreference = "Stop"
    Copy-item -Force -Recurse $sourceDirectory -Destination $destinationDirectory
    Write-Host "All files from $sourceDirectory copied to $destinationDirectory" -ForegroundColor Green
} catch {
    Write-Host "$($_.Exception.Message)" -ForegroundColor Red
}
