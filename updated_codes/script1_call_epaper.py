import subprocess

# Define the arguments to pass
#args = "{\"name\":\"Moises\",\"age\":23}" #"{name: Juan Mecánico, age: 31}"
args = "Se_detecto_10_botellas"

# Construct the command
command = "cd /home/moises/Documents/proyectos/iqupa/e-Paper/RaspberryPi_JetsonNano/c; sudo make clean && sudo make -j4 EPD=epd7in5V2 && sudo ./epd " + f'{args}'

# Run the command
subprocess.run(command, shell=True)