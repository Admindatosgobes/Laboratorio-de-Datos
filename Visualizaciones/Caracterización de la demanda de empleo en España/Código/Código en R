#"Accidentes de trafico ocurridos en la ciudad de Madrid"#

#Pasos que se seguiran en este codigo
# 1. Carga de datos. 
# 2. Crear tablas de datos de trabajo. 
# 3. Seleccion de variables de interes.
# 4. Transformacion de tipos de variables.
# 5. Verificacion de datos ausentes. 
# 6. Asignacion de niveles categoricos a diferentes variables 
# 7. Generacion del archivo de entrada para Elastic con los datos transformados. 


# Establecer directorio de trabajo 
setwd("C:/Users/esansegu/Proyecto_GitHub/Accidentes de trafico en Madrid")


# Instalacion y carga de librerias 

#Realizamos una lista de las librerias que nos interesa cargar en el entorno de R

librerias <- c("tidyverse", "lubridate", "data.table")

#Descargamos e instalamos las librerias
package.check <- lapply(
  librerias,
  FUN = function(x) {
    if (!require(x, character.only = TRUE)) {
      install.packages(x, dependencies = TRUE)
      library(x, character.only = TRUE)
    }
  }
)

# Cargamos todos los conjuntos de datos que nos interesen en nuestro entorno de 
# desarrollo. 

#Generamos una carpeta en la cual se descargaran todos los conjuntos de datos
if (dir.exists(".datasets") == FALSE)
  dir.create("./datasets")

#Nos colocamos dentro de la carpeta 
setwd("./datasets")

#Listado de datasets que descargaremos para realizar la visualizacion
datasets <- c("https://datos.madrid.es/egob/catalogo/300228-10-accidentes-trafico-detalle.csv",
              "https://datos.madrid.es/egob/catalogo/300228-11-accidentes-trafico-detalle.csv",
              "https://datos.madrid.es/egob/catalogo/300228-12-accidentes-trafico-detalle.csv",
              "https://datos.madrid.es/egob/catalogo/300228-13-accidentes-trafico-detalle.csv", 
              "https://datos.madrid.es/egob/catalogo/300228-14-accidentes-trafico-detalle.csv",
              "https://datos.madrid.es/egob/catalogo/300228-15-accidentes-trafico-detalle.csv",
              "https://datos.madrid.es/egob/catalogo/300228-16-accidentes-trafico-detalle.csv", 
              "https://datos.madrid.es/egob/catalogo/300228-17-accidentes-trafico-detalle.csv",
              "https://datos.madrid.es/egob/catalogo/300228-18-accidentes-trafico-detalle.csv",
              "https://datos.madrid.es/egob/catalogo/300228-19-accidentes-trafico-detalle.csv",
              "https://datos.madrid.es/egob/catalogo/300228-21-accidentes-trafico-detalle.csv",
              "https://datos.madrid.es/egob/catalogo/300228-22-accidentes-trafico-detalle.csv"
)

#Descargamos y cargamos en el entorno de R los datasets de interes
dt <- list()
for (i in 1:length(datasets)){
  files <- c("Accidentalidad2010",
             "Accidentalidad2011",
             "Accidentalidad2012",
             "Accidentalidad2013",
             "Accidentalidad2014",
             "Accidentalidad2015",
             "Accidentalidad2016",
             "Accidentalidad2017", 
             "Accidentalidad2018", 
             "Accidentalidad2019", 
             "Accidentalidad2020",
             "Accidentalidad2021")
  download.file(datasets[i], files[i])
  filelist <- list.files(".")
  print(i)
  dt[i] <- lapply(filelist[i], read_delim, ";", escape_double = FALSE, 
                  locale = locale(encoding = "WINDOWS-1252"),
                  trim_ws = TRUE)
}

# Union de todas las tablas de accidentalidad cargadas en R
Accidentalidad <- rbindlist(dt, use.names =TRUE, fill =TRUE)
str(Accidentalidad)

Accidentalidad<-unite(Accidentalidad, LESIVIDAD ,c(25,44), remove = TRUE, na.rm = TRUE)
Accidentalidad<-unite(Accidentalidad, NUMERO_VICTIMAS ,c(20,27), remove = TRUE, na.rm = TRUE)
Accidentalidad<-unite(Accidentalidad, RANGO_EDAD, c(26,35,42), remove =TRUE, na.rm = TRUE)
Accidentalidad<-unite(Accidentalidad, TIPO_VEHICULO, c(22,40), remove = TRUE, na.rm = TRUE)
View(Accidentalidad)


# Re-asignar los tipos de variables

# Cambiar el tipo de variable a tipo fecha
Accidentalidad$FECHA <- dmy(Accidentalidad$FECHA)

#Dividir la fecha en tres variables: año, mes y dia

#Creamos la variable YEAR
Accidentalidad$YEAR <- year(Accidentalidad$FECHA)
Accidentalidad$YEAR <- as.factor(Accidentalidad$YEAR)
str(Accidentalidad$YEAR)


