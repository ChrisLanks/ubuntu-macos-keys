# Enter script code

winClass = window.get_active_class()
# Vscode and konsole for interupts on console
if "konsole" in str(winClass) or "code" in str(winClass):
    keyboard.send_keys("<ctrl>+c")
#else:
    # Do Nothing
          
