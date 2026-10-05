"""Simula lanzamientos de dados de distintos tipos desde la terminal."""

import sys
import random
import time
from rich import box  # Estilos de borde para los paneles
from rich import print  # Para interpretar los objetos de Rich
from rich.align import Align  # Para alinear textos
from rich.panel import Panel  # Para los menús empaquetados
from rich.console import Console  # Para limpiar la terminal
from rich.live import Live

# Constantes con el número de caras de cada tipo de dado
D4 = 4
D6 = 6
D8 = 8
D10 = 10
D12 = 12
D20 = 20
VALORES_CAMBIANTES = 15

# Preparación de la consola y comienzo del menú principal
console = Console()

console.clear()
while True:
    # Mostrar el menú principal
    contenido = (
        "[bold cyan]1)[/] Lanzar dados\n"
        "[bold cyan]2)[/] Lanzar dados [yellow]MODO PRO\n"
        "[bold red]S)[/] Salir"
    )
    print(
        Panel(
            contenido,
            title="[bold yellow]MENÚ[/]",
            expand=False,
        ),
    )
    respuesta = input("Selecciona una opción: ")
    if respuesta == "1":
        console.clear()

        # Pedir el tipo de dado y repetir mientras la opción no sea válida
        while True:
            dados = (
                "1) D4       4) D10\n"
                "2) D6       5) D12\n"
                "3) D8       6) D20"
            )
            print(
                Panel(
                    dados,
                    title="TIPO DE DADO",
                    border_style="magenta",
                    subtitle="ELIGE UNO",
                    expand=False,
                ),
            )
            sub_respuesta = input("Tu elección: ").strip()
            if (
                sub_respuesta != "1"
                and sub_respuesta != "2"
                and sub_respuesta != "3"
                and sub_respuesta != "4"
                and sub_respuesta != "5"
                and sub_respuesta != "6"
            ):
                console.clear()
                print(
                    Panel(
                        "[red]Selecciona una opción válida",
                        box=box.ROUNDED,
                        border_style="red",
                        expand=False,
                    ),
                )
            else:
                break

        # Asociar la opción elegida con la constante de caras correspondiente
        if sub_respuesta == "1":
            caras_dado = D4
        elif sub_respuesta == "2":
            caras_dado = D6
        elif sub_respuesta == "3":
            caras_dado = D8
        elif sub_respuesta == "4":
            caras_dado = D10
        elif sub_respuesta == "5":
            caras_dado = D12
        else:
            # Si no es ninguna de las anteriores la opción se corresponderá con la 6
            caras_dado = D20

        # Convertir la entrada de texto a entero y validar que sea positiva
        while True:
            try:
                num_dados = int(
                    input(
                        f"¿Cuántos dados de {caras_dado} lados quieres lanzar?\n"
                        "Introduce un número entero positivo: "
                    )
                )
                if num_dados <= 0:
                    print(
                        Panel(
                            "[red]No se permite cero o valores negativos",
                            box=box.ROUNDED,
                            border_style="red",
                            expand=False,
                        ),
                    )
                    continue
                else:
                    break
            except ValueError:
                print(
                    Panel(
                        "[red]Introduce un número válido",
                        box=box.ROUNDED,
                        border_style="red",
                        expand=False,
                    )
                )
                continue

        # Animar cada dado y acumular el resultado definitivo
        suma_total = 0
        for i in range(1, num_dados + 1):
            with Live(console=console, refresh_per_second=20) as live:
                for j in range(VALORES_CAMBIANTES):
                    valor = random.randint(1, caras_dado)
                    color = "yellow"
                    if j == VALORES_CAMBIANTES - 1:
                        suma_total += valor
                        if valor == 1:
                            color = "red"
                        elif valor == caras_dado:
                            color = "green"

                    live.update(
                        Panel(
                            f"[{color}]{valor:^3d}[/]",
                            box=box.ROUNDED,
                            border_style=color,
                            width=7,
                        ),
                        refresh=True,
                    )
                    time.sleep(0.08)

        # La división devuelve un float aunque ambos operandos sean int, por eso utilizo la expresión de .2f que me deja solo dos decimales
        promedio = suma_total / num_dados
        print(
            Panel(
                f"Total: {suma_total}\nPromedio: {promedio:.2f}",
                box=box.ROUNDED,
                border_style="yellow",
                expand=False,
            ),
        )

        input("Pulsa Enter para continuar...")

    elif respuesta == "2":
        print(
            Panel(
                Align.center("[italic][red]Disponible próximamente"),
                title="Lanzar dado en un renderizado 3D",
                padding=(5, 5),
                box=box.ROUNDED,
                border_style="bold yellow",
                expand=True,
                width=80,

            )
        )
        input("Pulsa Enter para continuar...")
        pass

    elif respuesta == "s" or respuesta == "S":
        console.clear()
        print(
            Panel(
                "[red]Saliendo del programa...",
                box=box.MARKDOWN,
                border_style="red",
                expand=False,
            ),
        )
        sys.exit()
    else:
        console.clear()
        print(
            Panel(
                "[red]Selecciona una opción válida",
                box=box.ROUNDED,
                border_style="red",
                expand=False,
            ),
        )
