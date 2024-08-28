#!/usr/bin/env pwsh

# PowerShell script used as the entry point for the TeamCity CI server
# Usage: ./build.ps1 <BUILD_TYPE> (TARGET)
# Example: ./build.ps1 build a0


$APP_MAJOR_VERSION = "0"
$APP_MINOR_VERSION = "4"
$APP_PATCH_VERSION = "0"
$APP_BASE_VERSION = "$APP_MAJOR_VERSION.$APP_MINOR_VERSION.$APP_PATCH_VERSION"

function Main {

    param (
        [string]$BUILD_TYPE,
        [string]$BUILD_NUMBER
    )

    function Get-FullAppVersion {
        $git_branch_name_raw = git rev-parse --abbrev-ref HEAD
        $santitized_branch_name = $git_branch_name_raw -replace '[\\/_]', '-'
        return "$APP_BASE_VERSION-$santitized_branch_name"
    }

    function Show-Usage {
        Write-Host ""
        Write-Host "Usage: $($MyInvocation.MyCommand.Name) [task] {args}"
        Write-Host ""
        Write-Host "Tasks:"
        Write-Host "   --help              Display this usage message"
        Write-Host ""
        Write-Host "    publish            Builds the distributable executable."
        Write-Host ""
    }

    if (-not $BUILD_TYPE) {
        Write-Host "ERROR: invalid usage."
        Show-Usage
        exit 1
    }

    switch ($BUILD_TYPE) {
        "-h" { Show-Usage; exit 0 }
        "--help" { Show-Usage; exit 0 }

        "publish" {
            if (-not $BUILD_NUMBER) {
                Write-Host "ERROR: invalid usage. To publish, one must specify the CICD build number. Type 'local' if building locally"
                Write-Host ""
                exit 1
            }

            $app_full_version = Get-FullAppVersion
            $ALPENGLOW_FULL_VERSION = "$app_full_version-bld-$BUILD_NUMBER"

            Write-Host "Building '$ALPENGLOW_FULL_VERSION'..."
            Write-Host ""

            Write-Host "Updating file version info..."
            Copy-Item win_exe_version_info_template.py win_exe_version_info.py
            (Get-Content win_exe_version_info.py) -replace '{{APP_MAJOR_VERSION}}', $APP_MAJOR_VERSION |
                Set-Content win_exe_version_info.py
            (Get-Content win_exe_version_info.py) -replace '{{APP_MINOR_VERSION}}', $APP_MINOR_VERSION |
                Set-Content win_exe_version_info.py
            (Get-Content win_exe_version_info.py) -replace '{{APP_PATCH_VERSION}}', $APP_PATCH_VERSION |
                Set-Content win_exe_version_info.py
            (Get-Content win_exe_version_info.py) -replace '{{SHORT_VERSION}}', $APP_BASE_VERSION |
                Set-Content win_exe_version_info.py
            (Get-Content win_exe_version_info.py) -replace '{{FULL_VERSION}}', $ALPENGLOW_FULL_VERSION |
                Set-Content win_exe_version_info.py

            Move-Item win_exe_version_info.py my_app/win_exe_version_info.py -Force

            Write-Host "Building executable..."
            pyinstaller desktop.spec

            Write-Host ""
            Write-Host "Successfully built executable for version '$ALPENGLOW_FULL_VERSION'"
        }

        default {
            Write-Host "ERROR: Unknown build type $BUILD_TYPE"
            exit 1
        }
    }

    Write-Host ""
    exit 0
}

Main -BUILD_TYPE $args[0] -BUILD_NUMBER $args[1]

