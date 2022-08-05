import pytest

from Tarea1Micros import Prueba

# Se importan las funciones del código fuente

# Cada test envía los parámetros de su respectivo decorador a las funciones
# del código fuente, el resultado que arrojan dichas funciones se compara
# con el indicado en el assert.

# Prueba para cada uno de los parámetros de la función basic_operations


@pytest.mark.parametrize(  # Decorador para la parametrización de argumentos
    "Operando_1, Operando_2, OperacionSum, expectedSum",
    [  # Tupla que la función test_suma va a correr en cuatro ocasiones
        (3, 2, 1, 5),  # Elementos de la tupla
        (9, 8, 1, 17),
        (5, 4, 1, 9),
        (-4, 7, 1, 3)])
# Test que prueba la función de suma del código
def test_suma(Operando_1, Operando_2, OperacionSum, expectedSum):
    assert Prueba.basic_operations(
        Operando_1, Operando_2, OperacionSum
        ) == expectedSum
    # Compara el resultado de la función con el de la tupla


@pytest.mark.parametrize(  # Nuevo decorador para testear la función de resta
    "Operando_1, Operando_2, OperacionRest, expectedRest",
    [(3, 8, 2, -5),
     (5, 2, 2, 3),
     (-2, -4, 2, 2),
     (-3, 5, 2, -8)])
# Test para la función de resta del código que se está probando
def test_resta(Operando_1, Operando_2, OperacionRest, expectedRest):
    assert Prueba.basic_operations(
        Operando_1, Operando_2, OperacionRest) == expectedRest


@pytest.mark.parametrize(
    # Nuevo decorador para testear la función de división
    "Operando_1, Operando_2, OperacionDiv, expectedDiv",
    [(4, 8, 3, 0.5),
     (5, 2, 3, 2.5),
     (-2, 1, 3, -2)])
# Test para la función de división del código que se está probando
def test_division(Operando_1, Operando_2, OperacionDiv, expectedDiv):
    assert Prueba.basic_operations(
        Operando_1, Operando_2, OperacionDiv) == expectedDiv


# Decorador con una tupla con los parámetros para probar el-
# retorno correcto del código de error en caso de-
# ingresar un string, para cada operación.
@pytest.mark.parametrize(
    "Operando_1, Operando_2, OperacionSum, expectedSumError",
    [  # El código esperado debe ser "ERROR 0X0"
        (str, int, 1, "ERROR 0x0"),
        (int, str, 1, "ERROR 0x0"),
        (str, int, 2, "ERROR 0x0"),
        (int, str, 2, "ERROR 0x0"),
        (str, int, 3, "ERROR 0x0"),
        (int, str, 3, "ERROR 0x0"),
        (int, int, str, "ERROR 0x0"),
        (str, str, 1, "ERROR 0x0"),
        (str, str, 2, "ERROR 0x0"),
        (str, str, 3, "ERROR 0x0"),
        (str, str, str, "ERROR 0x0"),
    ]
    )  # Función para probar los errores a partir de la tupla anterior.
def test_errorString(Operando_1, Operando_2, OperacionSum, expectedSumError):
    assert Prueba.basic_operations(
        Operando_1, Operando_2, OperacionSum) == "ERROR 0x0"


# Decorador para probar la división entre cero.
@pytest.mark.parametrize(
    "Operando_1, Operando_2, OperacionDiv0, expectedDiv0",
    [
        (int, 0, 3, "ERROR 0x2")
    ]
    )
# Función para prueba de la división entre cero
def test_Div0(Operando_1, Operando_2, OperacionDiv0, expectedDiv0):
    assert Prueba.basic_operations(
        Operando_1, Operando_2, OperacionDiv0) == "ERROR 0x2"


# Tupla para probar el correcto desempeño de la función count_chart
@pytest.mark.parametrize(
    "Palabra, expectedCount",
    [
        ("microprocesadores", 17),
        ("microcontroladores", 18)
    ]
    )
# Test que prueba la función count_chart a partir de la tupla anterior
def test_countChart(Palabra, expectedCount):
    assert Prueba.count_char(Palabra) == expectedCount

# Tupla para probar el retorno del error de la función count_chart


@pytest.mark.parametrize(
    "Palabra, expectedCountError",
    [

        # El código esperado es "ERROR 0x3"
        (int, "ERROR 0x3")
    ]
    )
# Función que prueba el error de la función count_chart
def test_countChartError(Palabra, expectedCountError):
    assert Prueba.count_char(Palabra) == expectedCountError

# Cada función definida en este código compara el resultado esperado-
# con el que arroja el código fuente para distintos eventos, esto
# se realiza con cada assert de la función. Además, cada función de test
# tiene su propia tupla con los parámetros que se le ingresan al código
# fuente.
