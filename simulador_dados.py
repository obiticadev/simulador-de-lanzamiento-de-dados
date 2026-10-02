import sys
from rich import print  # Para interpretar los objetos de Rich
from rich.panel import Panel  # Para los menús empaquetados
from rich.console import Console  # Para limpiar la terminal

console = Console()


def revisar_seleccion(respuesta: str):
    pass


def menu():
    contenido = (
        "[bold cyan]1)[/] Lanzar dados\n"
        "[bold red]S)[/] Salir"
    )
    print(Panel(contenido, title="[bold yellow]MENÚ[/]", expand=False))


def tipo_dado():
    dados = (
        "1) D4       4) D10\n"
        "2) D6       5) D12\n"
        "3) D8       6) D20"
    )
    print(Panel(dados, title="TIPO DE DADO",
          border_style="magenta", subtitle="ELIGE UNO", expand=False))
    respuesta = input()


def seleccion_invalida():
    print(Panel("[red]Selecciona una opción válida", box=Box=ROUNDED, border_style="RED"))


while True:
    console.clear()
    menu()
    respuesta = input("Selecciona una opción: ")
    match respuesta:
        case "1":
            while True:
                console.clear()
                tipo_dado()
        case "s" | "S":
            console.clear()
            print("Saliendo del programa...")
            sys.exit()
        case _:
            console.clear()
            seleccion_invalida()
