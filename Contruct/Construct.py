import sqlite3

Conexion=sqlite3.connect("Web.db")
Mi_Cursor=Conexion.cursor()
Mi_Cursor.execute("CREATE TABLE Web(Numeracion INTEGER PRIMARY KEY AUTOINCREMENT,Dato TEXT)")
datos_curiosos=[ ("https://www.wikipedia.org/", "Enciclopedia en línea gratuita y colaborativa"),    ("https://www.nytimes.com/", "Periódico estadounidense con noticias de todo el mundo"),    ("https://www.reddit.com/", "Plataforma social de discusión y agregación de noticias"),    ("https://www.youtube.com/", "Plataforma de alojamiento de vídeos"),    ("https://www.bbc.com/", "Portal de noticias y contenido multimedia de la BBC"),    ("https://www.nationalgeographic.com/", "Revista de divulgación científica y exploración"),    ("https://www.spotify.com/", "Servicio de música en streaming"),    ("https://www.codecademy.com/", "Plataforma para aprender a programar"),    ("https://www.coursera.org/", "Plataforma de educación en línea con cursos de universidades de todo el mundo"),
                 ("https://www.amazon.com/", "Plataforma de venta en línea de productos de todo tipo"),    ("https://www.instagram.com/", "Red social de fotografía y video"),    ("https://www.twitch.tv/", "Plataforma de streaming de videojuegos y eventos en vivo"),    ("https://www.medium.com/", "Plataforma de publicación y lectura de artículos y ensayos"),    ("https://www.stackoverflow.com/", "Comunidad de programadores para hacer preguntas y obtener respuestas"),    ("https://www.imdb.com/", "Base de datos en línea de información sobre películas, series de televisión y programas de streaming"),    ("https://www.zillow.com/", "Portal de bienes raíces para encontrar casas, apartamentos y propiedades en venta o alquiler"),    ("https://www.yelp.com/", "Plataforma de recomendaciones y reseñas de restaurantes, bares y negocios locales"),    ("https://www.quizlet.com/", "Plataforma de aprendizaje en línea con herramientas para crear y estudiar flashcards y exámenes"),    ("https://www.duolingo.com/", "Plataforma para aprender idiomas con juegos, ejercicios y pruebas"),
                 ("https://www.couchsurfing.com/", "Comunidad global de viajeros que conecta a las personas que buscan alojamiento gratuito con los anfitriones locales que ofrecen un lugar para quedarse"),    ("https://archive.org/", "Biblioteca digital que ofrece acceso gratuito a millones de libros, películas, música y más"),    ("https://www.freerice.com/", "Sitio web de juegos educativos que te permite aprender y donar arroz gratis a través del Programa Mundial de Alimentos de las Naciones Unidas"),    ("https://www.wolframalpha.com/", "Motor de búsqueda computacional que resuelve problemas matemáticos y científicos, proporciona datos y gráficos y ofrece análisis de texto y lenguaje natural"),    ("https://www.brainpickings.org/", "Blog sobre la creatividad, la literatura, el arte, la ciencia y la filosofía"),    ("https://radio.garden/", "Mapa interactivo del mundo que permite escuchar emisoras de radio en todo el planeta"),    ("https://www.atlasobscura.com/", "Guía en línea de lugares inusuales, curiosidades y maravillas del mundo"),
                  ("https://thispersondoesnotexist.com/", "Sitio web que genera una cara de persona completamente falsa cada vez que se recarga la página, utilizando la inteligencia artificial"),    ("https://www.boredpanda.com/", "Comunidad creativa en línea que comparte ideas e inspiración para la vida cotidiana"),    ("https://www.duolingo.com/", "Plataforma de aprendizaje de idiomas en línea, gratuita y gamificada, que ayuda a los usuarios a aprender nuevos idiomas de manera divertida"),    ("https://www.myfridgefood.com/", "Sitio web que te permite ingresar los ingredientes que tienes en tu refrigerador y te da recetas para cocinar"),    ("https://www.mentalfloss.com/", "Revista en línea que presenta noticias interesantes e historias curiosas en una variedad de temas"),    ("https://www.ted.com/", "Plataforma de conferencias en línea que presenta charlas inspiradoras y educativas de expertos en diversas disciplinas"),    ("https://www.uncommongoods.com/", "Tienda en línea de regalos y artículos para el hogar inusuales y creativos, hechos por artistas y diseñadores independientes"),
                  ]