#Creamos la variable MONTH
Accidentalidad$MONTH <- month(Accidentalidad$FECHA)
Accidentalidad$MONTH <- as.factor(Accidentalidad$MONTH)

#Asignamos los niveles a la variable "MONTH"
levels(Accidentalidad$MONTH) <- c("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
                                  "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre",
                                  "Diciembre")
str(Accidentalidad$MONTH)


#Generamos la variable DAY, con los dias de la semana a partir de la fecha
Accidentalidad$DAY <- wday(Accidentalidad$FECHA) 
Accidentalidad$DAY <- as.factor(Accidentalidad$DAY)

#Asignamos los niveles a la variable "DAY"
levels(Accidentalidad$DAY) <- c("Domingo", "Lunes", "Martes", "Miercoles", "Jueves",
                                "Viernes", "Sabado")
str(Accidentalidad$DAY)


#Re-asignar el resto de variables a tipo factor
Accidentalidad$`TIPO ACCIDENTE` <- as.factor(Accidentalidad$`TIPO ACCIDENTE`)
str(Accidentalidad$`TIPO ACCIDENTE`)
Accidentalidad$TIPO_VEHICULO <- as.factor(Accidentalidad$TIPO_VEHICULO)
str(Accidentalidad$TIPO_VEHICULO)
Accidentalidad$`TIPO PERSONA`<- as.factor(Accidentalidad$`TIPO PERSONA`)
str(Accidentalidad$`TIPO PERSONA`)
Accidentalidad$RANGO_EDAD <- as.factor(Accidentalidad$RANGO_EDAD)
str(Accidentalidad$RANGO_EDAD)
Accidentalidad$SEXO <- toupper(Accidentalidad$SEXO)
Accidentalidad$SEXO <- as.factor(Accidentalidad$SEXO)
str(Accidentalidad$SEXO)
Accidentalidad$LESIVIDAD <- as.factor(Accidentalidad$LESIVIDAD)
str(Accidentalidad$LESIVIDAD)
Accidentalidad$DISTRITO <- as.factor(Accidentalidad$DISTRITO)
str(Accidentalidad$DISTRITO)


#Seleccionar las variables de la tabla que nos interesen para trabajar
Accidentalidad <- Accidentalidad %>% select ((c("FECHA", "DISTRITO", "LUGAR ACCIDENTE",
                                                "TIPO_VEHICULO","TIPO PERSONA", "SEXO", 
                                                "LESIVIDAD", "RANGO_EDAD", "TIPO ACCIDENTE",
                                                "NUMERO_VICTIMAS","YEAR", "MONTH", "DAY")))


str(Accidentalidad)


# Tratamiento de NAs
any(is.na(Accidentalidad)) 
sum(is.na(Accidentalidad)) #Detectamos el numero de NAs que presenta la tabla 
mean(is.na(Accidentalidad))
colSums(is.na(Accidentalidad)) #Detectamos el numero de NAs que presenta la tabla por variable 

#Sustituimos las NAs en las variables categoricas por "No Asignado"
Accidentalidad[is.na(Accidentalidad)] <- "No Asignado"


#Asignar los niveles de la variable "LESIVIDAD" siguiendo los niveles establecidos 
#por el ayuntamiento de Madrid 
#(https://datos.madrid.es/FWProjects/egob/Catalogo/Seguridad/Ficheros/Estructura_DS_Accidentes_trafico_desde_2019.pdf)
levels(Accidentalidad$LESIVIDAD)
levels(Accidentalidad$LESIVIDAD) <- c("Sin asistencia sanitaria", "Herido leve", 
                                      "Herido leve", "Herido grave", "Fallecido", 
                                      "Herido leve", "Herido leve", "Herido leve", 
                                      "Ileso", "Herido grave", "Herido leve", "Ileso",
                                      "Fallecido", "No asignado")
                                      
                                       

levels(Accidentalidad$LESIVIDAD)

#Asignar los niveles de la variable "TIPO ACCIDENTE"
str(Accidentalidad$`TIPO ACCIDENTE`)
levels(Accidentalidad$`TIPO ACCIDENTE`)
levels(Accidentalidad$`TIPO ACCIDENTE`) <- c("Alcance", "Atropello", "Atropello animal",
                                             "Atropello persona", "Caida", "Caida", 
                                             "Caida bicicleta", "Caida ciclomotor",
                                             "Caida motocicleta", "Caida vehiculo 3 ruedas", 
                                             "Caida viajero bus", "Choque con objeto fijo", 
                                             "Choque con objeto fijo", "Choque con objeto fijo",
                                             "Colision frontal", "Colision fronto-lateral",
                                             "Colision lateral","Colision multiple", 
                                             "Colision doble", "Colision frontal",
                                             "Colision fronto-lateral", "Colision lateral", 
                                             "Colision multiple", "Colision multiple", 
                                             "Despeñamiento", "Otras causas", "Otras causas",
                                             "Salida de via","Salida de via", "Vuelco", "Vuelco")

Accidentalidad %>% count(`TIPO ACCIDENTE`)

