# IIC2026'2 - Visualización de la Información - Examen
- Autor: Raimundo Martínez Rioseco (N° Alumno: 16637232)

En esta entrega se incluyen los siguientes archivos:
- index.html - Contiene el HTML con el informe y botón hacia la herramienta de visualización construida.
- examen.html - Contiene el HTML sobre el cual se construye la herramienta de visualización.
- examen.js - Contiene el código en JavaScript y D3.js usado para construir la herramienta de visualización.
- style.css - Contiene el estilo del informe y la herramienta de visualización.
- artist.csv - Contiene los datos de la artista.
- albums.csv - Contiene los datos de los álbumes de la artista.
- tracks.csv - Contiene los datos de las pistas de la artista.
- dataset_examen.ipynb - Contiene el código usado para la construcción del dataset.


Para visualizar correctamente la herramienta de visualización se debe abrir un servidor de http usando el comando en consola:
> python -m http.server [número de puerto]

Y luego abrir un navegador y dirigirse a
> http://localhost:[número de puerto]/

El número de puerto usado durante el desarrollo de la herramienta fue 8000. El navegador usado durante el desarrollo fue Google Chrome versión 107.0.5304.107. Los archivos .csv, .html, .js y .css deben encontrarse en el mismo directorio.

En la herramienta de visualización se generan varios mensajes de advertencias. Esto se debe al embed de Spotify que se incluye en la herramienta de visualización y cuyo funcionamiento interno no es parte del alcance de este trabajo. Solo se aseguró que las muestras de audio funcionaran en el contexto de la herramienta de visualización.