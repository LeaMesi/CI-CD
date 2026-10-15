"""Conversor de temperaturas entre Celsius y Fahrenheit."""

import argparse


def convertir_temperatura(valor: float, origen: str, destino: str) -> float:
    """Convierte una temperatura entre Celsius (C) y Fahrenheit (F).

    Raises:
        ValueError: si la escala no es C o F, o la temperatura está
            por debajo del cero absoluto.
    """
    origen = origen.upper()
    destino = destino.upper()

    if origen not in {"C", "F"} or destino not in {"C", "F"}:
        raise ValueError("Las escalas válidas son C y F.")

    celsius = valor if origen == "C" else (valor - 32) * 5 / 9
    if celsius < -273.15:
        raise ValueError("La temperatura no puede ser menor que el cero absoluto.")

    if destino == "C":
        return celsius
    return celsius * 9 / 5 + 32


def main() -> None:
    parser = argparse.ArgumentParser(description="Convierte temperaturas entre C y F.")
    parser.add_argument("valor", type=float, help="Temperatura a convertir")
    parser.add_argument("origen", choices=("C", "F", "c", "f"), help="Escala de origen")
    parser.add_argument("destino", choices=("C", "F", "c", "f"), help="Escala de destino")
    args = parser.parse_args()

    try:
        resultado = convertir_temperatura(args.valor, args.origen, args.destino)
    except ValueError as error:
        parser.error(str(error))

    print(f"{args.valor:g} °{args.origen.upper()} = {resultado:.2f} °{args.destino.upper()}")


if __name__ == "__main__":
    main()
