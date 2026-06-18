# 1. Değişken Tanımlama (Variables)
$ProjectDir = "."
$LogFile = "$ProjectDir\logs\pipeline.log"
$Timestamp = (Get-Date).ToString("yyyy-MM-dd HH:mm:ss")

"[$Timestamp] Starting data pipeline automation..." >> $LogFile

# 2. Klasör Kontrolü (If/Else)
if (Test-Path "$ProjectDir\raw") {
    "[$Timestamp] SUCCESS: Raw data directory exists." >> $LogFile
    # İleride buraya Python scriptini tetikleyecek kodu yazacağız:
    # python main.py
    "[$Timestamp] Data processing finished successfully." >> $LogFile
} else {
    "[$Timestamp] FAILED: Raw data directory missing! Creating it now..." >> $LogFile
    New-Item -ItemType Directory -Path "$ProjectDir\raw" -Force
}