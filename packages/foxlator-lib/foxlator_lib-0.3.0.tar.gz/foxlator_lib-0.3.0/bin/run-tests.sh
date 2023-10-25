#!/bin/bash
# to install any new requirements call with --update-requirements

echo "$ - running unit tests"

venv_path='./test-venv'
install_libs=false

if [ "$1" = '--update-requirements' ]; then 
    install_libs=true 
fi

if ! [ -d $venv_path ]; then
    echo "$ - venv not found, will generate one"
    python3.10 -m venv $venv_path
    install_libs=true
fi

source $venv_path/bin/activate
echo "$ - venv sourced, using: "$(which python3.10) 

if [ "$install_libs" = true ]; then
    echo "$ - installing requirements"
    python3.10 -m pip install -r ./test-requirements.txt

    if ! [ -d ./dist/ ]; then
        echo "$ - ERROR - couldn't find library distribution, you need to build it first"
        exit -1
    fi

    python3.10 -m pip install ./dist/foxlator_lib*.whl --force-reinstall
    echo "$ - done"
fi

test_files=$(ls ./test/*_tests.py 2>/dev/null)
test_file_count=$(echo $test_files | grep -o "\.py" | wc -l)

if [ $test_file_count -eq 0 ]; then
    echo "$ - WARNING - didn't not find any test files, nothing to do here"
else
    echo "$ - found" $test_file_count "test files, will run"
    PYTHONPATH=./test python3.10 -m pytest --verbose $test_files
fi
