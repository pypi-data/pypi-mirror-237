from __future__ import annotations
from typing import Callable
import tkinter as tk
from PIL import Image, ImageTk


def temp_start():
    pass


def temp_update():
    pass


class Color:
    def __init__(self, *args):
        if len(args) == 0:
            self.r = self.g = self.b = 0
            self.a = 1
        elif len(args) == 1:
            self.r = self.g = self.b = args[0]
            self.a = 1
        elif len(args) == 2:
            self.r = self.g = self.b = args[0]
            self.a = args[1]
        elif len(args) == 3:
            self.r, self.g, self.b = args
            self.a = 1
        elif len(args) == 4:
            self.r, self.g, self.b, self.a = args
        else:
            self.r = args[0]
            self.g = args[1]
            self.b = args[2]
            self.a = args[3]

    def hex(self):
        r = min(int(self.r * 255), 255)
        g = min(int(self.g * 255), 255)
        b = min(int(self.b * 255), 255)
        hex_value = "#{:02X}{:02X}{:02X}".format(r, g, b)
        return hex_value

    def hex_alpha(self):
        r = min(int(self.r * 255), 255)
        g = min(int(self.g * 255), 255)
        b = min(int(self.b * 255), 255)
        a = min(int(self.a * 255), 255)
        hex_value = "#{:02X}{:02X}{:02X}{:02X}".format(r, g, b, a)
        return hex_value


class Tinker:
    def __init__(self, start: Callable = None, update: Callable = None) -> None:
        if start is None:
            start = temp_start

        if update is None:
            update = temp_update

        self.root = tk.Tk()
        self.window = TWindow(None)
        self.window.widget = self.root
        self.window.set_title("Tinker")

        screen_width = self.window.screen_width()
        screen_height = self.window.screen_height()

        self.window.x = screen_width / 2 - 200
        self.window.y = screen_height / 2 - 200
        self.window.width = 400
        self.window.height = 400

        self.frame_count = -1
        self.start = start
        self.update = update
        self.initiated = False
        self.started = False

    def run(self):
        self.frame_count += 1

        if self.initiated:
            if not self.started:
                self.start()
                self.started = True

            self.update()

        self.root.after(100, self.run)
        if not self.initiated:
            self.initiated = True
            self.root.mainloop()


# region ELEMENTS

class TElement():
    def __init__(self, parent_element: TElement) -> None:
        self.parent = parent_element
        self._widget: tk.Widget = None

        self._x = 0
        self._y = 0
        self._width = 100
        self._height = 100
        self._padx = 0
        self._pady = 0

        self._text = ""
        self._background: Color
        self._foreground: Color
        self._font_size: int = 16
        self._font_type: str = "Arial"

    # region TRANSFORM

    def get_transform(self):
        return self._x, self._y, self._width, self._height

    def set_transform(self, x: int = None, y: int = None, width: int = None, height: int = None):
        if width is not None:
            width = int(width)
            self.widget.configure(width=width)
            self._width = width

        if height is not None:
            height = int(height)
            self.widget.configure(height=height)
            self._height = height

        if x is not None:
            x = int(x)
            self.widget.place(x=x)
            self._x = x

        if y is not None:
            y = int(y)
            self.widget.place(y=y)
            self._y = y

    @property
    def x(self):
        x, y, width, height = self.get_transform()
        return x

    @x.setter
    def x(self, value):
        self.set_transform(x=value)

    @property
    def y(self):
        x, y, width, height = self.get_transform()
        return y

    @y.setter
    def y(self, value):
        self.set_transform(y=value)

    @property
    def width(self):
        x, y, width, height = self.get_transform()
        return width

    @width.setter
    def width(self, value):
        self.set_transform(width=value)

    @property
    def height(self):
        x, y, width, height = self.get_transform()
        return height

    @height.setter
    def height(self, value):
        self.set_transform(height=value)

    def auto_place(self):
        self.widget.place_forget()
        self.widget.pack()

    @property
    def padx(self):
        return self._padx

    @padx.setter
    def padx(self, value: int):
        self.widget.configure(padx=value)

    @property
    def pady(self):
        return self._pady

    @pady.setter
    def pady(self, value: int):
        self.widget.configure(pady=value)

    @property
    def padding(self):
        return (self.padx, self.pady)

    @padding.setter
    def padding(self, value: tuple(int, int)):
        x, y = value
        self.padx = x
        self.pady = y
    # endregion
    # region SCREEN

    def screen_width(self):
        return self.widget.winfo_screenwidth()

    def screen_height(self):
        return self.widget.winfo_screenheight()

    def screen_name(self):
        return self.widget.winfo_screen()

    # endregion
    # region PROPERTIES
    @property
    def widget(self):
        return self._widget

    @widget.setter
    def widget(self, value: tk.Widget):
        self._widget = value
        self.on_widget()

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value: str):
        self._text = value
        self.widget.configure(text=value)

    @property
    def background(self):
        return self._background

    @background.setter
    def background(self, value: Color):
        self._background = value
        self.widget.configure(bg=value.hex())

    @property
    def foreground(self):
        return self._foreground

    @foreground.setter
    def foreground(self, value: Color):
        self._foreground = value
        self.widget.configure(fg=value.hex())

    @property
    def font_size(self):
        return self._font_size

    @font_size.setter
    def font_size(self, value: int):
        self._font_size = value
        self.widget.configure(font=(self._font_type, value))

    @property
    def font(self):
        return self._font_type

    @font.setter
    def font(self, value: int):
        self._font_type = value
        self.widget.configure(font=(value, self._font_size))
    # endregion
    # region EVENTS

    def on_child(self, child: TElement):
        pass

    def on_parent(self, parent: TElement):
        pass

    def on_widget(self):
        pass
    # endregion

    # region SUBELEMENTS

    def adopt(self, child):
        self.on_child(child)
        child.on_parent(self)
        return child

    def window(self):
        window = TWindow(self)
        self.adopt(window)
        return window

    def label(self, text: str = None):
        label = TLabel(self, text=text)
        self.adopt(label)
        return label

    def button(self, text: str = "Button"):
        button = TButton(self, text=text)
        self.adopt(button)
        return button

    def entry(self):
        entry = TEntry(self)
        self.adopt(entry)
        return entry

    def frame(self):
        frame = TFrame(self)
        self.adopt(frame)
        return frame

    # endregion


