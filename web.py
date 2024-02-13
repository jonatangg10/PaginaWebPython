# pip install flask
# flask es Flask es un framework minimalista escrito en Python que permite crear aplicaciones web rápidamente y 
# con un mínimo número de líneas de código. Está basado en la especificación WSGI de Werkzeug y el motor de templates Jinja2 y tiene una licencia BSD

from flask import Flask,render_template, request

app = Flask("my-first-website-in-python")

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/educacion")
def educacion():
    return render_template("educacion.html")

@app.route("/lenguajes")
def lenguajes():
    # Mislenguajes = ("github", "Comandos linux", "Python", "Jenkins")
    Mislenguajes = {
        "git" : {
            "descripcion" : "Es un sistema de control de versiones distribuido que te permite registrar los cambios que haces en tus archivos.",
            "popularidad" : "Alto",
            "link" : "https://seti.udemy.com/course/git-github/",
            "lanzamiento" : 2005     
        },
        "github" : {
            "descripcion" : "GitHub es una compañía sin fines de lucro que ofrece un servicio de hosting de repositorios almacenados en la nube.",
            "popularidad" : "Alto",
            "link" : "https://seti.udemy.com/course/git-github/",
            "lanzamiento" : 2008     
        },
        "Comandos Linux" : {
            "descripcion" : "Un comando Linux es un programa o utilidad que se ejecuta en la CLI, una consola que interactúa con el sistema.",
            "popularidad" : "Alto",
            "link" : "https://kinsta.com/es/blog/linux-comandos/",
            "lanzamiento" : 1991
        },
        "Python" : {
            "descripcion" : "Es un lenguaje de programación ampliamente utilizado en las aplicaciones web, el desarrollo de software, la ciencia de datos y el machine learning.",
            "popularidad" : "Alto",
            "link" : "https://seti.udemy.com/course/ultimate-python-de-cero-a-programador-experto/",
            "lanzamiento" : 1991
        },
        "Jenkins" : {
            "descripcion" : "Jenkins es un servidor open source para la integración continua. Es una herramienta que se utiliza para compilar y probar proyectos de software de forma continua.",
            "popularidad" : "Alto",
            "link" : "https://seti.udemy.com/course/la-guia-de-jenkins-de-cero-a-experto/",
            "lanzamiento" : 1995
        },
    }
    return render_template("lenguajes.html", mlenguajes=Mislenguajes)

@app.route("/comandos")
def comandos():
    #comandosLinux = ("PHP", "JavaScript", "Python", "React.js")

    comandosLinux = {
        "ssh" : {
            "descripcion" : "El comando ssh ofrece comunicación encriptada y segura entre dos sistemas sobre una red no segura. Este comando reemplaza al telnet, rlogin, rsh. La primera vez que realizas la conexión debes aceptar la firma del otro host.",
            "link" : "https://kinsta.com/es/blog/comandos-de-ssh/"     
        },
        "history" : {
            "descripcion" : "El comando history permite conocer los últimos comandos que se han ejecutado en un servidor.Por defecto, siempre se muestran los últimos 500 comandos que se han lanzado, a partir de los datos que se encuentran en el archivo.",
            "link" : "https://geekland.eu/como-usar-y-configurar-el-historial-de-comandos-history-en-linux/"     
        },
        "ls" : {
            "descripcion" : "El comando te permite mostrar todo el contenido de una carpeta o directorio en la línea de comandos.",
            "link" : "https://www.ionos.es/digitalguide/servidores/configuracion/comando-ls-de-linux/#:~:text=%C2%B6,por%20defecto%20en%20orden%20alfab%C3%A9tico."     
        },
        "ls -l" : {
            "descripcion" : "ls -l. La opción -l nos permite listar los ficheros en formato de una sola columna, listando un fichero por cada línea con la siguiente información: permisos del fichero, el número de enlace, nombre del propietario, nombre del grupo al que pertenece, tamaño en bytes, una marca de tiempo y nombre del fichero.",
            "link" : "https://docs.oracle.com/cd/E19620-01/805-7644/x-5lbaf/index.html"     
        },
        "cd" : {
            "descripcion" : "El comando cd (change directory) permite moverse entre directorios del sistema. Puedes cambiar de directorio especificando la ruta absoluta desde el directorio raíz o relativa desde tu ubicación actual.",
            "link" : "https://www.ionos.es/digitalguide/servidores/configuracion/comando-cd-de-linux/"     
        },
        "cd .." : {
            "descripcion" : "El comando cd (change directory) permite moverse entre directorios del sistema. Puedes cambiar de directorio especificando la ruta absoluta desde el directorio raíz o relativa desde tu ubicación actual.",
            "link" : "https://www.ionos.es/digitalguide/servidores/configuracion/comando-cd-de-linux/"     
        },
        "cd -" : {
            "descripcion" : "El comando cd (change directory) permite moverse entre directorios del sistema. Puedes cambiar de directorio especificando la ruta absoluta desde el directorio raíz o relativa desde tu ubicación actual.",
            "link" : "https://www.ionos.es/digitalguide/servidores/configuracion/comando-cd-de-linux/"     
        },
        "pwd" : {
            "descripcion" : "El comando pwd viene de 'print working directory', (mostrar el directorio actual). Cuando usted escribe pwd, le está preguntando a su sistema Linux que le muestre su ubicación actual. Su sistema le responde imprimiendo la ruta completa del directorio actual en el intérprete de comandos, en el monitor.",
            "link" : "https://www.ionos.es/digitalguide/servidores/configuracion/comando-cd-de-linux/"     
        },
        "mkdir" : {
            "descripcion" : "El comando de Linux conocido como mkdir te permite crear una o más carpetas en tu directorio de trabajo actual. El comando también te permite crear jerarquías de carpetas complejas.",
            "link" : "https://www.ionos.es/digitalguide/servidores/configuracion/comando-mkdir-de-linux/#:~:text=El%20comando%20de%20Linux%20conocido,crear%20jerarqu%C3%ADas%20de%20carpetas%20complejas."     
        },
        "rmdir" : {
            "descripcion" : "El comando rmdir. Para eliminar un directorio en Linux permanentemente, usa los comandos rmdir o rm. Usa el comando rmdir o rm -d para eliminar directorios vacíos.",
            "link" : "https://www.hostinger.co/tutoriales/borrar-archivos-carpetas-linux#:~:text=directorios%20en%20Linux%3F-,El%20comando%20rmdir,d%20para%20eliminar%20directorios%20vac%C3%ADos."     
        },
        "rm" : {
            "descripcion" : "El mandato rm elimina las entradas para un archivo, grupo de archivos o archivos seleccionados determinados que se han especificado de una lista de un directorio.",
            "link" : "https://www.ionos.es/digitalguide/servidores/configuracion/comando-rm-de-linux/"     
        },
    }
    return render_template("comandos.html", comandos=comandosLinux)

@app.route("/signup", methods=["POST"])
def signup():
    if request.method == "POST":
        nombre = request.form['NombreFormulario']
        numero = request.form['numero']
        correo = request.form['correo']
        return f"{nombre} - {numero} - {correo}"
    else:
        return "bad"

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")

@app.route("/<name>")
def variables(name):
    return render_template("name.html",contenido=name,lorem = "Test texto")

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port='5000')
    #debug true hace que cuando haya un cambio no se tenga que volver a correr el servidor
