#!/usr/bin/python
# -*- coding: utf-8 -*-
# configurado que use o xogo de caracteres latino, con tiles, eñe, €,...
# Módulo de proba test-sys.py

import sys
print('Este é un script de proba das variables e métodos do módulo sys', '\n')

""" Para que dende o propio script se poida obte-la información
hai que lanza-lo script dende consola, por exemplo con:
python ./test-sys.py Ola miña raiña x 365
invocando ó script con varios parámetros de exemplo"""

print('\033[1m','sys.argv','\033[0m','devolve a lista de argumentos que se pasaron por liña de comandos ó script: ')
print(sys.argv,'\n')

print('\033[1m','sys.executable','\033[0m','devolve a ruta absoluta do intérprete python que executou o script invocado por liña de comandos: ')
print(sys.executable,'\n')

print('\033[1m','sys.version','\033[0m','devolve a versión de Python do intérprete que se está a executar: ')
print(sys.version,'\n')

print('\033[1m','sys.platform','\033[0m','devolve a plataforma (sistema operativo) sobre a que se está a executa-lo intérprete de Python: ')
print(sys.platform,'\n')

print('\033[1m','sys.executable','\033[0m','devolve as rutas nas que o intérprete python busca os módulos dos que cargar funcións, variables,... a usar: ')
print(sys.path,'\n')

print('\033[1m','sys.getdefaultencoding()','\033[0m','devolve o sistema de codificación usado por defecto: ')
print(sys.getdefaultencoding(),'\n')

print('\033[1m','exit()','\033[0m','remata a execución do intérprete de comandos: ')
exit()

# Logo dun exit() xa non se executaría o restante código do script,
# polo tanto o seguinte print() non se amosaría por pantalla
print('adeus')

def foo():
   return('foo')

def bar():
   return('bar')
