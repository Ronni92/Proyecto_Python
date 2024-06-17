from flask import Flask, render_template #importacion de la biblioteca

app= Flask(__name__)#es una  parametro para indicarle la carpeta donde almacenar
 
@app.route('/')# permitir que los usuarios naveguen 
def index():#muestra el contenido / para navegar se debe cambiar el nombre
    return render_template('index.html')

if __name__=="__main__": #funcion principal para arrancar el codigo
    app.run(debug=True) #servidor local