# Pipeline ETL: Automatizado con Azure Data Factory (Ventas Zara) 🔁
#
#
## Descripción 📃

El presente proyecto simula un **Pipeline ETL automatizado** utilizando **Azure Data Factory (ADF)**. El proyecto se basa en procesar datos de ventas ficticias de Zara, desde archivos crudos en **Azure Blob Storage** hasta una zona limpia y lista para su posterior análisis.

Esto representa una situación común en empresas de retail, donde los datos de ventas se reciben diariamente en formatos tales como CSV, y deben ser procesados, transformados y almacenados para su posterior análisis.
#
## Herramientas utilizadas 🛠
#

| Herramienta | Propósito |
| ------ | ------ |
| `Azure Data Factory (ADF)` | Orquestación del pipeline y transformación de datos |
| `Azure Blob Storage` | Almacenamiento de datos en zonas _raw_ y _clean_ |
| `Python 3.13 (Pandas)` | Análisis exploratorio inicial del dataset |
| [Draw.io](https://www.drawio.com/) | Diseño del diagrama de arquitectura |

#
## Zonas en Azure Blob Storage 📁

- **Raw Zone**: Archivos CSV originales cargados manualmente.
- **Clean Zone**: Archivos procesados o limpios generados por el Pipeline en ADF.
#
## Flujo del Pipeline 🧵

1. 💻 Carga inicial del archivo `zara_sales_june.csv` a Azure Blob Storage.
2. 🧩 ADF ejecuta el flujo de datos, tomando como source `ds-raw-data` hacia el sick o receptor `ds-clean-data`.
3. 📏 El pipeline transforma y agrega una nueva columna derivada llamada `revenue` (ganancia).
4. 📦 Se guarda un nuevo archivo en `ds-clean-data` y posteriormente en `clean-zone`, (Azure Blob), ahora limpio y listo para su análisis.

##  Estructura del proyecto 📚
#
```## Estructura del Proyecto
➡ ETL-sales-pipeline-adf-zara
    * architecture/
        * ArchivosReadme.md
    * azure/
        * logs/
            - ResultadosDeEjecución.txt
    * data/
        * raw/
            - zara_sales_june.csv
        * clean/
    * documentation/
        * Documentación del proyecto
        * screenshots/
            - CapturasDePantalla.png
    * README.md
    * requirements.md
```

# Reflexión final 🤔

A través del proyecto, mi capacidad de entendimiento y anáisis del mundo automatizado de los Pipelines, aumentó en gran medida, aprendí a relizar una creación completa de un Pipeline ETL en Azure Data Factory, conociendo cada paso, cada conexión y lo más importante, el propósito general y de cada uno de ellos. Aprendi también la configuración básica de una cuenta de almacenamiento y sus contenedores con el servicio Azure Blob Storage, como también, la documentación clara de todo el proyecto. 

_Gracias por leer.._
#### _Autor: Esteban Parrado_
#
#
#
#
>“La tecnología no es nada. Lo importante es que tengas fe en la gente, que sean básicamente buenas e inteligentes, y si les das herramientas, harán cosas maravillosas con ellas”
>-Steve Jobs.
