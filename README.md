Proyecto_02_RefugioAnimal


La visualización mediante una aplicación interactiva utilizando Shiny en Python y el análisis de ciertos aspectos en la base de datos seleccionada se desarrolló entre los tres participantes de este grupo de trabajo. Para llevarlo a cabo, se requirió del aporte equitativo, y comunicación clara por parte de cada uno de los participantes, para completarlo de manera favorable. Las tareas realizadas en conjunto fueron la selección del dataset a utilizar y el desarrollo del código de la app de Shiny para Python, la presentación y el informe La visualización mediante una aplicación interactiva utilizando Shiny en Python y el análisis de ciertos aspectos en la base de datos seleccionada se desarrolló entre los tres participantes de este grupo de trabajo. Para llevarlo a cabo, se requirió del aporte equitativo, y comunicación clara por parte de cada uno de los participantes, para completarlo de manera favorable. Las tareas realizadas en conjunto fueron la selección del dataset a utilizar y el desarrollo del código de la app de Shiny para Python, la presentación y el informe.

Participantes:

Isabel Flores Rodríguez C32973

Keylor Gómez Jiménez C232380

Estefanía Núñez Jiménez C4H993


Desarrollo de la Aplicación Shiny en Python

La aplicación debe estar desarrollada utilizando Shiny para Python (documentación oficial).
Debe permitir la visualización y análisis interactivo del conjunto de datos seleccionado.

Requisitos técnicos mínimos:

Interfaz gráfica intuitiva y funcional.
Cuatro tipos de visualizaciones:

*Grafico de Dispersion

*Histograma

*Diagrama de caja

*Grafico de Pie

Opciones para filtrar o modificar los datos visualizados según parámetros definidos por el usuario.


Selección y Análisis del Conjunto de Datos