datos_curiosos = [
    "https://www.wikipedia.org/ - Enciclopedia en línea gratuita y colaborativa",
    "https://www.nytimes.com/ - Periódico estadounidense con noticias de todo el mundo",
    "https://www.reddit.com/ - Plataforma social de discusión y agregación de noticias",
    "https://www.youtube.com/ - Plataforma de alojamiento de vídeos",
    "https://www.bbc.com/ - Portal de noticias y contenido multimedia de la BBC",
    "https://www.nationalgeographic.com/ - Revista de divulgación científica y exploración",
    "https://www.spotify.com/ - Servicio de música en streaming",
    "https://www.codecademy.com/ - Plataforma para aprender a programar",
    "https://www.coursera.org/ - Plataforma de educación en línea con cursos de universidades de todo el mundo",
    "https://www.amazon.com/ - Plataforma de venta en línea de productos de todo tipo",
    "https://www.instagram.com/ - Red social de fotografía y video",
    "https://www.twitch.tv/ - Plataforma de streaming de videojuegos y eventos en vivo",
    "https://www.medium.com/ - Plataforma de publicación y lectura de artículos y ensayos",
    "https://www.stackoverflow.com/ - Comunidad de programadores para hacer preguntas y obtener respuestas",
    "https://www.imdb.com/ - Base de datos en línea de información sobre películas, series de televisión y programas de streaming",
    "https://www.zillow.com/ - Portal de bienes raíces para encontrar casas, apartamentos y propiedades en venta o alquiler",
    "https://www.yelp.com/ - Plataforma de recomendaciones y reseñas de restaurantes, bares y negocios locales",
    "https://www.quizlet.com/ - Plataforma de aprendizaje en línea con herramientas para crear y estudiar flashcards y exámenes",
    "https://www.duolingo.com/ - Plataforma para aprender idiomas con juegos, ejercicios y pruebas",
    "https://www.couchsurfing.com/ - Comunidad global de viajeros que conecta a las personas que buscan alojamiento gratuito con los anfitriones locales que ofrecen un lugar para quedarse",
    "https://archive.org/ - Biblioteca digital que ofrece acceso gratuito a millones de libros, películas, música y más",
    "https://www.freerice.com/ - Sitio web de juegos educativos que te permite aprender y donar arroz gratis a través del Programa Mundial de Alimentos de las Naciones Unidas",
    "https://www.wolframalpha.com/ - Motor de búsqueda computacional que resuelve problemas matemáticos y científicos, proporciona datos y gráficos y ofrece análisis de texto y lenguaje natural",
    "https://www.brainpickings.org/ - Blog sobre la creatividad, la literatura, el arte, la ciencia y la filosofía",
    "https://radio.garden/ - Mapa interactivo del mundo que permite escuchar emisoras de radio en todo el planeta",
    "https://www.atlasobscura.com/", "Guía en línea de lugares inusuales, curiosidades y maravillas del mundo",
 "https://thispersondoesnotexist.com/ Sitio web que genera una cara de persona completamente falsa cada vez que se recarga la página, utilizando la inteligencia artificial",
 "https://www.boredpanda.com/ Comunidad creativa en línea que comparte ideas e inspiración para la vida cotidiana",
 "https://www.duolingo.com/ Plataforma de aprendizaje de idiomas en línea, gratuita y gamificada, que ayuda a los usuarios a aprender nuevos idiomas de manera divertida",
 "https://www.myfridgefood.com/ Sitio web que te permite ingresar los ingredientes que tienes en tu refrigerador y te da recetas para cocinar",
 "https://www.mentalfloss.com/ Revista en línea que presenta noticias interesantes e historias curiosas en una variedad de temas",
 "https://www.ted.com/ Plataforma de conferencias en línea que presenta charlas inspiradoras y educativas de expertos en diversas disciplinas",
 "https://www.uncommongoods.com/ Tienda en línea de regalos y artículos para el hogar inusuales y creativos, hechos por artistas y diseñadores independientes",
    ]

new_list=[]
for element in datos_curiosos:
    new_list.append((element,))
lista = new_list

Mi_Cursor.executemany("INSERT INTO Web VALUES (NULL,?)",lista)
Conexion.commit()
Conexion.close()