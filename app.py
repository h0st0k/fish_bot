import flet as ft
import subprocess
import os

def main(page: ft.Page):
    page.title = "Пульт управления Ботом"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    status_text = ft.Text("Статус комплекса: Готов к запуску", size=20, color="lightblue")

    def start_bot_click(e):
        status_text.value = "Статус: Команда отправлена на ПК!"
        page.update()
        # Запускаем через абсолютный путь с явным вызовом bash
        script_path = os.path.expanduser("~/Desktop/Запустить_Бота.sh")
        subprocess.Popen(f"bash {script_path}", shell=True)
        time_status()

    def stop_bot_click(e):
        status_text.value = "Статус: Комплекс ПРИНУДИТЕЛЬНО ОСТАНОВЛЕН!"
        page.update()
        subprocess.run("pkill -f bot.py", shell=True)
        subprocess.run("pkill -f chrome", shell=True)

    def time_status():
        status_text.value = "Статус: Бот успешно работает в фоне..."
        page.update()

    btn_start = ft.ElevatedButton("ЗАПУСТИТЬ ВСЮ ФЕРМУ", on_click=start_bot_click, bgcolor="green", color="white", width=250, height=50)
    btn_stop = ft.ElevatedButton("ОСТАНОВИТЬ ВСЁ", on_click=stop_bot_click, bgcolor="red", color="white", width=250, height=50)

    page.add(
        ft.Text("🤖", size=40),
        status_text,
        ft.Container(height=20),
        btn_start,
        ft.Container(height=10),
        btn_stop
    )

ft.app(target=main, view=ft.AppView.WEB_BROWSER)
