param([switch]$Elevated)

# Tests if the Powershell window is executed in admin mode
function Test-Admin {
    $currentUser = New-Object Security.Principal.WindowsPrincipal $([Security.Principal.WindowsIdentity]::GetCurrent())
    $currentUser.IsInRole([Security.Principal.WindowsBuiltinRole]::Administrator)
}

# Start script in Powershell in admin mode
if ((Test-Admin) -eq $false)  {
    if ($elevated) {
        # tried to elevate, did not work, aborting
    } else {
        Start-Process powershell.exe -Verb RunAs -ArgumentList ('-noprofile -noexit -file "{0}" -elevated' -f ($myinvocation.MyCommand.Definition))
    }
    exit
}
 
# Restart Process using PowerShell 64-bit 
If ($ENV:PROCESSOR_ARCHITEW6432 -eq "AMD64") {
   Try {
       &"$ENV:WINDIR\SysNative\WindowsPowershell\v1.0\PowerShell.exe" -File $PSCOMMANDPATH
   }
 Catch {
     Throw "Failed to start $PSCOMMANDPATH"
 }
    Exit
}
 
# Save the current location and switch to this script's directory 
$prevPwd = $PWD; Set-Location -ErrorAction Stop -LiteralPath $PSScriptRoot

# Setup and Start the Game
try
{
    # Check Python
    $p = &{python -V} 2>&1

    if($p -is [System.Management.Automation.ErrorRecord])
    {
        # Python is not installed or correctly configured
        Write-Host "Python is not installed or correctly configured. Therefore the program could not be started. `n`nPlease visit https://www.python.org/downloads/ to install the latest version of Python and try again.`n"
    }
    else
    {
        $version = $p -replace "Python "
        $pyVersion = [version] $version
        $requiredVersion = '3.9'

        # Is Python version lower than 3.9 ?
        if($pyVersion -lt $requiredVersion)
        {
            # Python version may not be sufficient to run the game
            Write-Host "Python found on your machine but version $pyversion is lower than $requiredVersion.`n`nPlease visit https://www.python.org/downloads/ to install the latest version of Python and try again.`n"
        }
        else
        {
            # Python installed and version is valid
            Write-Host "Python is installed and version $pyversion is valid. Script will continue.`n"

            # Check pip
            $pip = &{pip -V} 2>&1

            if($pip -is [System.Management.Automation.ErrorRecord])
            {
                Write-Host "pip is not correctly configured. Please resolve the issue and try again."
            }
            else
            {
                # Look for main-file
                $mainPyPath = Get-Item $PSScriptRoot\src\main\python\main.py

                if(![System.IO.File]::Exists($mainPyPath))
                {
                    # file with path $path doesn't exist
                    Write-Host "Couldn't find main.py as an entrypoint in the project.`nMake sure this script is running from the correct path (root directory of the project) and try again."
                }
                else
                {
                    # Installing Pybuilder
                    Write-Host "Pybuilder will be installed.`n"
                    pip install pybuilder
                    
                    # Run Pybuilder for required dependencies and Unit tests
                    Write-Host "`nRun Pybuilder to install all remaining dependencies and unit tests.`n"   
                    pyb

                    # Ask before starting
                    Write-Host -Prompt "`nEverything is correctly configured and the game is ready to start."

                    # Run Python script
                    python $mainPyPath
                }
            }
        }    
    }

    Read-Host -Prompt "Press ENTER to exit"

    $PWD  # output the current location 
}
finally {
  # Restore the previous location.
  $prevPwd | Set-Location
}