from abc import ABC, abstractmethod
import numpy as np

class ScreenCaptureInterface(ABC):

    @abstractmethod
    def capture_window(self, window_title: str) -> np.ndarray:
        """
        Захватывает скриншот выбранного окна и возвращает его как NumPy массив.

        Args:
            window_title (str): Заголовок окна, который нужно захватить.

        Returns:
            np.ndarray: Скриншот в формате NumPy массива с каналами RGB.
        """
        pass
