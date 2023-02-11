# Check Python
$p = &{python -V} 2>&1

if($p -is [System.Management.Automation.ErrorRecord])
{
    # Python is not installed or correctly configured
    
    Write-Host "Python is not installed or correctly configured. Therefore the program could not be started. `n`n
    Please visit https://www.python.org/downloads/ to install the latest version of Python and try again.`n"
}
else
{
    $version = $p -replace "Python "
    $pyVersion = [version] $version

    # Is Pyversion lower than 3.10 ?
    if($pyVersion -lt '3.10')
    {
        # Python version may not be sufficient to run the game
        Write-Host "Python found on your machine but version $pyversion is lower than 3.10.`nPlease visit https://www.python.org/downloads/ to install the latest version of Python and try again.`n"
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
            $mainPyPath = Get-Item src\main\python\main.py | Resolve-Path -Relative

            if(![System.IO.File]::Exists($mainPyPath))
            {
                # file with path $path doesn't exist
                Write-Host "Couldn't find main.py as an entrypoint in the project.`nMake sure this script is running from the correct path (In the root directory of the project) and try again."
            }
            else
            {
                # Installing Pybuilder
                Write-Host "Pybuilder will be installed.`n"
                pip install pybuilder


                # Installing Pybuilder
                Write-Host "`nRun Pybuilder to install all remaining dependencies and unit tests.`n"

                # Run Pybuilder for required dependencies and Unit tests
                pyb

                # Ask before starting
                Read-Host -Prompt "`nEverything is correctly configured and the game is ready to start.`nPress ENTER to start the game"

                # Run Python script
                python $mainPyPath
            }
        }
    }    
}

Read-Host -Prompt "`nPress ENTER to exit"