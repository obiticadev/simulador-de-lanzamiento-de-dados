import sys
from rich import box  # Estilos de borde para los paneles
from rich import print  # Para interpretar los objetos de Rich
from rich.panel import Panel  # Para los menús empaquetados
from rich.console import Console  # Para limpiar la terminal

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
                pass
            elif sub_respuesta == "2":
                pass
            elif sub_respuesta == "3":
                pass
            elif sub_respuesta == "4":
                pass
            elif sub_respuesta == "5":
                pass
            elif sub_respuesta == "6":
                pass
            else:
                raise ValueError("Error inesperado")
        case "s" | "S":
            console.clear()
            print(Panel("[red]Saliendo del programa...",
                        box=box.MARKDOWN, border_style="red", expand=False))
            sys.exit()
        case _:
            console.clear()
            print(Panel("[red]Selecciona una opción válida",
                        box=box.ROUNDED, border_style="red", expand=False))