Del dataset (zip): Animal Shelter Analytics, se estara utilizando la base de datos (.csv): Austin_Animal_Center_Intakes.csv (https://www.kaggle.com/datasets/jackdaoud/animal-shelter-analytics?select=Austin_Animal_Center_Intakes.csv)

El autor, Jack Daoud, explicó el contexto de la base de datos que él se inspiró de conducir un EDA en los datos del refugio de animales, sacó los datos del portal público de la ciudad de Austin, Texas en el segmento del servicio de animales, el contenido del dataset contiene tres CSVs:

-Austin_Animal_Center_Intakes.csv 
-Austin_Animal_Center_Outcomes.csv 
-Austin_Animal_Center_Stray_Map.csv

Los ingresos son del Centro de Animales desde el 1 de octubre de 2013 hasta la fecha de publicación de los datos. Es reflejado el estado de los animales al llegar al centro, todos los animales reciben un identificador único al ingresar. Anualmente, más del 90 % de los animales que ingresan al centro son adoptados, transferidos a refugios o devueltos a sus dueños.

Sobre el Dataset:

-El conjunto de datos es de dominio público 
-Posee 124121 registros, sus variables son: "Animal ID", "DateTime", "MonthYear", y "Age upon Intake", variables categoricas: "Name", "Found Location", "Intake Type", "Intake Condition", "Animal Type", "Sex upon Intake", "Breed", "Color"
-Para la utilizacion satisfactoria de la aplicacion de visualizacion de Shiny para Python que desarrollamos modificamos el dataset, reduciendo los registros a 501, igualmente agrupando/generalizando las variables de Color,Breed_Group,Sex upon Intake,Intake Type,Location_Group. Otra de las modificaciones hechas a las variables fue convertir la variable de "Age_Days" a una variable estrictamente numérica, anteriormente describe la edad de los animales en semanas (ej: 1 week, 2 weeks, ..), lo modificamos para que en los registros ahora se muestra el número de la edad en días. 


Explicación y justificación:

Se escogió el dataset de “Austin Animal Center Intakes” porque contiene información real y actualizada (la última actualización fue hace 5 años) sobre los animales que ingresan al refugio de la ciudad de Austin, Texas. Este conjunto de datos es de interés ya que permite analizar patrones de ingreso de animales, sus condiciones de llegada, tipos, edades, sexo y raza. Como el dataset contiene variables categóricas y numéricas, su análisis abarca mayor diversidad en el ámbito estadístico.

(Contexto directo del autor, recuperado de la página de Kaggle)
Context:

I was reading Every Nose Counts: Using Metrics in Animal Shelters when I got inspired to conduct an EDA on animal shelter data. I looked online for data and found this dataset which is curated by Austin Animal Center (https://www.austintexas.gov/austin-animal-center). The data can be found on https://data.austintexas.gov.

This data can be utilized for EDA practice. So go ahead and help animal shelters with your EDA powers by completing this task!

Acknowledgement

Thank you Austin Animal Center for all the animal protection you provide to stray & owned animals. Also, thank you for making your data accessible to the public.


Definición de objetivos y preguntas: 

Objetivo 1: Identificar la distribución de las edades de los animales en relación con el índice de registro.

Pregunta 1: ¿Cómo se distribuyen las edades de los animales en función del índice de registro?

Grafico: Dispersion


Objetivo 2: Determinar qué tipo de animal ingresa con mayor frecuencia al centro.

Pregunta 2: ¿Qué tipo de animal ingresa más?

Grafico: Histograma


Objetivo 3: Encontrar el color que predomina sobre todos los animales del refugio.

Pregunta 3: ¿Qué color predomina en los animales?

Grafico: Pie


Objetivo 4: Reconocer el color que predomina sobre todos los animales del refugio.

Pregunta 4: ¿Cuál es la edad que predomina entre los animales al momento que los refugian?

Gráfico: Diagrama de caja 

Presentación del Análisis

La presentacion igualmente se puede visualizar en el enlance adjunto a continuacion: [ https://www.canva.com/design/DAG3sc1IhtU/EfIsOgtpYZ5qFFRkfb8SgQ/edit](https://www.canva.com/design/DAG3sc1IhtU/EfIsOgtpYZ5qFFRkfb8SgQ/edit?utm_content=DAG3sc1IhtU&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

Colaboración con Git:

El desarrollo debe realizarse en un repositorio GitHub: Proyecto_02_RefugioAnimal.

Todos los integrantes deben contribuir activamente, quedando reflejado en el historial de commits.

Ramas:

Keylor, Estefania e Isabel

Realización de commits descriptivos y frecuentes.
Ejecución de pull y push para sincronización de cambios.
Realización de merge de ramas secundarias con la rama principal (main).
Incluid capturas de pantalla o enlaces al historial del repositorio como evidencia en el informe final.

Entrega y Evaluación

Formato de entrega:

Código fuente de la aplicación en el repositorio Git.
Informe en PDF que incluya:
Descripción del grupo y roles.
Justificación y análisis del conjunto de datos.
Preguntas y objetivos planteados.
Capturas de la aplicación en funcionamiento.
Evidencia del uso de Git (capturas o enlaces).
Plazos:
La fecha límite de entrega será comunicada por el docente y respetará el formato 23/11/2025. 11.Criterios de evaluación:
Descripción del proyecto:


El informe puede ser accedido igualmente mediante el siguiente enlance: https://docs.google.com/document/d/1g1GkrBCVKcJCNFncS1JUe5SO4SKsUxV4XC4eIaKN2e8/edit?usp=sharing


<img width="796" height="426" alt="image" src="https://github.com/user-attachments/assets/0d6eca4e-c6b1-4a7d-ae21-f5e90f22001a" />
<img width="799" height="420" alt="image" src="https://github.com/user-attachments/assets/16cf6be8-ae90-4327-b704-98a15879ac40" />
<img width="794" height="529" alt="image" src="https://github.com/user-attachments/assets/1180455b-e242-4cda-af0f-be2866f4aedc" />

Observaciones Finales:

El éxito del proyecto depende tanto de la calidad técnica como de la colaboración entre los miembros del grupo. Entregar el proyecto final del repositorio de Git en un archivo .zip con los carnés de los estudiantes involucrados. Para cualquier duda, consultar con el docente o revisar los recursos oficiales de Shiny y Git.
