from cx_Freeze import setup, Executable

base = None    

executables = [Executable("xml plc reader.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "xml plc reader",
    options = options,
    version = "1",
    description = 'reads xml plc',
    executables = executables
)
