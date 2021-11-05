Los tests de la Api Rest se realizarán con la herramienta automatica de Newman de Postman.
Se deberá asegurar que en el ordenador donde se vayan a realizar los tests se encuentren los archivos siguientes:

-Archivo exportado de la coleccion json: ej."archivoColeccion.json"
-Archivo exportado del entorno postman en json: ej,"archivoEntorno.json"

El test se realizará en la consola(asegurate de tener instalado node.js)
*****Si no tenemos instalado la herramienta newman, ejecutar el siguiente comando:
	npm install -g newman

Una vez instalado ejecutar en el directorio donde esten los anteriores archivos mencionados el siguiente comando:

	newman run -e [nombrearchivoentorno] [nombrearchivocoleccion]

/*Si no funciona asegurate de haber enchufado el xampp y arrancado el servidor en el pueerto 8080 desde python*/