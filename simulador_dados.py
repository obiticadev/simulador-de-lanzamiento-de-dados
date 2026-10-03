import sys
from rich import box  # Estilos de borde para los paneles
from rich import print  # Para interpretar los objetos de Rich
from rich.panel import Panel  # Para los menús empaquetados
from rich.console import Console  # Para limpiar la terminal

D4 = 4
D6 = 6
D8 = 8
D10 = 10
D12 = 12
D20 = 20

console = Console()


console.clear()
while True:
    contenido = (
        "[bold cyan]1)[/] Lanzar dados\n"
        "[bold red]S)[/] Salir"
    )
    print(Panel(contenido, title="[bold yellow]MENÚ[/]", expand=False))
    respuesta = input("Selecciona una opción: ")
    match respuesta:
        case "1":
            console.clear()
            while True:
                dados = (
                    "1) D4       4) D10\n"
                    "2) D6       5) D12\n"
                    "3) D8       6) D20"
                )
                print(Panel(dados, title="TIPO DE DADO",
                            border_style="magenta", subtitle=f"ELIGE UNO", expand=False))
                sub_respuesta = input("Tu elección: ").strip()
                if (sub_respuesta != "1" and sub_respuesta != "2" and sub_respuesta != "3" and sub_respuesta != "4" and sub_respuesta != "5" and sub_respuesta != "6"):
                    console.clear()
                    print(Panel("[red]Selecciona una opción válida",
                                box=box.ROUNDED, border_style="red", expand=False))
                else:
                    break

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
            elif sub_respuesta == "6":
                caras_dado = D20
            while True:
                try:
                    num_dados = int(input(
                        f"¿Cuántos dados de {caras_dado} lados quieres lanzar?\nIntroduce un número entero positivo: "))
                    if num_dados <= 0:
                        print(Panel("[red]No se permite cero o valores negativos",
                                    box=box.ROUNDED, border_style="red", expand=False))
                    else:
                        break
                except ValueError:
                    print(Panel("[red]Introduce un número válido",
                          box=box.ROUNDED, border_style="red", expand=False))
        case "s" | "S":
            console.clear()
            print(Panel("[red]Saliendo del programa...",
                        box=box.MARKDOWN, border_style="red", expand=False))
            sys.exit()
        case _:
            console.clear()
            print(Panel("[red]Selecciona una opción válida",
                        box=box.ROUNDED, border_style="red", expand=False))
