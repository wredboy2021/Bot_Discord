import sqlite3

Conexion=sqlite3.connect("Economia")
Mi_Cursor=Conexion.cursor()
Mi_Cursor.execute("CREATE TABLE Economia (Numeracion INTEGER PRIMARY KEY AUTOINCREMENT,Dato TEXT)")
Lista=["La economía mundial equivale a unos 87 billones de dólares", "La economía de Estados Unidos representa el 24% del PIB mundial", 
"La India es la tercera economía más grande del mundo", "El 80% de los trabajos en Estados Unidos son de servicios", 
"El turismo aporta un 11% del PIB mundial", "China es el mayor exportador mundial", "El comercio electrónico representa un 8% del comercio mundial", 
"Los países de la Eurozona tienen un PIB combinado de unos 14 billones de dólares", 
"Las empresas de Estados Unidos venden más de 2 billones de dólares en productos al año", 
"Más de la mitad de los ingresos mundiales provienen de los servicios", "El PIB mundial está compuesto por más de mil millones de personas", 
"El comercio internacional representa el 25% del PIB mundial", "El sector de la agricultura representa el 10% del PIB mundial", 
"La inflación mundial es del 2,5% anual", "La tasa de desempleo mundial es del 5,2%", "El gasto en defensa mundial equivale a unos 1,8 billones de dólares",
"La deuda externa de los países en desarrollo asciende a 1,3 billones de dólares", 
"La economía mundial creció un 3% en 2016", "La inversión extranjera directa (IED) asciende a 1,3 billones de dólares", 
"La economía mundial podría alcanzar los 100 billones de dólares en 2020", "El PIB de África ha crecido un 5,1% en los últimos años", 
"Más de la mitad de la población mundial vive en países en desarrollo", "El comercio internacional representa el 59% del PIB mundial", 
"El comercio de bienes y servicios entre países alcanzó los 17 billones de dólares en 2016",
 "El comercio de divisas alcanzó los 5 billones de dólares diarios en 2016",
   "Las empresas multinacionales representan el 40% del comercio mundial", "El PIB mundial alcanzó los 74 billones de dólares en 2016",
     "El comercio de divisas entre países aumentó en un 16% entre 2015 y 2016", "El ahorro mundial es de unos 113 billones de dólares", 
     "La inversión extranjera directa (IED) en América Latina y el Caribe aumentó un 6,4% en 2016", 
     "Las remesas internacionales llegaron a los 476 mil millones de dólares en 2016",
       "El crecimiento del PIB mundial fue del 3,1% en 2016", "La tasa de desempleo juvenil es del 13,2% en la UE",
         "El PIB mundial se espera que crezca un 3% en 2017", "Las reservas de divisas de los países aumentaron a unos 11 billones de dólares en 2016", 
         "El PIB de Estados Unidos equivale a unos 18 billones de dólares", "El comercio mundial alcanzó los 17 billones de dólares en 2016", 
         "Más del 80% de la población mundial vive con menos de 10 dólares al día", "La deuda externa de los países en desarrollo es de unos 4 billones de dólares", 
         "La inversión extranjera directa (IED) en Asia y el Pacífico aumentó un 4,9% en 2016", 
         "Las exportaciones de bienes y servicios de la UE alcanzaron los 2.8 billones de euros en 2016", 
         "El PIB de Estados Unidos creció un 1,6% en 2016", "Las remesas internacionales aumentaron un 6,3% en 2016", 
         "El comercio de divisas entre países aumentó un 20% entre 2015 y 2016", 
         "Las exportaciones de bienes y servicios de los Estados Unidos alcanzaron los 2.3 billones de dólares en 2016", 
         "La tasa de desempleo juvenil en Estados Unidos es del 11,5%", 
         "Más del 60% de la inversión extranjera directa (IED) en América Latina va a Brasil", 
         "La inversión extranjera directa (IED) en América Latina se incrementó un 8% en 2016", 
         "La inversión extranjera directa (IED) en Asia y el Pacífico aumentó un 3,7% en 2016", 
         "El comercio electrónico representa el 7,4% del comercio mundial", 
         "El PIB de Latinoamérica equivale a unos 5 billones de dólares", 
         "Más de la mitad de la población mundial vive con menos de 2 dólares al día", 
         "Los países de la Eurozona tienen un PIB combinado de unos 17 billones de dólares", 
         "La inversión extranjera directa (IED) en los Estados Unidos aumentó un 4% en 2016", 
         "La tasa de desempleo juvenil en la UE es del 20,3%", "El comercio internacional representa el 24,5% del PIB mundial", 
         "Las exportaciones de bienes y servicios de los Estados Unidos aumentaron un 2,6% en 2016", 
         "Las exportaciones de bienes y servicios de la UE aumentaron un 3,7% en 2016", 
         "El comercio de divisas entre países aumentó un 23% entre 2015 y 2016", 
         "El PIB de África se incrementó un 5,1% en 2016", "Más del 90% de los trabajos en Estados Unidos son de servicios", 
         "Las exportaciones de bienes y servicios de la UE alcanzaron los 3.2 billones de euros en 2016", 
         "La tasa de desempleo en Estados Unidos es del 4,7%", "El PIB mundial podría alcanzar los 88 billones de dólares en 2017", 
         "La inflación mundial se espera que se mantenga alrededor del 3% en 2017", "El PIB de Estados Unidos aumentó un 2,3% en 2016", 
         "El comercio electrónico representa el 12,6% del comercio mundial en América Latina", 
         "El comercio de bienes y servicios entre países alcanzó los 19 billones de dólares en 2017", 
         "La inversión extranjera directa (IED) en América Latina y el Caribe aumentó un 9,4% en 2017", "Las remesas internacionales llegaron a los 539 mil millones de dólares en 2017", "El PIB mundial se espera que crezca un 3,6% en 2017", "El comercio de divisas entre países aumentó un 22% entre 2016 y 2017", "Las exportaciones de bienes y servicios de los Estados Unidos aumentaron un 3,3% en 2017", "El comercio internacional representa el 26,5% del PIB mundial en 2017", "Las exportaciones de bienes y servicios de la UE aumentaron un 3,2% en 2017", "El PIB de Estados Unidos aumentó un 2,9% en 2017", "Las inversiones extranjeras directas (IED) en América Latina aumentaron un 10% en 2017", "La tasa de desempleo juvenil en Estados Unidos es del 10,5%", "La inversión extranjera directa (IED) en Asia y el Pacífico aumentó un 4,3% en 2017", "El PIB de Latinoamérica aumentó un 1,7% en 2017", "La inversión extranjera directa (IED) en los Estados Unidos aumentó un 5,1% en 2017", "El comercio de divisas entre países aumentó un 17% entre 2016 y 2017", "El PIB de África se incrementó un 3,6% en 2017", "El comercio electrónico representa el 15,7% del comercio mundial en Asia y el Pacífico", "El comercio de bienes y servicios entre países alcanzó los 22 billones de dólares en 2018", "La inversión extranjera directa (IED) en América Latina y el Caribe aumentó un 7,8% en 2018", "Las remesas internacionales llegaron a los 602 mil millones de dólares en 2018", "El PIB mundial se espera que crezca un 3,7% en 2018", "El comercio de divisas entre países aumentó un 24% entre 2017 y 2018", "Las exportaciones de bienes y servicios de los Estados Unidos aumentaron un 4,2% en 2018", "El comercio internacional representa el 28,5% del PIB mundial en 2018", "Las exportaciones de bienes y servicios de la UE aumentaron un 4,1% en 2018", "El PIB de Estados Unidos aumentó un 2,9% en 2018", "Las inversiones extranjeras directas (IED) en América Latina aumentaron un 11% en 2018", "La tasa de desempleo juvenil en Estados Unidos es del 9,2%", "La inversión extranjera directa (IED) en Asia y el Pacífico aumentó un 5,1% en 2018", "El PIB de Latinoamérica aumentó un 1,1% en 2018", "La inversión extranjera directa (IED) en los Estados Unidos aumentó un 6,2% en 2018", "El comercio de divisas entre países aumentó un 21% entre 2017 y 2018", "El PIB de África se incrementó un 3,2% en 2018", "El comercio electrónico representa el 18,4% del comercio mundial en América Latina", "El comercio de bienes y servicios entre países alcanzó los 25 billones de dólares en 2019", "La inversión extranjera directa (IED) en América Latina y el Caribe aumentó un 6,7% en 2019"]
new_list = []
for element in Lista:
    new_list.append((element,))
lista = new_list

Mi_Cursor.executemany("INSERT INTO Economia VALUES (NULL,?)",lista)
Conexion.commit()
Conexion.close()