#"Guía práctica de introducción al Análisis Exploratorio de Datos"#

# Pasos que se seguiran en este codigo
# 1. Carga de librerias. 
# 2. Carga de datos. 
# 3. Analisis descriptivo.
# 4. Ajuste de tipos de variables.
# 5. Deteccion y tratamiento de datos ausentes.
# 6. Deteccion y tratamiento de valores atipicos. 
# 7. Analisis de correlacion entre variables.  



#Pre-requisitos 
#Antes de empezar a trabajar con los datos debemos fijar el directorio de trabajo.   

setwd("C:\Users\proyecto\Iniciativa_Aporta\EDA")


#1. Carga de librerias

#Instalacion de librerias
if  (!requireNamespace("readr", quietly = TRUE)) {install.packages("readr")}
if  (!requireNamespace("ggplot2", quietly = TRUE)) {install.packages("ggplot2")}
if  (!requireNamespace("Hmisc", quietly = TRUE)) {install.packages("Hmisc")}
if  (!requireNamespace("corrplot", quietly = TRUE)) {install.packages("corrplot")}
if  (!requireNamespace("plyr", quietly = TRUE)) {install.packages("corrplot")}

#Carga de librerias

library(readr)
library(ggplot2)
library(Hmisc)
library(corrplot)
library(plyr)



#2. Carga de datos 
# Cargamos todos los conjuntos de datos que nos interesen en nuestro entorno de 
# desarrollo.

calidad_aire<- 
  read_delim("https://datosabiertos.jcyl.es/web/jcyl/risp/es/medio-ambiente/calidad_aire_historico/1284212629698.csv",
             delim=";", col_names = TRUE, locale = locale(encoding = "WINDOWS-1252"))

View(calidad_aire)

#3. Analisis exploratorio

str(calidad_aire)

summary(calidad_aire)

describe(calidad_aire)

#Generamos el histograma de dos variables para observar la distribucion de sus datos

#Antes de realizar cualquier analisis cambiamos el nombre a la variable 

calidad_aire <- rename(calidad_aire, c( `O3 (ug/m3)`= "O3" ))
calidad_aire <- rename(calidad_aire, c( `PM10 (ug/m3)`= "PM10" ))
calidad_aire <- rename(calidad_aire, c( `PM25 (ug/m3)`= "PM25" ))
calidad_aire <- rename(calidad_aire, c( `CO (mg/m3)`= "CO" ))
calidad_aire <- rename(calidad_aire, c( `NO (ug/m3)`= "NO" ))
calidad_aire <- rename(calidad_aire, c( `NO2 (ug/m3)`= "NO2" ))
calidad_aire <- rename(calidad_aire, c( `SO2 (ug/m3)`= "SO2" ))

#Realizamos los histogramas

par(mfrow=c(1,2))

hist_O3 <- hist(calidad_aire$O3, main = "", 
                   xlab = "O3 (ug/m3)", ylab = "Frecuencia", 
                   breaks = 1000, xlim = c(0,150))

hist_PM10 <- hist(calidad_aire$PM10, main = "", 
                 xlab = "PM10 (ug/m3)", ylab = "Frecuencia", 
                 breaks = 1000, xlim = c(0,150))

#4. Ajuste de tipos de variables

#Exploracion del dataset
str(calidad_aire)

#Encontramos tres variables a las cuales debemos re-ajustar el tipo (Fecha, 
#Provincia y Estacion) para que puedan ser tratadas de manera correcta en 
#posteriores analisis.

#Re-ajustar la variable Fecha
calidad_aire$Fecha <- as.Date(calidad_aire$Fecha, format("%d/%m/%Y"))
str(calidad_aire$Fecha)

#Re-ajustar la variable Provincia
unique(calidad_aire$Provincia)
calidad_aire$Provincia <- as.factor(calidad_aire$Provincia)
levels(calidad_aire$Provincia)

#Re-ajustar la varaible Estacion
unique(calidad_aire$Estacion)
calidad_aire$Estacion <- as.factor(calidad_aire$Estacion)
levels(calidad_aire$Estacion)


#5. Deteccion y tratamiento de valores perdidos

#Deteccion de NAs en la tabla de datos

#a. Deteccion de valores perdidos en toda la tabla de datos.

#Este comando devuelve un resultado booleano por cada observacion que presenta la tabla de datos:
   #TRUE, en caso de que la observacion sea un valor perdido;
   #FALSE, en caso de que el valor sea perdido
is.na(calidad_aire) 


#Este comando te devuelve un resultado booleano (TRUE o FALSE) para toda la tabla de datos. 
   #El valor TRUE indica la presencia de datos perdidos en la tabla. 
   #El valor FALSE, indica que no existen valores perdidos en la tabla.
any(is.na(calidad_aire)) 

#Muestra la suma de todos los valores perdidos que presenta la tabla.
sum(is.na(calidad_aire)) 

