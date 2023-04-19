import sqlite3

Conexion=sqlite3.connect("Backrooms.db")
Mi_Cursor=Conexion.cursor()
Mi_Cursor.execute("CREATE TABLE Backrooms_Niveles (Numeracion INTEGER PRIMARY KEY AUTOINCREMENT,Dato TEXT)")

niveles =["El Nivel 1 es un almacén grande y en expansión que cuenta con pisos y paredes de concreto, barras de refuerzo expuestas y una niebla que cuelga a poca altura sin una fuente discernible. La niebla a menudo se fusiona en condensación, formando charcos en el piso en áreas inconsistentes. A diferencia del Nivel 0, este nivel posee un suministro constante de agua y electricidad, lo que permite la habitación indefinida de los Wanderers siempre que se tomen las precauciones adecuadas. También es mucho más expansivo, posee escaleras, ascensores, habitaciones aisladas y pasillos.",
    "El Nivel 0 es un espacio expansivo no euclidiano, que se asemeja a las habitaciones traseras de una tienda minorista. Todas las habitaciones en el Nivel 0 comparten las mismas características superficiales, como el papel tapiz monoamarillo gastado, la alfombra vieja y húmeda, los enchufes eléctricos dispersos y la iluminación fluorescente colocada de manera inconsistente. Aparte de estas características comunes, no hay dos habitaciones idénticas dentro del nivel.",
    "El Nivel 2 consiste principalmente en túneles de mantenimiento de hormigón gris oscuro, que se extienden por millones de millas. Las paredes están revestidas con tuberías y ocasionalmente con conductos de ventilación, que a menudo contienen un líquido espeso y viscoso de color negro. A veces se pueden encontrar puertas, pero la mayoría están cerradas o conducen a callejones sin salida. Estas habitaciones suelen albergar estantes con una variedad aleatoria de objetos, ocasionalmente computadoras.",
    "El Nivel 3 es una serie de pasillos largos, oscuros y retorcidos que funcionan de manera similar al Nivel 0. Todos consisten en habitaciones segmentadas aleatoriamente, que no se forman en un patrón en particular, y son extremadamente ruidosas con los ruidos de la maquinaria. Los pasillos son muy estrechos y cerrados, algunos incluso requieren Wanderers de altura media y construcción para doblarse, encorvarse, gatear o caminar de lado a través de ellos.",
    "El Nivel 4 se asemeja a un edificio de oficinas vacío que se encuentra casi completamente desprovisto de muebles. Algunas habitaciones en este nivel tienen ventanas, aunque la mayoría de ellas están completamente oscurecidas. Cualquier ventana que no esté oscurecida es una trampa y debe evitarse a toda costa.",
    "El Nivel 5 es un complejo hotelero infinito, con muchas habitaciones y pasillos. El nivel en sí parece haber sido construido en la década de los años 30, con muebles que datan de los años 20. Hay tres áreas principales en el Nivel 5 que son totalmente accesibles.",
    'El nivel 6 se puede describir como un espacio segmentado por paredes metálicas colocado de manera aleatoria, con un suelo fabricado de lo que parece ser concreto, y un sistema de tuberías que abundan en las paredes; sin límite presente. Las tuberías del nivel brotan un líquido que hasta el momento es desconocido; únicamente sabiéndose esto mediante anécdotas de algunos Wanderers. Rumores indican que esto podría tratarse de agua de almendras.',
    'El Nivel 7 es un océano imposiblemente grande que parece extenderse infinitamente en todas las direcciones. A pesar de la ausencia de fuentes de luz fijas dentro del nivel, una tenue luz natural está presente en todo el nivel. La exploración detallada de este océano es escasa debido al peligro extremo y a la cantidad de preparación que requiere para navegar. Lo que sabemos del Nivel 7 es lo siguiente:',
    'El Nivel 8 está formado por enormes cavernas y pequeños sistemas de cuevas que se retuercen como los sistemas subterráneos normales. Al igual que el Nivel 7, está completamente oscuro sin fuentes de luz adecuadas. El Nivel 8 es muy húmedo, con Agua de Almendras fluyendo de las paredes y el techo. Las estalactitas y estalagmitas parecen ser muy comunes en el Nivel 8. Los sonidos hacen eco en todo el nivel, por lo que es relativamente fácil escuchar el peligro potencial, o incluso atraerlo si no se tiene cuidado. El Nivel 8 normalmente carece de luz natural, pero fuentes de luz de origen desconocido brillan en las paredes húmedas, haciendo que el nivel brille ligeramente en algunas zonas.',
    'El Nivel 9, conocido como "Suburbios Oscuros" o "Los Suburbios", es una extensa y sinuosa red de carreteras asfaltadas y casas residenciales, parecida a un vecindario suburbano moderno. Las fuentes naturales de luz en el nivel son escasas, ya que aparte de su permanente falta de luz diurna, que puede servir de obstáculo para los Wanderers, las luces que emanan de su plétora de estructuras rara vez suelen funcionar. Además de estos obstáculos a la visibilidad, el nivel está cubierto por una espesa niebla que envuelve sus calles en la oscuridad e impide ver más allá de una distancia aproximada de diez metros. Junto con los fuertes vientos y las tormentas que de vez en cuando azotan el nivel, la temperatura media suele oscilar en torno a los 10°C (50°F), lo que hace que el clima general del Nivel 9 sea un obstáculo importante para los que deambulan por sus calles.',
    "El Nivel 10 es un extenso pastizal de campos de trigo y cebada que se extienden infinitamente en todas direcciones, divididos en parcelas por hileras de árboles y arbustos. El clima del nivel nunca parece cambiar de un cielo nublado y plomizo, con breves e infrecuentes rachas de lluvia ligera y niebla. La lúgubre atmósfera del Nivel 10, unida a su invariable estado de luz diurna, dificulta en cierta medida la percepción del tiempo, ya que sólo las ocasionales ráfagas de viento entre los cultivos rompen la uniformidad.",
    "El Nivel 11 es similar al Nivel 9 en tamaño y estructura, sin embargo, en lugar de consistir en casas suburbanas de clase media, está poblado de apartamentos, edificios de oficinas y varios edificios de departamentos. La gente ha informado que parece tener aspectos y puntos de referencia de varias ciudades conocidas, incluidas, entre otras, Nueva York, Chicago, Los Ángeles, St. Louis y Toronto. Estas estructuras tienen las mismas propiedades que el resto de los edificios del Nivel 11 mencionados anteriormente. El Nivel 11 también está repleto de parques, plazas, pistas de patinaje sobre hielo, canchas de baloncesto, estaciones de metro y tiendas minoristas.", 
    "La luz blanca era cegadora; me zumbaba la cabeza con sólo mirarla. Me encontraba en una habitación perfectamente prístina, nada rompía el blanco puro hasta que levanté la cabeza. Una mesa y una silla colocadas perfectamente en el centro de la habitación me confundieron, encima colgaban dos luces, me recordaban a las que vi una vez en un pub. Me escocían los cortes por los cristales rotos; estaban a mi alrededor y, sin embargo, no podía verlos. La luz parecía refractarse y empeorar mi dolor de cabeza cuando miraba más allá; el fuerte zumbido de la estática no ayudaba. (Parte del relato del nivel 12)", 
    "El Nivel 13 es aparentemente un edificio de apartamentos con un número extremadamente alto de pisos. Dentro de cada piso, hay muchas residencias pequeñas, cada una con un número en la puerta. Estos números están en un sistema en el que se enumeran el piso, la sección del piso y el número de apartamento. El diseño actual del edificio es similar al de la arquitectura típica de los años ochenta. Las paredes del pasillo son blancas y la alfombra tiene un diseño geométrico marrón. Este diseño es consistente en todos los pisos.", 
     "El Nivel 14 se asemeja a un hospital militar abandonado hace mucho tiempo y que actualmente se encuentra en un estado de deterioro como consecuencia del envejecimiento. El agua contaminada que contiene fluidos corporales se filtra por las tuberías y se acumula en el suelo"]

new_list = []
for element in niveles:
    new_list.append((element,))
lista = new_list

Mi_Cursor.executemany("INSERT INTO Backrooms_Niveles VALUES (NULL,?)",lista)
Conexion.commit()
Conexion.close()