class TWindow (TElement):
    def __init__(self, parent_element: TElement) -> None:
        super().__init__(parent_element)
        if parent_element:
            self.widget: tk.Toplevel = tk.Toplevel(parent_element.widget)

        self.is_showing = True

    def on_widget(self):
        self.set_transform(0, 0, 100, 100)
        self.background = Color(0.2)
        self.forground = Color(0.2)

    # region TRANSFORM
    def get_transform(self):
        return self._x, self._y, self._width, self._height

    def set_transform(self, x: int = None, y: int = None, width: int = None, height: int = None):
        if x is not None:
            x = int(x)

        if y is not None:
            y = int(y)

        if width is not None:
            width = int(width)

        if height is not None:
            height = int(height)

        gx = self.x if x is None else x
        gy = self.y if y is None else y
        gwidth = self.width if width is None else width
        gheight = self.height if height is None else height

        self.widget.geometry(f"{gwidth}x{gheight}+{gx}+{gy}")

        if x is not None:
            self._x = x

        if y is not None:
            self._y = y

        if width is not None:
            self._width = width

        if height is not None:
            self._height = height
    # endregion

    def set_title(self, title: str):
        self.widget.title(title)

    def get_title(self):
        return self.widget.title()

    def hide(self):
        self.widget.iconify()
        self.is_showing = False

    def show(self):
        self.widget.deiconify()
        self.is_showing = True

    def toggle_visibility(self):
        if self.is_showing:
            self.hide()
        else:
            self.show()

    def withdraw(self):
        self.widget.withdraw()

    def close(self):
        self.widget.destroy()

    def hide_titlebar(self):
        self.widget.overrideredirect(True)

    def show_titlebar(self):
        self.widget.overrideredirect(False)


class TLabel (TElement):
    def __init__(self, parent_element: TElement, text: str = "Text") -> None:
        super().__init__(parent_element)
        self.widget = tk.Label(parent_element.widget)
        self.text = text
        self.font = "Arial"
        self.font_size = 10
        self.foreground = Color(1)
        self.widget.pack()

    def on_parent(self, parent: TElement):
        self.background = parent.background


class TButton (TElement):
    img = None

    def __init__(self, parent_element: TElement, text: str = "Button") -> None:
        super().__init__(parent_element)
        self.widget = tk.Button(parent_element.widget,
                                compound="center", width=55, height=35)

        if TButton.img is None:
            img = Image.new(mode="RGB", size=(1, 1))
            img = ImageTk.PhotoImage(img)
            TButton.img = img

        self.widget.configure(image=TButton.img)

        self.clicks = []
        self.widget.bind("<Button-1>", self.click)
        self.event: tk.Event = None

        self.text = text
        self.font = "Arial"
        self.font_size = 12
        self.background = Color(0.3)
        self.foreground = Color(1)
        self.widget.pack()

    def click(self, event):
        self.event = event
        for click in self.clicks:
            click()

    def on_click(self, click: Callable):
        self.clicks.append(click)
        return click


class TEntry (TElement):
    def __init__(self, parent_element: TElement) -> None:
        super().__init__(parent_element)
        self.widget = tk.Entry(parent_element.widget)
        self.background = Color(0.15)
        self.foreground = Color(1)
        self.font_size = 12
        self.widget.pack()


class TFrame (TElement):
    def __init__(self, parent_element: TElement, width: int = 100, height: int = 100) -> None:
        super().__init__(parent_element)
        self.widget = tk.Frame(parent_element.widget)
        self.background = Color(0.25)
        self.width = width
        self.height = height
        self.widget.pack()

# endregion
