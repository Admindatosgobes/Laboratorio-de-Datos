if  (!requireNamespace("dplyr", quietly = TRUE)) {install.packages("shiny"))}
if  (!requireNamespace("dplyr", quietly = TRUE)) {install.packages("tidyverse")}
if  (!requireNamespace("dplyr", quietly = TRUE)) {install.packages("plotly")}
if  (!requireNamespace("dplyr", quietly = TRUE)) {install.packages("scatterD3")}

library(shiny)
library(tidyverse)
library(plotly)
library(scatterD3)


ui <- shinyServer(fluidPage(
  
  h1("Ejemplo de representación de datos en tiempo real con R y Shiny Apps"),
  p("Basado en el trabajo de https://github.com/cutterkom"),
  a(href = "https://github.com/cutterkom/r-shiny-realtime-streaming-data", "Para más información consultar la fuente original en Github."),
  p("Este ejemplo, muestra una aplicación para visualizar en tiempo real las plazas de aparcamiento libres disponibles en los aparcamientos del centro de la ciudad de Málaga"),
  p("Los datos originales proceden del catálogo de datos abiertos de datos.gob.es"),
  a(href = "https://datos.gob.es/catalogo/l01290672-ocupacion-aparcamientos-publicos-municipales", "Conjunto de datos original (distribución CSV)"),
  

  # h2("ggplot2 Library"),
  # plotOutput("plot"),
  
  h2("Plotly Library"),
  p("Colocando el cursor sobre la localización deseada se muestran el número de plazas libres"),
  p("El color indica de forma cualitativa la capacidad de aparcamientos totales de cada una de las ubicaciones"),
  plotlyOutput("plotly"),
  
  h2("Plotly Library"),
  p("Colocando el cursor sobre la localización deseada se muestran el número de plazas libres"),
  p("El color indica de forma cualitativa la capacidad de aparcamientos totales de cada una de las ubicaciones"),
  plotlyOutput("plotlymap"),
  
  # h2("D3"),
  # scatterD3Output("d3")
  
  ))


server <- shinyServer(function(input, output, session) {
  # helper: shut down Shiny session in RStudio, when you close the browser tab
  session$onSessionEnded(stopApp)
  
  # function to create a dataframe with column x as a random number and y as the current timestamp
  get_new_data <- function() {
    y = sample(10:70, 1) # draw a random number between 10 and 70
    x = as.POSIXct(Sys.time(), format = "%Y-%m-%d %H%m", origin = "1970-01-01")
    data.frame(x, y)
  }
  
  # initialise an empty dataframe as a reactiveValues object.
  # it is going to store all upcoming new data
  
  myurl <- "https://datosabiertos.malaga.eu/recursos/aparcamientos/ocupappublicosmun/ocupappublicosmun.csv"
  

  
  #values <- reactiveValues(df = data.frame(x = NA, y = NA))
  values <- reactiveValues(df = data)
  
  
  # call the function get_new_data() every two seconds
  # and bind the resulting dataframe to the reactiveValues dataframe
  observeEvent(reactiveTimer(60000)(), {
    # Trigger every 2 seconds
    values$df <- isolate({
      
      data <- read_csv(url(myurl))
      # get and bind the new data
      #rbind(values$df, get_new_data()) %>%
        #filter(!is.na(x)) # filter the first value to prevent a first point in the middle of the plot
    })
  })
  
    data <- head(data, 10)
    
    data$capacidad <- as.numeric(data$capacidad)
    data$logcapacidad <- log(data$capacidad)    

  # # create ggplot2 chart
  # output$plot <- renderPlot({
  #   #x_axis_start <-
  #     #as.POSIXct(min(values$df$x), format = "%Y-%m-%d", origin = "1970-01-01")
  #   #x_axis_end <-
  #     #as.POSIXct(min(values$df$x), format = "%Y-%m-%d", origin = "1970-01-01") + 200
  #   #y_axis_range <- c(0, 70)
  #   
  #   ggplot(data = values$df, aes(
  #     x = nombre,
  #     y = libres
  #   )) +
  #     geom_point() #+
  #     #expand_limits(x = c(x_axis_start, x_axis_end), y = y_axis_range)
  #   
  #   ggplot(data=data, aes(x=nombre, y=libres, fill=as.numeric(capacidad))) +
  #     geom_bar(colour="black", stat="identity") +
  #     guides(fill=FALSE)
  #   
  #   
  # })
  
  # create plotly chart
  output$plotly <- renderPlotly({
    #x_axis_start <-
      #as.POSIXct(min(values$df$x), format = "%Y-%m-%d", origin = "1970-01-01")
    #x_axis_end <-
      #as.POSIXct(min(values$df$x), format = "%Y-%m-%d", origin = "1970-01-01") + 200
    input$go_button # This makes the renderPlot depend on the go_button

    plot_ly(
      data = values$df,
      x = ~ nombre,
      y = ~ libres,
      color = ~ as.numeric(capacidad)) %>%
      add_bars() %>%
      layout(barmode = "stack")
      
  #layout(xaxis = list(
        #range =  c(x_axis_start, x_axis_end),
        #type = "date"
      #),
      #yaxis = list(range = c(0, 70)))

  })
  
  
  
  output$plotlymap <- renderPlotly({
    plot_mapbox(values$df) %>%
    add_markers(
      x = ~longitude, 
      y = ~latitude, 
      size = ~libres, 
      color = ~capacidad,
      colors = c("Black", "Grey","Blue","Red","Yellow","Green"),
      text = ~paste(nombre, libres),
      hoverinfo = "text"
    ) %>%
      layout(
        mapbox = list(
          center = list(lat = 36.7201748, lon = -4.42),
          zoom =13
        )
      )
  })
  
#   
#   # create D3 chart
#   output$d3 <- renderScatterD3({
#     scatterD3(
#       data = values$df,
#       x = x,
#       y = y,
#       xlim = c(min(values$df$x), min(values$df$x) + 200),
#       ylim = c(0, 70)
#     )
#   })
#   
})

shinyApp(ui = ui, server = server)
