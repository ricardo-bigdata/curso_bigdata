# Módulo modulo_secundario.py
def exemplo_funcion_Z(param1,param2):
    return param1 + param2

if __name__ == "__main__":
    print('Son un módulo secundario e non vou imprimir nada se se me importa','\n','Pero se se me executa directamente... si que imprimo algo!!!','\n', 'que para iso teño a miña condición if __name__ == "__main__":')
    print(exemplo_funcion_Z(1,2))
