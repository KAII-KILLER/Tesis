# Cargamos la biblioteca necesaria
library(rpart)
library(caret) #para dividir los datos

data_pacientes <- read.csv("/home/leonardo/Documents/Tesis/pacientes_clean2.csv")

# Dividir los datos en un conjunto de entrenamiento y un conjunto de prueba
set.seed(1234) # Para reproducibilidad
indices <- createDataPartition(data_pacientes$diagnostico, p = 0.8, list = FALSE)
datos_entrenamiento <- data_pacientes[indices,]
datos_prueba <- data_pacientes[-indices,]

# Entrenamos el árbol de decisión
modelo_arbol <- rpart(diagnostico ~ acido_folico + toxoplasmosis + rubeola_citomegalovirus + herpes_simple + VIH + sangrado +
                        amenaza_parto_prematuro + vomito_embarazo + medicacion_embarazo + infecciones + hipertension_arterial + 
                        diabetes_gestacional + preeclampsia + requiere_reanimacion + ictericia + hipoglicemia + oxigenoterapia + 
                        hospitalizacion + seno_materno_exclusivo + apgar1 + apgar5 + parto_prematuro + abortos_previos + bajo_peso,
                      data = datos_entrenamiento, 
                      control = rpart.control(minsplit = 2)) 

# Hacemos predicciones en el conjunto de prueba
predicciones_arbol <- predict(modelo_arbol, datos_prueba, type = "class")

# Evaluamos el rendimiento
matriz_confusion <- confusionMatrix(predicciones_arbol, datos_prueba$diagnostico)
print(matriz_confusion)
