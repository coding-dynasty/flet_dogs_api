import json

import flet as ft
import requests as rq

image = ft.Image()
status = ft.Text()
error = ''
print(error)

def request():
    global error
    try:
        res = rq.get('https://dog.ceo/api/breeds/image/random')
        _json = json.loads(res.text)
        error = ''
        return {'status': _json["status"], 'message': _json["message"]}
    except Exception as err:
        error = 'Error: ' + str(err).split('(')[2]


data = request()


def main(page: ft.Page):
    global data, status, image

    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def handle_error():
        if error:
            status.value = error
            image.visible = False
            page.update()
        else:
            status.value = data['status']
            image.src = data['message']
            image.width = 400
            image.height = 200
            image.visible = True
            page.update()

    handle_error()

    def refresh(e):
        global data, image, status, error
        data = request()
        handle_error()

    icon = ft.IconButton(ft.icons.REFRESH, on_click=refresh)

    page.add(
        ft.Row(
            [
                status,
                image,
                icon
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )


if __name__ == '__main__':
    ft.app(target=main)
