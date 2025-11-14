Proyecto_02_RefugioAnimal


Introduccion:

El presente proyecto tiene como objetivo que los estudiantes desarrollen una aplicación interactiva utilizando Shiny en Python, trabajen de forma colaborativa en grupos establecidos y empleen buenas prácticas de colaboración mediante el uso de Git. Además, deberán seleccionar y analizar un conjunto de datos relevante, justificar su elección y presentar los resultados a través de la aplicación. La colaboración efectiva y la documentación clara serán aspectos fundamentales para la evaluación final.


Participantes:

Isabel Flores Rodríguez C32973

Keylor Gómez Jiménez C232380

Estefanía Núñez Jiménez C4H993


Desarrollo de la Aplicación Shiny en Python

La aplicación debe estar desarrollada utilizando Shiny para Python (documentación oficial).
Debe permitir la visualización y análisis interactivo del conjunto de datos seleccionado.

Requisitos técnicos mínimos:

Interfaz gráfica intuitiva y funcional.
Al menos tres tipos de visualizaciones (por ejemplo, gráficos de barras y mapas de calor).
Opciones para filtrar o modificar los datos visualizados según parámetros definidos por el usuario.
Código bien estructurado, comentado y siguiendo buenas prácticas de programación.
Selección y Análisis del Conjunto de Datos

Del dataset (zip): Animal Shelter Analytics, se estara utilizando la base de datos (.csv): Austin_Animal_Center_Intakes.csv (https://www.kaggle.com/datasets/jackdaoud/animal-shelter-analytics?select=Austin_Animal_Center_Intakes.csv)
El conjunto de datos es publico ya que fue recuperado del sitio web "Kaggle".
Posee 124121 registros, sus variables son: "Animal ID", "DateTime", "MonthYear", y "Age upon Intake", variables categoricas: "Name", "Found Location", "Intake Type", "Intake Condition", "Animal Type", "Sex upon Intake", "Breed", "Color"

Explicación y justificación:

Se escogió el dataset de “Austin Animal Center Intakes” porque contiene información real y actualizada (la ultima actualizacion fue hace 5 años) sobre los animales que ingresan al refugio de la ciudad de Austin, Texas. Este conjunto de datos es de interés ya que permite analizar patrones de ingreso de animales, sus condiciones de llegada, tipos, edades, sexo y raza. Como el dataset contiene variables categoricas y numericas, su analisis abarca mayor diversidad en el ambito estadistico.

Sobre el Dataset:

El texto a continuacion fue recuperado desde la pagina de Kaggle, donde el autor del Dataset explico su contexto de la base de datos:

Context:

I was reading Every Nose Counts: Using Metrics in Animal Shelters when I got inspired to conduct an EDA on animal shelter data. I looked online for data and found this dataset which is curated by Austin Animal Center (https://www.austintexas.gov/austin-animal-center). The data can be found on https://data.austintexas.gov.

This data can be utilized for EDA practice. So go ahead and help animal shelters with your EDA powers by completing this task!

Content The data set contains three CSVs:

Austin_Animal_Center_Intakes.csv Austin_Animal_Center_Outcomes.csv Austin_Animal_Center_Stray_Map.csv

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

Grafico: Diagrama de caja 

Presentación del Análisis

La presentacion igualmente se puede visualizar en el siguiente enlance adjunto a continuacion: [ https://www.canva.com/design/DAG3sc1IhtU/EfIsOgtpYZ5qFFRkfb8SgQ/edit](https://www.canva.com/design/DAG3sc1IhtU/EfIsOgtpYZ5qFFRkfb8SgQ/edit?utm_content=DAG3sc1IhtU&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

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
