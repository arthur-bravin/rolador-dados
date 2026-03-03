import flet as ft
import random as rd

# Função MAIN
def main(page: ft.Page):
    page.title = "Dice Roller - Bravo"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    # Campo de texto que exibirá o resultado da rolagem dos dados
    txt_result = ft.Text(value="0", size=60, text_align=ft.TextAlign.CENTER, width=100, disabled=True)
    # Campo de texto que exibirá o resultado detalhado da rolagem dos dados
    txt_result_detail = ft.Text(value="", size=14, text_align=ft.TextAlign.CENTER, width=500, disabled=True, visible=False)

    # Campo de texto que mostrará a quantidade de dados à ser rolada
    txt_quantity_d4 = ft.TextField(label="D4", text_size=30, value="0", width=60, text_align=ft.TextAlign.CENTER, read_only=True)
    txt_quantity_d6 = ft.TextField(label="D6", text_size=30, value="0", width=60, text_align=ft.TextAlign.CENTER, read_only=True)
    txt_quantity_d8 = ft.TextField(label="D8", text_size=30, value="0", width=60, text_align=ft.TextAlign.CENTER, read_only=True)
    txt_quantity_d10 = ft.TextField(label="D10", text_size=30, value="0", width=60, text_align=ft.TextAlign.CENTER, read_only=True)
    txt_quantity_d12 = ft.TextField(label="D12", text_size=30, value="0", width=60, text_align=ft.TextAlign.CENTER, read_only=True)
    txt_quantity_d20 = ft.TextField(label="D20", text_size=30, value="0", width=60, text_align=ft.TextAlign.CENTER, read_only=True)

    # Campo de texto que mostrará as rolagens realizadas
    txt_log = ft.TextField(label="Registro de Rolagens", multiline=True, min_lines=5, max_lines=5, read_only=True)
    
    # Função para subtrair
    def minus_click(e: ft.TextButton):
        change_values(e, 0)

    # Função para somar
    def plus_click(e: ft.TextButton):
        change_values(e, 1)
    
    def change_values(e: ft.TextButton, button):
        # 0 = Botão sinal de "-"
        # 1 = Botão sinal de "+"
        txt_result.value = str(0)
        txt_result.color = None
        txt_result_detail.visible = False

        if button == 0:  
            match e.control.key:
                case "R4": txt_quantity_d4.value = check_value(str(int(txt_quantity_d4.value) - 1))
                case "R6": txt_quantity_d6.value = check_value(str(int(txt_quantity_d6.value) - 1))
                case "R8": txt_quantity_d8.value = check_value(str(int(txt_quantity_d8.value) - 1))
                case "R10": txt_quantity_d10.value = check_value(str(int(txt_quantity_d10.value) - 1))
                case "R12": txt_quantity_d12.value = check_value(str(int(txt_quantity_d12.value) - 1))
                case "R20": txt_quantity_d20.value = check_value(str(int(txt_quantity_d20.value) - 1))
        else:
            match e.control.key:
                case "A4": txt_quantity_d4.value = check_value(str(int(txt_quantity_d4.value) + 1))
                case "A6": txt_quantity_d6.value = check_value(str(int(txt_quantity_d6.value) + 1))
                case "A8": txt_quantity_d8.value = check_value(str(int(txt_quantity_d8.value) + 1))
                case "A10": txt_quantity_d10.value = check_value(str(int(txt_quantity_d10.value) + 1))
                case "A12": txt_quantity_d12.value = check_value(str(int(txt_quantity_d12.value) + 1))
                case "A20": txt_quantity_d20.value = check_value(str(int(txt_quantity_d20.value) + 1))

        page.update() # Atualiza a interface
    
    def reset_values():
        txt_quantity_d4.value = "0"
        txt_quantity_d6.value = "0"
        txt_quantity_d8.value = "0"
        txt_quantity_d10.value = "0"
        txt_quantity_d12.value = "0"
        txt_quantity_d20.value = "0"

    # Função para verificar o valor da quantidade selecionada
    # Para que não seja possível escolher um valor negativo
    def check_value(value):
        if value and int(value) < 0:
            value = "0"
        return value

    def execute_roll():
        roll_result = 0
        roll_sum = 0
        roll_detail = ""
        roll_count = 0
        final_result = 0
        final_detail = ""

        if int(txt_quantity_d4.value) > 0:
            roll_count = int(txt_quantity_d4.value)
            while roll_count > 0:
                roll_result = rd.randint(1, 4)
                roll_sum = roll_sum + roll_result
                roll_detail = f"{roll_result}" if roll_detail == "" else roll_detail + f" + {roll_result}"
                roll_count = roll_count -1

            final_result = final_result + roll_sum
            final_detail = f"D4({roll_detail})"

        roll_result = 0
        roll_sum = 0
        roll_detail = ""

        if int(txt_quantity_d6.value) > 0:
            roll_count = int(txt_quantity_d6.value)
            while roll_count > 0:
                roll_result = rd.randint(1, 6)
                roll_sum = roll_sum + roll_result
                roll_detail = f"{roll_result}" if roll_detail == "" else roll_detail + f" + {roll_result}"
                roll_count = roll_count -1

            final_result = final_result + roll_sum
            final_detail = final_detail + f"D6({roll_detail})" if final_detail == "" else final_detail + f" + D6({roll_detail})"

        roll_result = 0
        roll_sum = 0
        roll_detail = ""

        if int(txt_quantity_d8.value) > 0:
            roll_count = int(txt_quantity_d8.value)
            while roll_count > 0:
                roll_result = rd.randint(1, 8)
                roll_sum = roll_sum + roll_result
                roll_detail = f"{roll_result}" if roll_detail == "" else roll_detail + f" + {roll_result}"
                roll_count = roll_count -1

            final_result = final_result + roll_sum
            final_detail = final_detail + f"D8({roll_detail})" if final_detail == "" else final_detail + f" + D8({roll_detail})"

        roll_result = 0
        roll_sum = 0
        roll_detail = ""

        if int(txt_quantity_d10.value) > 0:
            roll_count = int(txt_quantity_d10.value)
            while roll_count > 0:
                roll_result = rd.randint(1, 10)
                roll_sum = roll_sum + roll_result
                roll_detail = f"{roll_result}" if roll_detail == "" else roll_detail + f" + {roll_result}"
                roll_count = roll_count -1

            final_result = final_result + roll_sum
            final_detail = final_detail + f"D10({roll_detail})" if final_detail == "" else final_detail + f" + D10({roll_detail})"

        roll_result = 0
        roll_sum = 0
        roll_detail = ""

        if int(txt_quantity_d12.value) > 0:
            roll_count = int(txt_quantity_d12.value)
            while roll_count > 0:
                roll_result = rd.randint(1, 12)
                roll_sum = roll_sum + roll_result
                roll_detail = f"{roll_result}" if roll_detail == "" else roll_detail + f" + {roll_result}"
                roll_count = roll_count -1

            final_result = final_result + roll_sum
            final_detail = final_detail + f"D12({roll_detail})" if final_detail == "" else final_detail + f" + D12({roll_detail})"

        roll_result = 0
        roll_sum = 0
        roll_detail = ""

        if int(txt_quantity_d20.value) > 0:
            roll_count = int(txt_quantity_d20.value)
            while roll_count > 0:
                roll_result = rd.randint(1, 20)
                roll_sum = roll_sum + roll_result
                roll_detail = f"{roll_result}" if roll_detail == "" else roll_detail + f" + {roll_result}"
                roll_count = roll_count -1

            final_result = final_result + roll_sum
            final_detail = final_detail + f"D20({roll_detail})" if final_detail == "" else final_detail + f" + D20({roll_detail})"

        final_detail = f"{final_detail} = {final_result}"
        txt_result.value = final_result
        txt_result_detail.value = final_detail
        txt_result_detail.visible = True

        reset_values()

    # Adiciona os elementos na página
    page.add(
        ft.Row(
            [
                txt_result,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [
                txt_result_detail,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row([],alignment=ft.MainAxisAlignment.CENTER,),
        ft.Row([],alignment=ft.MainAxisAlignment.CENTER,),
        ft.Row([],alignment=ft.MainAxisAlignment.CENTER,),
        ft.Row([],alignment=ft.MainAxisAlignment.CENTER,),
        ft.Row([],alignment=ft.MainAxisAlignment.CENTER,),
        ft.Row([],alignment=ft.MainAxisAlignment.CENTER,),
        ft.Row(
            [
                ft.TextButton(key="R4", content="-", on_click=minus_click),
                txt_quantity_d4,
                ft.TextButton(key="A4", content="+", on_click=plus_click),
                ft.TextButton(key="R6", content="-", on_click=minus_click),
                txt_quantity_d6,
                ft.TextButton(key="A6", content="+", on_click=plus_click),
                ft.TextButton(key="R8", content="-", on_click=minus_click),
                txt_quantity_d8,
                ft.TextButton(key="A8", content="+", on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row([],alignment=ft.MainAxisAlignment.CENTER,),
        ft.Row([],alignment=ft.MainAxisAlignment.CENTER,),
        ft.Row([],alignment=ft.MainAxisAlignment.CENTER,),
        ft.Row(
            [
                ft.TextButton(key="R10", content="-", on_click=minus_click),
                txt_quantity_d10,
                ft.TextButton(key="A10", content="+", on_click=plus_click),
                ft.TextButton(key="R12", content="-", on_click=minus_click),
                txt_quantity_d12,
                ft.TextButton(key="A12", content="+", on_click=plus_click),
                ft.TextButton(key="R20", content="-", on_click=minus_click),
                txt_quantity_d20,
                ft.TextButton(key="A20", content="+", on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row([],alignment=ft.MainAxisAlignment.CENTER,),
        ft.Row([],alignment=ft.MainAxisAlignment.CENTER,),
        ft.Row([],alignment=ft.MainAxisAlignment.CENTER,),
        ft.Row(
            [
                ft.TextButton(content="Rolar", width=150, height=60, style=ft.ButtonStyle(bgcolor=ft.Colors.LIGHT_BLUE, color=ft.Colors.WHITE, padding=ft.Padding.all(20)), on_click=execute_roll),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

# Executa o app
ft.app(target=main)
