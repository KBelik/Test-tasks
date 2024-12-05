import os
import time
import pyautogui

# Открываем калькулятор в зависимости от операционной системы
def open_calculator():
    if os.name == 'nt':  # Windows
        os.system('start calc')
    elif os.name == 'posix':  # macOS или Linux
        os.system('open -a Calculator')  # Для macOS
        # Для Linux может понадобиться другое имя приложения, например:
        # os.system('gnome-calculator')
    time.sleep(2)  # Ждем, пока калькулятор откроется

# Функция для нажатия кнопок калькулятора
def press_buttons():
    path_key = 'calc_key/'
    # Определяем изображения кнопок (необходимо заранее сделать скриншоты кнопок)
    buttons = {
        '1': 'calc1key.png',
        '2': 'calc2key.png',
        '+': 'calcpluskey.png',
        '7': 'calc7key.png',
        '=': 'calcequalskey.png'
    }

    for button in ['1', '2', '+', '7', '=']:
        button_location = pyautogui.locateCenterOnScreen(path_key+buttons[button], confidence=0.9)
        if button_location is not None:
            pyautogui.click(button_location)  # Нажимаем на кнопку
            time.sleep(0.5)  # Небольшая задержка между нажатиями
        else:
            print(f"Кнопка {button} не найдена на экране.")

# Основная функция
def main():
    open_calculator()
    press_buttons()

if __name__ == "__main__":
    main()
