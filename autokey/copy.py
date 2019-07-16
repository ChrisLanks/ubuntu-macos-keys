# Enter script code

#winTitle = window.get_active_title()
winClass = window.get_active_class()
#dialog.info_dialog("Window information", "Active window information:\\nTitle: '%s'\\nClass: '%s'" % (winTitle, winClass))
if "konsole" not in str(winClass):
    keyboard.send_keys("<ctrl>+c")
else:
    keyboard.send_keys("<ctrl>+<shift>+c")

          
