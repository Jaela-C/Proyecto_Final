# **Proyecto_Final**
## Pulso político de ciudades y provincias del Ecuador
   - **Provincias del Ecuador - Twitter a CouchDB**
       - Los scripts que contienen el nombre de cada una de las provincias del Ecuador, realizan el mismo proceso que será detallado a continuación. La única diferencia que presentan es la ubicación de cada una de las provincias.
       - Las librerías importadas fueron: couchdb, Stream, OAuthHandler, StreamListener, json y la principal tweepy.
       - La librería couchdb almacena los datos que se extraen con el uso de tweepy.
       - Para utilizar el API de Twitter es necesario declarar las credenciales que nos porporciona Twitter.
       - Se usa una clase llamada *listener* para realizar el streaming.
       - Se definen dos funciones: on_data y on_error; la primera nos permite almacenar los datos en formato JSON y la segunda muestra un mensaje en el caso de que ocurra un error cuando se está ejecutando el código.
       - Iniciamos el servidor de couchdb con la dirección: *'http://<'user'>:<'password'>@localhost:5984/'*
       - En el caso de no existir la base de datos en couchdb la creamos o guardamos los datos en una base existente.
       - Para realizar la exracción de datos de un lugar determinado se usa el filtro *locations* y se envían coordenadas de geolocalización.
   - **Configuración para Logstash**
       - Los archivos *política* y *pulso-político* permiten realizar una 'configuración' para enviar los datos de couchdb a *elasticsearch*.
       - Los archivos reciben: nombre de la base de datos presente en couchdb, la contraseña y el nombre de usuario.
       - Los archivos envían a elasticsearch: el host y el nombre del index a crearse.
   - **Mapping**
       - El archivo se usa para darle un correcto formato a las fechas.
   - **Análisis de sentimientos**
       - Los scripts: *sentiment_arauz* y *sentiment_lasso* realizan el mismo proceso que será detallado a continuación. La única diferencia que presentan es el criterio de búsqueda que se usa para obtener los datos.
       - Las librerías importadas fueron: Stream, OAuthHandler, StreamListener, json, textblob, elasticsearch y la principal tweepy.
       - Se crea una instancia de elasticserarch
       - Para utilizar el API de Twitter es necesario declarar las credenciales que nos porporciona Twitter.
       - Se crea una clase llamada *TweetStreamListener* que contiene las funciones *on_data* y *on_error*.
       - Procedemos a decodificar el JSON y guardamos el tweet en TextBlob.
       - Para determinar si los sentimientos son positivos o negativos realizamos un if, elif y else; si la polaridad es menor que 0, el sentimiento es negativo, si la polaridad es igual a 0, el sentimiento es neutral, de no cumplirse esas condiciones el sentimiento es positivo.
       - Se crea un index que almacena información en *elasticsearch*, los campos guardados son: autor, fecha, mensaje, locación, polaridad, sentimiento y subjetividad.
       - En el caso de tener un error el código nos muestra el estado.
       - Se crea una instancia de tweepy.
       - Se autentica con las credenciales del API de Twitter.
       - Se crea una instancia para Twitter Stream.
       - Para realizar la extracción de datos se usa el filtro *track* y se envían palabras clave como: ecuarauz, MashiRafael, Elecciones2021 y Guillermo Lasso, respectivamente.
   - **Facebook a CouchDB**
       - Los scripts: *facebook_lasso* y *facebook_arauz* realizan el mismo proceso que será detallado a continuación. La única diferencia que presentan es la página de la cual se extrae información para cada candidato.
       - Las librerías importadas fueron: couchdb, json, time y la principal facebook_scraper.
       - Iniciamos el servidor de couchdb con la dirección: *'http://<'user'>:<'password'>@localhost:5984/'*
       - Guardamos los datos en una base existente.
       - Realizamos un *for* que permita navegar en cada uno de los posts que estén presentes en las cuentas de: LassoGuillermo y ecuarauz2021. La búsqueda se hizo en 1000 páginas.
       - Dentro del *for* se guarda la información extraída en un *doc* tipo JSON, se realizan verificaciones y se declara un tiempo de espera para evitar un bloqueo de cuenta.
       - Todos los datos se envían a una base de datos de couchdb.

## Extracción de datos Juegos en línea

* **Procedimiento**
  * Con el fin de reducir el tamaño de la muestra a medir se desarrollaron dos Scripts en Python utilizados 
    para realizar Web Scraping en una página web que contiene bastante información sobre juegos, jugadores, 
    torneos, etc. Esta página web es [Liquipedia](https://liquipedia.net/).
    
    De esta página web se extrajo un total de 30 juegos dentro del ámbito de los Electronic Sport (e-sport), 
    además de se extrajo la nacionalidad de los jugadores dentro del ámbito de los e-sports. Esto fue de gran ayuda 
    para definir la dirección de la investigación. 
    
    Se decidió realizar la búsqueda por medio de un track de palabras ya que, arrojaban más datos que hacerlo por
    localización extraída de la nacionalidad de los jugadores.
    
    Estos datos extraídos, ya presentaban una localización en la mayoría de casos, entonces podría ser más fácil si se 
    lo buscaba de esta manera.
    
    Finalmente se compararon las gráficas generadas, con otras extraídas de la plataforma [Kaggle](https://www.kaggle.com/)
    para verificar si existía alguna similitud con lo investigado.

##
