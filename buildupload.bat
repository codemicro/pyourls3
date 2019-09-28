@echo off
setlocal
:PROMPT
echo This will compile new wheels and source code archives, as well as compile new documentation.
SET /P AREYOUSURE=Are you sure (Y/[N])?
IF /I "%AREYOUSURE%" NEQ "Y" GOTO END

echo.
echo Deleting old wheels
cd dist
del *.*
cd ..
echo.
echo Compiling new wheels
python setup.py sdist bdist_wheel

echo.
SET /P AREYOUSURE=Would you like to upload the new compiled source code? (Y/[N])?
IF /I "%AREYOUSURE%" NEQ "Y" GOTO ENDONE
echo Uploading to PyPI
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
:ENDONE

echo.
echo Compiling docs
mkdocs build

:END
endlocal