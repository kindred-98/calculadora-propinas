# main_gui.py

# main_gui.py

import tkinter as tk
from src.gui import TipCalculatorGUI
import traceback
import sys


def main():
    try:
        root = tk.Tk()
        app = TipCalculatorGUI(root)
        root.mainloop()
    except Exception as e:
        with open("error_log.txt", "w") as f:
            f.write(traceback.format_exc())
        sys.exit(1)


if __name__ == "__main__":
    main()