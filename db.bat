@echo off


:: IF %1 PARAMETER IS NULL DO THAT
set null=false

if "%1"=="" (
    set null=true
)

if %null%==true (
    echo PretiumDB v1.0.0 Copyright 2023 [arr]
    echo Type "--h" for more information
)

:: ELSE DO THAT



:: END OF CLI

echo.