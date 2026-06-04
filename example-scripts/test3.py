from AzuraLang import window, label, button, reporterror, run

# Initialize a standard environment window
window("loggerWin", title="AzuraLang Logging Sandbox", size="300x200")
label("loggerWin", text="Testing Logger Core Elements...")

# 1. Manually test a native framework error simulation directly
print("\n--- Simulated Framework Exception Trace ---")
reporterror(
    code="[12342412x141234312]",
    message="Failed to dynamically register system asset layout.", 
    er_line="42", 
    err_type="RuntimeEngineException"
)

# 2. Trigger an automated error routing trap by calling a non-existent window handle
print("--- Triggering Automated Component Fault Routing ---")
button("loggerWin", text="This will safely fail and log to console")

