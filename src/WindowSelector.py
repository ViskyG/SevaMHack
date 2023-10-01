import pygetwindow as gw

class WindowSelector:

    def get_window_list(self):
        all_windows = gw.getAllTitles()
        all_windows = [title for title in all_windows if title != '']
        return all_windows

    def user_select_window(self):
        window_list = self.get_window_list()
        if not window_list:
            print("No windows found.")
            return None

        print("Выберите окно для снятия скриншота:")
        for i, title in enumerate(window_list):
            print(f"{i + 1}. {title}")

        choice = int(input("Введите номер окна: ")) - 1

        if choice < 0 or choice >= len(window_list):
            print("Неверный выбор.")
            return None

        return window_list[choice]
