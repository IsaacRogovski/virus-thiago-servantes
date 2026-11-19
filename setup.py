from cx_Freeze import setup, Executable

# Substitua "script.py" pelo nome do seu arquivo .py principal
setup(
    name="Google",
    version="1.0",
    description="Google",
    executables=[Executable("mudar_papel_de_parede.py")],
)
#a