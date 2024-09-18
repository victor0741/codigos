from Alumnos import Alumno

def main():
     jesus = Alumno("jesús", "cruz hernández")
     print(jesus)

     jesus.saludar()
     jesus.adios()

     goku = Alumno("Goku", "") #goku es un nuevo objeto de Alumno
     goku.saludar()
     goku.adios()

if __name__ == "__main__":
    main()