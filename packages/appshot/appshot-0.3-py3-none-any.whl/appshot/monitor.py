import keyboard
from pynput import mouse

class MonitorExit(Exception): ...

class MonitorLogin:
    # If not run the first, it will fail to check once
    keyboard.is_pressed('ctrl')
    # ---------------------
    # Button | Key. State:
    PRESSED = 4294967296
    RELEASED = 2147483648
    # ---------------------
    # Buttons:
    LEFT = 1073741824
    RIGHT = 536870912
    MIDDLE = 268435456
    # ---------------------
    # Keys:
    CTRL = 1073741824
    SHIFT = 536870912
    ALT = 268435456
    ESC = 134217728
    SPACE = 67108864
    ENTER = 33554432
    BACK = 16777216
    DELETE = 8388608
    # UserDefineKeys
    U1 = 4194304
    U2 = 2097152
    U3 = 1048576
    U4 = 524288
    U5 = 262144
    U6 = 131072
    U7 = 65536
    U8 = 32768
    U9 = 16384
    U10 = 8192
    U11 = 4096
    U12 = 2048
    U13 = 1024
    U14 = 512
    U15 = 256
    U16 = 128
    U17 = 64
    U18 = 32
    U19 = 16
    U20 = 8
    U21 = 4
    U22 = 2
    U23 = 1
    # --------------------
    # UserDefine
    U_DEF = {}

    def __init__(self, monitor_button: int, callback=None, ad_key: int = None, ad_callback=None):
        self.monitor_button = monitor_button
        self.callback = callback
        self.ad_key = ad_key
        self.ad_callback = ad_callback

        # transform data
        self.buttons: list = []  # pynput.mouse.Button type
        self.buttons_states: list = []
        self.keys: list = []  # str in keyboard.Key
        self.keys_states: list = []

        self._parse()

    @staticmethod
    def define(Ui: int, to: str):
        MonitorLogin.U_DEF[Ui] = to

    def _parse(self):
        # 根据monitor_button和ad_key, 修改_buttons _buttons_pressed _keys _keys_pressed
        # buttons:
        if self.monitor_button & self.PRESSED:
            self.buttons_states += [True]
        if self.monitor_button & self.RELEASED:
            self.buttons_states += [False]
        if self.monitor_button & self.LEFT:
            self.buttons.append(mouse.Button.left)
        if self.monitor_button & self.RIGHT:
            self.buttons.append(mouse.Button.right)
        if self.monitor_button & self.MIDDLE:
            self.buttons.append(mouse.Button.middle)
        # keys:
        if self.ad_key is None:
            return
        if self.ad_key & self.PRESSED:
            self.keys_states += [True]
        if self.ad_key & self.RELEASED:
            self.keys_states += [False]
        if self.ad_key & self.CTRL:
            self.keys.append("ctrl")
        if self.ad_key & self.ALT:
            self.keys.append("alt")
        if self.ad_key & self.SHIFT:
            self.keys.append("shift")
        if self.ad_key & self.ESC:
            self.keys.append("esc")
        if self.ad_key & self.SPACE:
            self.keys.append("space")
        if self.ad_key & self.ENTER:
            self.keys.append("enter")
        if self.ad_key & self.BACK:
            self.keys.append("backspace")
        if self.ad_key & self.DELETE:
            self.keys.append("delete")
        if self.ad_key & self.U1:
            self.keys.append("u1")
        if self.ad_key & self.U2:
            self.keys.append("u2")
        if self.ad_key & self.U3:
            self.keys.append("u3")
        if self.ad_key & self.U4:
            self.keys.append("u4")
        if self.ad_key & self.U5:
            self.keys.append("u5")
        if self.ad_key & self.U6:
            self.keys.append("u6")
        if self.ad_key & self.U7:
            self.keys.append("u7")
        if self.ad_key & self.U8:
            self.keys.append("u8")
        if self.ad_key & self.U9:
            self.keys.append("u9")
        if self.ad_key & self.U10:
            self.keys.append("u10")
        if self.ad_key & self.U11:
            self.keys.append("u11")
        if self.ad_key & self.U12:
            self.keys.append("u12")
        if self.ad_key & self.U13:
            self.keys.append("u13")
        if self.ad_key & self.U14:
            self.keys.append("u14")
        if self.ad_key & self.U15:
            self.keys.append("u15")
        if self.ad_key & self.U16:
            self.keys.append("u16")
        if self.ad_key & self.U17:
            self.keys.append("u17")
        if self.ad_key & self.U18:
            self.keys.append("u18")
        if self.ad_key & self.U19:
            self.keys.append("u19")
        if self.ad_key & self.U20:
            self.keys.append("u20")
        if self.ad_key & self.U21:
            self.keys.append("u21")
        if self.ad_key & self.U22:
            self.keys.append("u22")
        if self.ad_key & self.U23:
            self.keys.append("u23")

    def buildup(self):
        for i in range(23):
            _ = f"u{i}"
            if _ in self.keys:
                _i = self.keys.index(_)
                self.keys[_i] = self.U_DEF[i]

class MouseMonitorK:
    def __init__(self, *monitor_logins: MonitorLogin):
        # 创建一个鼠标监听器对象
        self.listener = mouse.Listener(on_click=self._on_click, daemon=True)
        # 创建一个字典，用来存储每个鼠标按键对应的监视信息
        self.monitor_dict = {}
        self.monitor_logins = monitor_logins

    def _on_click(self, x, y, button, pressed):
        try:
            self.on_click(x, y, button, pressed)
        except MonitorExit:
            self.listener.stop()


    def on_click(self, x, y, button, pressed):
        # 当鼠标按键被按下或抬起时，执行这个函数
        # 如果这个按键在监视字典中，说明需要进行监视 | 获取这个按键对应的监视信息对象
        monitor_logins = self.monitor_dict.get(button)
        if monitor_logins is not None:
            for monitor_login in monitor_logins:
                # 如果鼠标按键的状态和监视信息对象的状态相同，说明需要执行回调函数
                if pressed in monitor_login.buttons_states:
                    # 如果监视信息对象有回调函数，就执行回调函数
                    if monitor_login.callback is not None:
                        monitor_login.callback(x, y)
                    # 如果监视信息对象有附加的键盘按键检测和附加回调函数
                    if monitor_login.keys and monitor_login.ad_callback is not None:
                        _ = True
                        for key in monitor_login.keys:
                            # 检测附加的键盘按键是否被按下
                            is_pressed = keyboard.is_pressed(key)
                            # print(f"key={key},  pressed={is_pressed}")
                            _ = _ and (is_pressed in monitor_login.keys_states)
                            if not _:
                                break
                        if _:
                            monitor_login.ad_callback(x, y)

    def join(self):
        # 启动鼠标监听器
        for monitor_login in self.monitor_logins:
            monitor_login.buildup()
            # 将鼠标按键作为键，监视信息作为值，添加到字典中
            for btn in monitor_login.buttons:
                _ = self.monitor_dict.get(btn)
                if _ is None:
                    _ = []
                _ += [monitor_login]
                self.monitor_dict[btn] = _
        self.listener.start()
        self.listener.join()


    def stop(self):
        # 停止鼠标监听器
        self.listener.stop()

ML = MonitorLogin