from src.MSSScreenCapture import MSSScreenCapture
from src.WindowSelector import WindowSelector
import matplotlib.pyplot as plt
import cv2
def main():
    window_selector = WindowSelector()
    selected_window_title = window_selector.user_select_window()

    if selected_window_title is None:
        print("Операция отменена или окно не выбрано.")
        return

    screen_capture = MSSScreenCapture()
    screenshot = screen_capture.capture_window(selected_window_title)

    if screenshot is None:
        print("Скриншот не удалось сделать.")
        return

    # Преобразование цветов
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGRA2RGB)

    # Показать изображение для проверки
    plt.imshow(screenshot)
    plt.show()

if __name__ == "__main__":
    main()
