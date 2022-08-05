import random
import string


class Tarea1:
    def  basic_operations(self, Op1, Op2, Oper):
        # se introducen los parámetros el Operador 1 y 2,
        #así como el parámetro Oper encargado de
        # seleccionar la operación a llevar a cabo
        if Op1 == int:
            Op1 = random.randint(-10, 10)
        elif Op1 == str:
            Op1 = random.choice(string.ascii_letters)
        if isinstance(Op1, int):
            if Op2 == int:
                Op2 = random.randint(-10, 10)
            elif Op2 == str:
                Op1 = random.choice(string.ascii_letters)
            # Verifica que el operador 1 sea un número entero
            if isinstance(Op2, int):
                if Oper == int:
                    Oper = random.randint(-10, 10)
                elif Oper == str:
                    Oper = random.choice(string.ascii_letters)
                # Verifica que el operador 2 sea un número entero
                if isinstance(Oper, int):
                    # Verifica que el parámetro Oper sea un número entero,
                    # Se encarga de seleccionar la operación a llevar a cabo
                    if Oper == 1:  # En caso de que el parámetro Oper sea 1
                        return Op1+Op2  # Se retorna la suma del operador 1 y 2
                    elif Oper == 2:  # En caso de que el parámetro Oper sea 2
                        return Op1-Op2  # Retorna la resta del operador 1 y 2
                    elif Oper == 3:  # En caso de que el parámetro Oper sea 3
                        if Op2 == 0:  # Se verifica que el Operador 2 no sea 0
                            e2 = "ERROR 0x2"
                            return e2
                            # Si es 0 se devuelve un código de error
                        else:
                            if Op2 != 0:  # Si el Operador 2 no es 0
                                return Op1/Op2
                                # Retorna la división del operador 1 y 2
                    else:
                        e2 = "ERROR 0x1"
                        return e2
                        # Si el parámetro Oper es distinto de 1, 2 o 3
                        # Retorna un código de error único
                else:
                    e0 = "ERROR 0x0"
                    return e0
            else:
                e0 = "ERROR 0x0"
                return e0
        else:
            e0 = "ERROR 0x0"
            return e0
            # Si Op1, Op2 o Oper no son un número entero
            # Retorna un código de error único

    def count_char(self, ent):  # se introduce el parámetro de entrada ent
        if isinstance(ent, str):  # Verifica si el parámetro es un string
            return len(ent)  # Si es un string, cuenta la cantidad
            # de caracteres y la retorna
        else:
            e3 = "ERROR 0x3"
            return e3
            # Si no un string, retorna un código de error


Prueba = Tarea1()
Prueba.basic_operations(1,2, 1)
Prueba.count_char("rtrte")
