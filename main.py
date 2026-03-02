import flet as ft
import random as rd

# Função MAIN
def main(page: ft.Page):
    page.title = "Dice Roller - Bravo"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    # Campo de texto que exibirá o resultado da rolagem dos dados
    txt_result = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    # Campo de texto que mostrará a quantidade de dados à ser rolada
    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    # Campo de texto que mostrará as rolagens realizadas
    txt_log = ft.TextField(label="Registro de Rolagens", multiline=True, min_lines=5, max_lines=5, read_only=True)
    
    # Função para subtrair
    def minus_click(e):
        reset_values(0)

    # Função para somar
    def plus_click(e):
        reset_values(1)

    # Função de rolagem dos dados
    def dice_click(e):
        if int(txt_number.value) < 1:
            pass
        else:            
            dice_sides = switch_case_dice(e.control.content)
            dice_quantity = int(txt_number.value)
            roll_count = dice_quantity
            dice_result = 0
            txt_results = ""

            while roll_count > 0:
                roll = rd.randint(1, dice_sides)
                dice_result = dice_result + roll
                roll_count = roll_count - 1               
                txt_results = f"{roll}" if txt_results == "" else txt_results + f" + {roll}"

            if dice_result > 0:
                if dice_result == 1:
                    txt_result.color = ft.Colors.RED
                elif dice_result == dice_sides:
                    txt_result.color =ft.Colors.GREEN

                txt_result.value = str(dice_result)
                
            if txt_log.value == "":
                txt_log.value = f"{dice_quantity}{e.control.content} = {str(dice_result)}" if dice_quantity == 1 else f"{dice_quantity}{e.control.content} = ({txt_results}) {str(dice_result)}"
            else:
                txt_log.value = f"{dice_quantity}{e.control.content} = {str(dice_result)}" + f"\n{txt_log.value}" if dice_quantity == 1 else f"{dice_quantity}{e.control.content} = ({txt_results}) {str(dice_result)}" + f"\n{txt_log.value}"

            txt_number.value = "0"
            page.update()
        
    # FUnção para determinar o número de lados de acordo com o dado rolado
    def switch_case_dice(dice_name):
        match dice_name:
            case "d4": return 4
            case "d6": return 6
            case "d8": return 8
            case "d10": return 10
            case "d12": return 12
            case "d20": return 20
            case "d100": return 100
    
    # Função para verificar o valor da quantidade selecionada
    # Para que não seja possível escolher um valor negativo
    def check_value(value):
        if value and int(value) < 0:
            value = "0"
        return value
    
    def reset_values(button):
        # 0 = Botão sinal de "-"
        # 1 = Botão sinal de "+"
        if button == 0:            
            txt_result.value = str(0)
            txt_result.color = None
            txt_number.value = check_value(str(int(txt_number.value) - 1))
            page.update() # Atualiza a interface
        else:
            txt_result.value = str(0)
            txt_result.color = None
            txt_number.value = check_value(str(int(txt_number.value) + 1))
            page.update()
    
    # Limpa o log de rolagens
    def clear_rolls_log():
        txt_result.value = str(0)
        txt_number.value = str(0)
        txt_log.value = ""
        page.update()


    # Adiciona os elementos na página
    page.add(
        ft.Row(
            [
                txt_result
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [
                ft.IconButton(ft.Icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.Icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [
                ft.TextButton(content="d4", style=ft.ButtonStyle(color=ft.Colors.WHITE, bgcolor=ft.Colors.LIGHT_BLUE), on_click=dice_click),
                ft.TextButton(content="d6", style=ft.ButtonStyle(color=ft.Colors.WHITE, bgcolor=ft.Colors.LIGHT_BLUE), on_click=dice_click),
                ft.TextButton(content="d8", style=ft.ButtonStyle(color=ft.Colors.WHITE, bgcolor=ft.Colors.LIGHT_BLUE), on_click=dice_click),
                ft.TextButton(content="d10", style=ft.ButtonStyle(color=ft.Colors.WHITE, bgcolor=ft.Colors.LIGHT_BLUE), on_click=dice_click),
                ft.TextButton(content="d12", style=ft.ButtonStyle(color=ft.Colors.WHITE, bgcolor=ft.Colors.LIGHT_BLUE), on_click=dice_click),
                ft.TextButton(content="d20", style=ft.ButtonStyle(color=ft.Colors.WHITE, bgcolor=ft.Colors.LIGHT_BLUE), on_click=dice_click),
                ft.TextButton(content="d100", style=ft.ButtonStyle(color=ft.Colors.WHITE, bgcolor=ft.Colors.LIGHT_BLUE), on_click=dice_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [
                txt_log,
                ft.TextButton(content="Limpar Rolagens", on_click=clear_rolls_log),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

# Executa o app
ft.app(target=main)
