# Laboratorio de Datos

## [El Valor de los datos en tiempo real](https://datos.gob.es/es/blog/el-valor-de-los-datos-en-tiempo-real)

_Post elaborado por **Alejandro Alija**, experto en **Transformación Digital e Innovación**._

### Ejemplo de representación de datos en tiempo real con R y Shiny Apps

Para este ejemplo práctico, se ha utilizado un conjunto de datos abiertos del catálogo de [datos.gob.es](https://datos.gob.es/), en particular, [un conjunto de datos que contiene información sobre la ocupación de plazas de aparcamientos públicos en el centro de la ciudad de Málaga](https://datos.gob.es/catalogo/l01290672-ocupacion-aparcamientos-publicos-municipales). Los datos son accesibles a través de [este API](https://datosabiertos.malaga.eu/api/1/util/snippet/api_info.html?datastore_root_url=https%3A%2F%2Fdatosabiertos.malaga.eu%2Fapi%2Faction&resource_id=0dcf7abd-26b4-42c8-af19-4992f1ee60c6). En la descripción del conjunto de datos se indica que la actualización es cada 2 minutos.

A partir del conjunto de datos se ha construido una [app interactiva](http://apps.katharinabrunner.de/r-shiny-realtime-streaming-data/) donde el usuario puede observar en tiempo real el nivel de ocupación mediante unas visualizaciones gráficas.

El lector también tiene a su disposición el código de ejemplo para reproducirlo en cualquier momento.

Los pasos básicos de este código se detalla a continuación:

Tiene dos componentes:

1. Generar un punto de datos cada dos segundos

2. Trazar los datos con tres paquetes: [ggplot2](https://ggplot2.tidyverse.org/), [plotly](https://plot.ly/) y [scatterD3](https://juba.github.io/scatterD3/).

#### 1) Generación de nuevos datos

Primero, inicializamos un marco de datos vacío como un [objeto ``reactiveValues``](https://shiny.rstudio.com/articles/reactivity-overview.html), que recibirá y almacenada los nuevos puntos de datos.

```

# initialize an empty dataframe as a reactiveValues object.

# it is going to store all upcoming new data

values <- reactiveValues(df = data.frame(x = NA, y = NA))

```

Seguidamente, los datos aleatorios se guardaran como ``reactive values`` en un dataframe. La variable valores$df se completará de forma incremental cada dos segundo utilizando [observeEvent()](https://shiny.rstudio.com/reference/shiny/1.0.0/observeEvent.html):

```

observeEvent(reactiveTimer(2000)(),{ # Trigger every 2 seconds

values$df <- isolate({

# get and bind the new data

values_df <- rbind(values$df, get_new_data()) %>% filter(!is.na(x))

})

})

```

#### 2) Graficar los datos

Después de recibir nuevos datos en el marco de datos de valores reactivos, la aplicación traza los datos con tres paquetes.

El ejemplo de ggplot2:

```

# create ggplot2 chart

output$plot <- renderPlot({

x_axis_start <- as.POSIXct(min(values$df$x), format = "%Y-%m-%d", origin="1970-01-01")

x_axis_end <- as.POSIXct(min(values$df$x), format = "%Y-%m-%d", origin="1970-01-01") + 1000

y_axis_range <- c(0, 70)

values$df %>%

ggplot(aes(x = as.POSIXct(x, format = "%Y-%m-%d", origin="1970-01-01"), y = y)) +

geom_point() +

expand_limits(x = c(x_axis_start, x_axis_end), y = y_axis_range)

})

```

_Nota: El código publicado pretende ser una guía para el lector, pero puede requerir de dependencias externas o configuraciones específicas para cada usuario que desee ejecutarlo.​_