#Asignar los niveles de la variable "TIPO_VEHICULO"
str(Accidentalidad$TIPO_VEHICULO)
levels(Accidentalidad$TIPO_VEHICULO)
levels(Accidentalidad$TIPO_VEHICULO) <- c("No asignado", "ambulancia", "Ambulancia",
                                             "Auto-Taxi", "Autobus", "Autobus", 
                                             "Autobus", "Autobus-EMT", "Autocaravana",
                                             "Bicicleta", "Bicicleta", "Bicicleta EPAC", 
                                             "Camion", "Camion rigido", "Camion", 
                                             "Ciclomotor", "Ciclomotor", "ciclomotor",
                                             "Ciclomotor", "Ciclomotor 3 ruedas",
                                             "Cuadriciclo ligero", "Furgoneta", "Furgoneta",
                                             "Maquinaria agricola", "Maquinaria de obras",
                                             "Motocicleta 3 ruedas", "Motocicleta 3 ruedas",
                                             "Motocicleta", "Motocicleta", "Motocicleta", 
                                             "No asignado", "Otros vehiculos de motor", 
                                             "Patinete", "Remolque", "Semiremolque", 
                                             "No asignado", "Todo terreno", "Tractocamion",
                                             "Tren/metro", "Turismo", "Turismo", "Varios",
                                             "Vehiculo de 3 ruedas", "Vehiculo articulado",
                                             "VMU electrico")

Accidentalidad %>% count(TIPO_VEHICULO)

#Asignar los niveles de la variable "TIPO PERSONA"
str(Accidentalidad$`TIPO PERSONA`)
levels(Accidentalidad$`TIPO PERSONA`)
levels(Accidentalidad$`TIPO PERSONA`) <- c("Conductor", "Conductor", "Pasajero", 
                                           "Peaton", "Peaton", "Peaton", "Testigo",
                                           "Viajero")

Accidentalidad %>% count(`TIPO PERSONA`)

#Asignar los niveles de la variable "DISTRITO"
str(Accidentalidad$DISTRITO)
levels(Accidentalidad$DISTRITO)
levels(Accidentalidad$DISTRITO) <- c("Arganzuela", "Barajas", "Carabanchel", "Centro", 
                                     "Chamartin", "Chamartin", "Chamartin", "Chamberi", 
                                     "Chamberi", "Chamberi", "Ciudad lineal", 
                                     "Fuencarral-EL Pardo", "Hortaleza", "Latina",
                                     "Moncloa-Aravaca", "Moratalaz",
                                     "Puente de Vallecas", "Retiro", "Salamanca", 
                                     "San Blas", "San Blas","Tetuan", "Tetuan",
                                     "Tetuan", "Usera","Vicalvaro", "Vicalvaro",
                                     "Vicalvaro", "Villa de Vallecas","Villaverde")

Accidentalidad %>% count(DISTRITO)

#Asignar los niveles de la variable "RANGO_EDAD"
str(Accidentalidad$RANGO_EDAD)
levels(Accidentalidad$RANGO_EDAD)
levels(Accidentalidad$RANGO_EDAD) <- c("Desconocida", "DE 0 A 5 AÑOS", "DE 0 A 5 AÑOS",
                                       "DE 10 A 14 AÑOS", "DE 10 A 14 AÑOS", "DE 15 A 17 AÑOS",
                                       "DE 15 A 17 AÑOS", "DE 18 A 20 AÑOS", "DE 18 A 20 AÑOS",
                                       "DE 21 A 24 AÑOS", "DE 21 A 24 AÑOS", "DE 25 A 29 AÑOS",
                                       "DE 25 A 29 AÑOS", "DE 30 A 34 ANOS", "DE 30 A 34 ANOS",
                                       "DE 30 A 34 ANOS", "DE 35 A 39 AÑOS", "DE 35 A 39 AÑOS", 
                                       "DE 40 A 44 AÑOS", "DE 40 A 44 AÑOS", "DE 45 A 49 AÑOS",
                                       "DE 45 A 49 AÑOS", "DE 50 A 54 AÑOS", "DE 50 A 54 AÑOS", 
                                       "DE 55 A 59 AÑOS", "DE 55 A 59 AÑOS", " DE 6 A 9 AÑOS",
                                       " DE 6 A 9 AÑOS", "DE 60 A 64 AÑOS", "DE 60 A 64 AÑOS", 
                                       "DE 65 A 69 AÑOS", "DE 65 A 69 AÑOS", "DE 70 A 74 AÑOS", 
                                       "DE 70 A 74 AÑOS", "MAYOR DE 74 AÑOS", "Desconocida", 
                                       "Desconocida", "MAYOR DE 74 AÑOS", "MAYOR DE 74 AÑOS")

Accidentalidad %>% count(RANGO_EDAD)

#Analisis exploratorio de la tabla
summary(Accidentalidad)
str(Accidentalidad)


#Guardar la tabla generada
write.csv(Accidentalidad,
          file="Accidentalidad.csv",
          fileEncoding= "UTF-8")
