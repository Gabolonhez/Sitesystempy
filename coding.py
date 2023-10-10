# iniciate chat buttom
# popup to enter the chat (appears to everyone)
    # the message you entered the chat
    # the field and buttom to send message
# each message you send (appears to everyone)
    # name: text of message

import flet as ft

def main(page):
    
    chat = ft.Column()

    def enviar_mensagem_tunel(infos):
        usuario = infos["usuario"]
        if infos["tipo"] == "entrada":
            chat.controls.append(ft.Text(f"{usuario} Joined the chat", size=12, color=ft.colors.AMBER_400, italic=True))
        else:
            mensagem = infos["mensagem"]
            chat.controls.append(ft.Text(f"{usuario}: {mensagem}"))
        page.update()

    page.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(e):
        page.pubsub.send_all({"usuario": nome_usuario.value, "mensagem": campo_mensagem.value, "tipo": "mensagem"})
        campo_mensagem.value = ""
        page.update()

    campo_mensagem = ft.TextField(label="Type a message")
    botao_enviarmensagem = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    def entrar_chat(e):
        page.add(chat)
        page.add(ft.Row([campo_mensagem, botao_enviarmensagem]))
        popup.open = False
        page.pubsub.send_all({"usuario": nome_usuario.value, "tipo": "entrada"})
        page.remove(botao_iniciar)
        page.update()

    nome_usuario = ft.TextField(label="Write your name")
    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=ft.Text("Welcome to MyZap"),
        content=nome_usuario,
        actions=[ft.ElevatedButton("Join chat", on_click=entrar_chat)])

    def abrir_popup(e):
        page.dialog = popup
        popup.open = True
        page.update()

    botao_iniciar = ft.ElevatedButton("Iniciate chat", on_click=abrir_popup)

    page.add(botao_iniciar,)

ft.app(target=main, view=ft.WEB_BROWSER, port=8000)

