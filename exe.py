import subprocess


# Iterable con las rutas de los scripts
scripts_paths = ("/mnt/c/Users/carlo/OneDrive/Escritorio/proyecto/SI_POKEMON_2/run.py", "/mnt/c/Users/carlo/OneDrive/Escritorio/proyecto/SI_POKEMON/run.py")

# Creamos cada proceso    
procesos = [subprocess.Popen(["python3", script]) for script in scripts_paths]

# Esperamos a que todos los subprocesos terminen.
for proceso in procesos:
    proceso.wait()

# Resto de código a ejecutar cuando terminen todos los subprocesos.
