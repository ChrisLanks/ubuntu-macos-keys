# Enter script code

winClass = window.get_active_class()
if "konsole" not in str(winClass):
    keyboard.send_keys("<ctrl>+v")
else:
    keyboard.send_keys("<ctrl>+<shift>+v")