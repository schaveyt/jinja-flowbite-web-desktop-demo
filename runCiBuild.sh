#!/usr/bin/env bash

# Bash script used as the entry point for the TeamCity CI server
# Usage: ./runCiBuild.sh <BUILD_TYPE> (TARGET)
# Example: ./runCiBuild.sh build a0


# set -x
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

APP_MAJOR_VERSION="0"
APP_MINOR_VERSION="1"
APP_PATCH_VERSION="0"
APP_BASE_VERSION="${APP_MAJOR_VERSION}.${APP_MINOR_VERSION}.${APP_PATCH_VERSION}"

BUILD_TYPE="${1}"

function getFullAppVersion()
{
    local git_branch_name_raw=$(git rev-parse --abbrev-ref HEAD)
    local santitized_branch_name=$(echo ${git_branch_name_raw} |  sed "s/[\/_]/-/g")
    echo "${APP_BASE_VERSION}-${santitized_branch_name}"
}


function usage()
{
    echo ""
    echo "Usage: $0 [task] {args}"
    echo ""
    echo "Tasks:"
    echo "   --help              Display this usage message"
    echo ""
    echo "    publish            Builds the distributable executable."
    echo ""
}


if [ -z $BUILD_TYPE ]
then
    echo "ERROR: invalid usage."
    usage
    exit 1
fi


#
# Main Switch Case
#
case $BUILD_TYPE in

    -h|--help)
        usage
        exit 0
        ;;


    publish)

        BUILD_NUMBER="${2}"
        if [ -z $BUILD_NUMBER ]
        then
            echo "ERROR: invalid usage. To publish, one must specify the CICD build number. Type 'local' if building locally"
            echo ""
            exit 1
        fi

        app_full_version=$(getFullAppVersion)
        ALPENGLOW_FULL_VERSION=${app_full_version}-bld-${BUILD_NUMBER}

        echo "Building '${ALPENGLOW_FULL_VERSION}'..."
        echo ""

        echo "Updating file version info..."
        cp -R win_exe_version_info_template.py win_exe_version_info.py
        sed -i "s/{{APP_MAJOR_VERSION}}/$APP_MAJOR_VERSION/g" win_exe_version_info.py
        sed -i "s/{{APP_MINOR_VERSION}}/$APP_MINOR_VERSION/g" win_exe_version_info.py
        sed -i "s/{{APP_PATCH_VERSION}}/$APP_PATCH_VERSION/g" win_exe_version_info.py
        sed -i "s/{{SHORT_VERSION}}/$APP_BASE_VERSION/g" win_exe_version_info.py
        sed -i "s/{{SHORT_VERSION}}/$APP_BASE_VERSION/g" win_exe_version_info.py
        sed -i "s/{{FULL_VERSION}}/$ALPENGLOW_FULL_VERSION/g" win_exe_version_info.py

        mv win_exe_version_info.py my_app/win_exe_version_info.py

        echo "Building executable..."
        pyinstaller desktop.spec

        echo ""
        echo "Successfully executable for version '${ALPENGLOW_FULL_VERSION}'"

        ;;

    *)

    echo "ERROR: Unknown build type $BUILD_TYPE"
    exit 1

esac

echo ""

exit 0