#Muestra el porcentaje de valores perdidos que presenta la tabla
mean(is.na(calidad_aire)) 


#Muestra el numero de valores perdidos que presenta cada variable de la tabla
colSums(is.na(calidad_aire)) 

#Muestra el porcentaje de valores perdidos que presenta cada variable de la tabla
colMeans(is.na(calidad_aire), round(2)) 


#b. Eliminacion de los valores perdidos 

#Eliminacion de las variables que presentan un porcentaje superior al 50% de valores perdidos
calidad_aire_SV <- calidad_aire[,-which(colMeans(is.na(calidad_aire)) >= 0.50)]

colMeans(is.na(calidad_aire_SV), round(2))


#Sustitucion de NAs por la media de la variable a la cual pertenece

columnas_numericas <- which(sapply(calidad_aire, is.numeric))

cols_mean <- rep(NA, ncol(calidad_aire))
cols_mean[columnas_numericas] <- 
  colMeans(calidad_aire[, columnas_numericas], na.rm = TRUE)

calidad_aire_SinNA <- 
for (x in columnas_numericas) {
  calidad_aire[is.na(calidad_aire[,x]), x] <- round(cols_mean[x],2)
}

sum(is.na(calidad_aire))


#6. Deteccion y tratamiento de valores atipicos (outliers)


#a. Deteccion y tratamiento de datos atipicos en una Variable continua 
#(Variable "NO2 (ug/m3)", pero es el mismo proceso para cualquier
#variable continua que presente la tabla de datos)

#Deteccion de valores atipicos en una variable continua

#Creacion del histograma de frecuencias

par(mfrow=c(1,1))
histograma <- hist(calidad_aire$O3, main = "", 
                   xlab = "O3", ylab = "Frecuencia", 
                   breaks = 1000, xlim = c(0,150))
histograma

#Obtencion de las estadisticas del boxplot y creacion del boxplot

outliers <- boxplot(calidad_aire$O3, horizontal = TRUE, xlab ="O3 (ug/m3)")
outliers 

boxplot.stats(calidad_aire$O3)


# Eliminacion de los valores atipicos de una variable continua

calidad_aire_NoOut <- calidad_aire[!(calidad_aire$O3 %in% outliers$out), ]
boxplot(calidad_aire_NoOut$O3, horizontal = TRUE, xlab ="O3 (ug/m3)")
str(calidad_aire_NoOut)


# Comparativa entre ambas tablas (con outliers y sin outliers)
# Creacion del boxplot con la nueva tabla 

par(mfrow=c(1,2))  #Dividir el cuadro del grafico en dos 
boxplot(calidad_aire$O3, xlab ="03 (ug/m3)") #Creacion del boxplot 
#con la tabla con outliers
boxplot(calidad_aire_NoOut$O3, xlab ="O3 (ug/m3)") #Creacion del boxplot con
#la tabla sin outliers


#b. Deteccion de valores atipicos en una variable categorica (Variable "Provincia", 
#pero es el mismo proceso para cualquier variable continua que presenta la tabla de datos)

#Deteccion de valores atipicos en una variable categorica

#Contamos el numero de observaciones que tiene cada categoria de la variable

count(calidad_aire, "Provincia")

#Generamos el grafico de barras para ver la distribucion que presenta la variable
par(mfrow=c(1,1))
ggplot_provincias <- ggplot(calidad_aire) + 
  geom_bar(mapping = aes(x = Provincia, fill=Provincia))+ 
  xlab("Provincias")+
  ylab("Nº observaciones")+
  theme(axis.text.x = element_text(angle = 30))
ggplot_provincias


# Eliminacion de los valores atipicos de una variable categorica

eliminar_Madrid <- calidad_aire$Provincia %in% c("Madrid")
calidad_aire_SM <- calidad_aire[!eliminar_Madrid,]
count(calidad_aire_SM, "Provincia")
calidad_aire_SM$Provincia <- droplevels(calidad_aire_SM$Provincia)
levels(calidad_aire_SM$Provincia)

#Generamos el grafico de barras de nuevo para ver de nuevo los niveles del factor

ggplot_provincias_SM <- ggplot(calidad_aire_SM) + 
  geom_bar(mapping = aes(x = Provincia, fill=Provincia))+ 
  xlab("Provincias")+
  ylab("Nº observaciones")+
  theme(axis.text.x = element_text(angle = 30))
ggplot_provincias_SM


#7. Analisis de correlaciones

#Seleccion de las variables numericas
num_variables <- calidad_aire[,c(2,3,4,5,6,7,8)]

#Creacion de la Matriz de correlaciones de las variables numericas
correlation <- cor(num_variables)
correlation



#Creacion del Grafico de matriz de correlaciones 
par(mfrow=c(1,1))
corrplot(correlation, method = "square")



