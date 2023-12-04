@echo off

rem Ativa a env "etl"
call conda activate etl

rem Navega até a pasta do projeto
cd C:\Users\dados\Documents\GitHub\ETL

rem Executa o script dre.py
python dre.py

rem Executa o script comercial.py
python comercial.py