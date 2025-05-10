# Conurma

Este proyecto consiste en la creación de un aplicación para la subida de archivos, creación automática de una base de datos SQL con ellos y la posibilidad de edición de dichas tablas. El primer proceso es la carga y limpieza de los datos que vienen de archivos Excel, a continuación se suben los datos a SQL. Una vez creada la base de datos, se crea un backend para poder consumir y actualizar dicha base de datos desde un frontend.


## Tablas
Las tablas que se crean en la base de datos SQL son las siguientes:

1. **Asig. Inic. PIR6**: Esta tabla es la Asignación Inicial de PIR6. Su nombre en la base de datos es `asig_inic_pir6`. Sus columnas son las siguientes:
```python
columnas = ['ID', 'Municipio', 'Asignación Inicial PIR 6',
            'Asignación Inicial + Cofinanciación AYTO', '%\nGastos Corrientes',
            'Total\nGastos Corrientes', 'Gasto corriente ejecutado',
            'Inversión\nCAM', '% Inversión\nCAM', 'Inversión Ayuntamiento',
            '% Inversión Ayuntamiento', 'Total CAM+AYTO', 'Gestor',
            'TOTAL ALTAS', 'Aportación Ayto EXTRA', 'SALDO USADO',
            'SALDO RESTANTE ACTUACIONES   PIR 6', '% SALDO  ACTUACIONES PIR 6',
            'IMPORTE TOTAL COMPROMETIDO\n(ALTAS + REGISTRADAS)',
            'APORTACIÓN CM EXTRA FONDO DE RESERVA',
            'COFINANCIACIÓN EXTRA AYTO  PARA FR',
            'IMPORTE GLOBAL CONSUMIDO ACT + GC',
            'SALDO GLOBAL PIR (ACTUACIONES + GASTO CORRIENTE)',
            'Fecha Fichero', 'Status']
```

2. **Categorias**: Esta tabla es una relación de categorias. Su nombre en la base de datos es `categorias`. Sus columnas son las siguientes:
```python
columnas = ['ID','ORDEN', 'CATEGORÍAS', 'INCIDENCIA', 'GESTORES']
```

3. **Categorizacion**: Esta tabla es una relación de categorias y estados. Su nombre en la base de datos es `categorizacion`. Sus columnas son las siguientes:
```python
columnas = ['ID','ORDEN', 'CATEGORÍAS', 'ESTADOS DGIDL']
```

4. **Codigos de estado**: Esta tabla es una relación de estados con su descripción. Su nombre en la base de datos es `codigos_estado`. Sus columnas son las siguientes:
```python
columnas = ['ID','ORDEN', 'ESTADO GENERAL', 'ESTADO CONCRETO', 'DESCRIPCION',
            'ESTADO RESUMIDO', 'Column6', 'FASE', 'Column8', 'DG']
``` 

5. **Datos Municipales**: Esta tabla son los datos propios de cada municipio. Su nombre en la base de datos es `datos_municipales`.  Sus columnas son las siguientes:
```python
columnas = ['ID','Municipio', 'Sector', 'Comarca', 'Habitantes (01-enero-2021)',
            'Latitud', 'Longitud', 'ABC', 'ALCALDE', 'PARTIDO POLÍTICO','URL MUNICIPIO', 'IDs']
```

6. **Municipios**: Esta tabla son los datos propios de cada municipio junto con el número de expedientes. Su nombre en la base de datos es `municipios`.  Sus columnas son las siguientes:
```python
columnas = ['ID','Municipio', 'Sector', 'Comarca', 'Habitantes (01-enero-2021)',
            'Latitud', 'Longitud', 'ABC', 'ALCALDE', 'PARTIDO POLÍTICO',
            'URL MUNICIPIO', 'IDs', 'Nº Expedientes', 'Nº Expedientes PRISMA',
            'Nº Expedientes PIR 5', 'Nº Expedientes PIR 6']
```

7. **Hoja Final**: Esta tiene los datos de todas las actuaciones realizadas.  Su nombre en la base de datos es `hoja_final`. Sus columnas son las siguientes:
```python
columnas = ['ID', 'NUEVA MM/AA', 'Municipio', 'Sector', 'PROGRAMA', 'Gestión', 'Denominación actuación',
            'NºRegistro', 'Fecha entrada', 'Fecha RES ALTA', 'Fecha Resolución Modificación Alta',
            'Incremento o minoración de importe modificado', 'F.Inf.Tec.Alta', 'Fecha aportación proyecto AYTO',
            'Fecha informe comprobación documental', 'Fecha OK PROY Res autorizacion contratacion', 'Fecha INIC. EXP. LICIT.',
            'Fecha FIRMA CONTRATO', 'Fecha ACTA INICIO OBRA', 'Fecha ACTA RECEPCIÓN',
            'Fecha COMUNICACION FIN DE OBRA', 'Fecha ACTA CMG', 'Aporta Proyecto Alta', 'C.Menor Art. 13',
            'ÁREA TECNICA', 'Situación APP (MES ANTERIOR)', 'Situación APP (ACTUAL)',
            'COINCIDE Sit Actual-Previa', 'Importe ALTA', 'Importe CM', '% Financiación CM', 'Importe Ayto',
            '% Financiación Ayto', 'Aportación Ayto EXTRA', 'Importe OBRA', 'Importe Redacción Proyecto',
            'Importe Dirección Obra', 'Importe CSS', 'Importe Otros GA', 'O/S', 'TRAGSA / TRAGSATEC',
            'CONTRATO TRAGSATEC', 'TIPO ENCARGO TRAGSATEC', 'FECHA INICIO ENCARGO TRAGSATEC',
            'FECHA FIN ENCARGO TRAGSATEC', 'PLAZO TRAGSATEC', 'IMPORTE ENCARGO TRAGSATEC', 'CONTRATO TRAGSA',
            'TIPO ENCARGO TRAGSA', 'FECHA INICIO ENCARGO TRAGSA', 'PLAZO ENCARGO TRAGSA',
            'IMPORTE ENCARGO TRAGSA', 'OBSERVACIÓN APP CONURMA', 'Fecha INFO (llamada/app)', 'LLAMADA CONURMA',
            'Fecha visita', 'PROYECTISTA', 'EMPLAZAMIENTO', 'DESCRIPCIÓN PROYECTO', 'INFOGRAFÍA PROYECTO',
            'Fecha Adjudicación Obra', 'Plazo', 'Contratista', '% Ejecución estimado', 'FASE',
            'ESTADO TRAS COMPROBACIÓN CONURMA', 'ESTADO NUEVO CÓDIGO', 'SUBESTADO', 'FECHA CAMBIO ESTADO',
            'ACTIVO / INACTIVO', 'ALERTA ALTA', 'ALERTA PROYECTO', 'ALERTA LICITACIÓN', 'ALERTA OBRA',
            'ALERTA CMG', 'INCIDENCIA', 'CARTEL', 'OBSERVACIÓN (PWBI)', 'URL', 'CATEGORIZACIÓN',
            'ESTADO RESUMIDO', 'ENLACE CMG', 'FECHA  ACTA REPLANTEO PREVIO', 'Estado Obra', 
            'Fecha Final\nObra Objetivo', 'FONDO DE RESERVA', 'DESTINO FR', 
            
            'Incluida en AMS', 'Lote', 'Servicio', 'Empresa adjudicataria L 1-4',
            'Importe adjudicado L 1-4', 'Fecha inicio RP', 'Fecha fin RP',
            'Fecha inicio DF-CSYS', 'Fecha fin DF-CSYS', 'Lote 5',
            'Servicio lote 5', 'Empresa adjudicataria L 5', 'Importe adjudicado L 5', 
            'Incluida en AMO', 'Lote 1/2/3/4/5/6', 'Adjudicatario', 
            'Importe obra adjudicado', 'Baja ofertada', 'Fecha inicio obra', 
            'Fecha fin obra', '% Control calidad ofertado sobre PEM',
            'Importe destinado a Control de Calidad', 'Laboratorio Control de calidad',
            'Plazo de garantía obra (incluyendo la mejora ofertada)',
            
            'Fecha Fichero', 
            
            'Expediente traspaso Min Cred', 'importe Remanente UTILIZADO', 'Notas Director General',

            'Status']
```

8. **Doc Elaborada**: Esta tiene los datos de la documentacion elaborada.  Su nombre en la base de datos es `doc_aportada_pir6`. Sus columnas son las siguientes:
```python
columnas = ['ID', 'Expediente', 'Ref. documento', 'Documento', 'Anexo de', 
             'Plantilla', 'Estado', 'Fecha creación', 'Creado por', 
             'Fecha firma-rechazo', 'Fecha envío a otra unidad']
```

9. **Doc Aportada**: Esta tiene los datos de la documentacion aportada.  Su nombre en la base de datos es `doc_elaborada_pir6`. Sus columnas son las siguientes:
```python
columnas = ['ID', 'Expediente', 'Referencia', 'Asunto', 'Fecha entrada']
```

10. **Doc Requerida Aportada**: Esta tiene los datos de la documentacion requerida.  Su nombre en la base de datos es `doc_req_apor_pir6`. Sus columnas son las siguientes:
```python
columnas = ['ID', 'Expediente', 'Documento requerido', 'Ref. Aportación',
            'Fecha de aportación', 'Consulta autorizada', 'Observaciones']
```


## Estructura de carpetas

```plaintext
📦 Conurma
├── 📁 chatbot                       # Código Text-to-SQL 
│   ├── 📄 __init__.py               # Convierte un directorio en un paquete
│   ├── 📄 chatclass.py              # Clase del agente chatbot 
│   ├── 📄 prompts.py                # Prompts del sistema
│   ├── 📄 user_manager.py           # Clase para memoria del usuario
│
├── 📁 data_carga_inicial            # Carpeta de archivos de Excel para carga inicial
│   └── 📄 README.md                 # Detalles de datos 
│
├── 📁 db                            # Código para conexión SQL
│   ├── 📄 __init__.py               # Convierte un directorio en un paquete
│   ├── 📄 asig_inic_pir6.py         # Clase de la tabla Asig Inic PIR6
│   ├── 📄 categorias.py             # Clase de la tabla Categorias
│   ├── 📄 categorizacion.py         # Clase de la tabla Categorizacion
│   ├── 📄 codigos_estado.py         # Clase de la tabla Codigos de Estado
│   ├── 📄 connection.py             # Codigo conexión SQL
│   ├── 📄 contables_pir5.py         # Clase de la tabla Datos Contables PIR5
│   ├── 📄 datos_municipales.py      # Clase de la tabla Datos Municipales
│   ├── 📄 doc_aportada_pir6.py      # Clase de la tabla Documentacion PIR6
│   ├── 📄 doc_elaborada_pir6.py     # Clase de la tabla Documentacion PIR6
│   ├── 📄 doc_req_apor_pir6.py      # Clase de la tabla Documentacion PIR6
│   ├── 📄 gastos_pir6.py            # Clase de la tabla Documentacion PIR6
│   ├── 📄 hitos_pir6.py             # Clase de la tabla Documentacion PIR6
│   ├── 📄 hoja_final.py             # Clase de la tabla Hoja Final
│   ├── 📄 insert_update.py          # Función de inserción y actualización en DB
│   ├── 📄 municipios.py             # Clase de la tabla Municipios
│   ├── 📄 notificaciones_pir6.py    # Clase de la tabla Documentacion PIR6
│   ├── 📄 pagos_pir6.py             # Clase de la tabla Pagos PIR6
│   └── 📄 select.py                 # Función para selección desde DB
│
├── 📁 tmp_example                   # Carpeta con los ejemplos de archivos de subida
│   └── 📄 README.md                 # Detalles de datos 
│
├── 📁 tools                         # Herramientas 
│   ├── 📄 __init__.py               # Convierte un directorio en un paquete
│   └── 📄 tools.py                  # Herramientas (logger)
│
├── 📁 transformation                # Codigo de transformacion del dato
│   ├── 📄 __init__.py               # Convierte un directorio en un paquete
│   ├── 📄 actuaciones_pir5.py       # Transformacion tabla actuaciones PIR5
│   ├── 📄 actuaciones_pir6.py       # Transformacion tabla actuaciones PIR6
│   ├── 📄 asig_inic_pir6.py         # Transformacion tabla Asif Inic PIR6
│   ├── 📄 contables_pir5.py         # Transformacion Datos Contables PIR5
│   ├── 📄 datos_municipales.py      # Transformacion Datos Municipales
│   ├── 📄 doc_aportada_pir6.py      # Transformacion Documentacion PIR6
│   ├── 📄 doc_elaborada_pir6.py     # Transformacion Documentacion PIR6
│   ├── 📄 doc_req_apor_pir6.py      # Transformacion Documentacion PIR6
│   ├── 📄 gastos_pir6.py            # Transformacion Documentacion PIR6
│   ├── 📄 hitos_pir6.py             # Transformacion Documentacion PIR6
│   ├── 📄 municipios.py             # Transformacion tabla Municipios
│   ├── 📄 nombres_municipios.py     # Diccionario para poner tildes a los municipios
│   ├── 📄 notificaciones_pir6.py    # Transformacion Documentacion PIR6
│   └── 📄 pagos_pir6.py             # Transformacion tabla Pagos PIR6
│
├── 📄 .env.template                 # Plantilla de archivo .env 
├── 📄 .gitignore                    # Archivos y carpetas a ignorar en Git
├── 📄 .python-version               # Versión de python
├── 📄 create_db.py                  # Archivo para subida inicial de datos a SQL
├── 📄 Dockerfile                    # Dependencias y configuración 
├── 📄 main.py                       # Archivo principal con los endpoints para la aplicación
├── 📄 pyproject.toml                # Dependencias y configuración 
├── 📄 README.md                     # Documentación principal del proyecto
├── 📄 README_español.md             # Documentación principal del proyecto (en español)
├── 📄 requirements.txt              # Dependencias y configuración 
├── 📄 uv.lock                       # Dependencias y configuración 


```


## Dependencias

1. **Instalación `uv`**:

   El método de instalación recomendado de `uv` es:

   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

   De manera alternativa, podemos instalar `uv` via `pip`:

   ```bash
   pip install uv
   ```

   Para más detalles, revisar los [métodos de instalación](https://docs.astral.sh/uv/getting-started/installation/#installation-methods).



2. **Activación del entorno virtual**

    Activar el entorno virtual usado el siguiente comando:

    ```bash
    source .venv/bin/activate
    ```

3. **Sincronizar dependencias con uv**:

    ```bash
    uv sync
    ```

    Este comando instala las dependencias definidas en el archivo `pyproject.toml` con las misma versiones especificadas en el archivo `uv.lock`.

4. **Sincronizar dependencias con pip**:

    ```bash
    pip install -r requirements.txt
    ```

    Este comando instala las dependencias en el entorno virtual definidas en el archivo `requirements.txt`. También puede usarse el archivo `Dockerfile` para instalar de esta manera en el servidor de la aplicación.

## Variables de entorno

Este proyecto necesita de una base de datos SQL (MySQL, PostGres, SQLServer). La URI debe estar escrita en el archivo `.env`. En la platilla de archivo `.env.template` existe un ejemplo de URI y CHAT_URI para MySQL. Se recomienda usar un usuario distinto para CHAT_URI con permisos restringidos por seguridad. Se necesita obtener una API KEY de OpenAI [aqui](https://platform.openai.com/api-keys).

`URI = 'mysql+pymysql://user:password@localhost:3306/Conurma'`

`CHAT_URI = 'mysql+pymysql://user2:password@localhost:3306/Conurma'`

`OPENAI_API_KEY = 'sk-WrrN..................'`

## Creación de la base da datos inicial

En primer lugar se necesita crear una base de datos nueva en nuestro servidor SQL e introducir ese mismo nombre la URI en el archivo `.env`.

Una vez realizado este paso, se cargan los archivos que están en la carpeta `data_carga_inicial` ejecutando el siguiente comando:

```bash
python create_db.py
```


## Endpoints

Para inicializar el servidor de FastAPI, creado en el archivo `main.py`, se ejecuta el siguiente comando:
```bash
uvicorn main:app
```

Una vez inicializado el servidor, disponemos de cuatro endpoints.

1. Endpoint `select`:

    Con este endpoint podemos recuperar todos los datos de cualquier tabla que exista en la base de datos. Recordemos que dentro de la base de datos existen ocho tablas cuyos nombres son: `asig_inic_pir6`, `categorias`, `categorizacion`, `codigos_estado`, `datos_municipales`, `municipios`, `hoja_final`. Estos son los nombres que tienen las tablas en la base de datos. Este endpoint solo requiere como parámetro el nombre de la tabla a recuperar, un ejemplo de uso de este endpoint con curl es el siguiente:

    ```bash
    curl --location --request POST "http://127.0.0.1:8000/select" \
    --header "Content-Type: application/json" \
    --data-raw '{"table": "municipios"}'        
    ``` 

2. Endpoint `update`:

     Con este endpoint podemos actualizar tablas que hayan sido modificadas desde el frontend. Como parámetros tiene el usuario, el nombre de la tabla y los datos a modificar. Un ejemplo de uso de este endpoint con curl es el siguiente: 

    ```bash
    curl --location --request POST "http://127.0.0.1:8000/update" \
    --header "Content-Type: application/json" \
    --data-raw '{
    "user": "Yona",
    "table": "categorizacion",
    "data": [
        { "id": 1,
        "orden": 0,
        "status": null,
        "categorias": "PARQUES Y ZONAS VERDES",
        "subcategorias": "ZONAS VERDES"
        },
        { "id": 2,
        "orden": 1,
        "status": null,
        "categorias": "PARQUES Y ZONAS VERDES",
        "subcategorias": "PARQUE INFANTIL"
        }
    ]
    }'
    ``` 


3. Endpoint `dragdrop`:

    Este endpoint gestiona la creación y subida a la base datos de las tablas que se generan con el archivo `zip` que se arrastra a la aplicación. Tiene como parámetro la ruta donde son subidos archivos. Un ejemplo de uso de este endpoint con curl es el siguiente: 

    ```bash
    curl -X  POST http://127.0.0.1:8000/dragdrop \
    -H 'accept: application/json' \
    -H 'Content-Type: multipart/form-data' \
    -F 'payload=@tmp_example/ficheros_alimentacion.zip'
    ``` 


4. Endpoint `query`:

    Este endpoint realiza una consulta según el número de registro para ser visualizado. Tiene como parámetros el número de registro y el programa (PIR5 o PIR6). Un ejemplo de uso de este endpoint con curl es el siguiente: 

    ```bash
    curl --location --request POST http://127.0.0.1:8000/query \
    --header "Content-Type: application/json" \
    --data-raw '{"n_registro": "10-PAM1-00053.8/2021", "programa": "PIR6"}'
    ```

5. Endpoint `chat`:

    Este endpoint realiza la llamada al chatbot para hacer la consultas en la base de datos. Tiene como parámetros el usuario y el texto de 
    entrada del usuario. Un ejemplo de uso de este endpoint con curl es el siguiente: 
    ```bash
    curl --location --request POST http://127.0.0.1:8000/chat \
    --header "Content-Type: application/json" \
    --data-raw '{"content": "dame la informacion completa de la actuacion 10173303579 en una tabla", "user": "Yona"}'
    ```



Todos los endpoints devuelven un mensaje de error en caso de fallar.


## Proceso de Drag and Drop

En el proceso de drag and drop en la aplicación, se tiene que comprimir en un archivo `zip` la carpeta ficheros_alimentacion creada con la siguiente estructura y se arrastra a la aplicación:

```plaintext
├── 📁 ficheros_alimentacion                                    # Carpeta para archivos de subida
│   │
│   ├── 📁 250114_PIR5                                          # Carpeta para archivos de PIR5
│   │   ├── 📄 250114_T1_Actuaciones_PIR5.xlsx                  # Archivo Excel de T1 PIR5
│   │   ├── 📄 250115_T2_Estado+de+Actuaciones_PIR5.xlsx        # Archivo Excel de T2 PIR5
│   │   ├── 📄 250114_T5_SeguimientoEconómico_PIR5.xlsx         # Archivo Excel de T5 PIR5
│   │   └── 📄 250114_T6_DocumentosContables_PIR5.xlsx          # Archivo Excel de T6 PIR5         
│   │
│   └── 📁 250114_PIR6                                          # Carpeta para archivos de PIR6
│       ├── 📄 250114_T1_ListadoActuacionesSolicitud_PIR6.xlsx  # Archivo Excel de T1 PIR6
│       ├── 📄 250114_T2_ExportacionDatosGestion_PIR6.xlsx      # Archivo Excel de T2 PIR6
│       ├── 📄 250114_T3_PlanActuacion_PIR6.xlsx                # Archivo Excel de T3 PIR6
│       ├── 📄 250114_T4_Actuaciones_PIR6.xlsx                  # Archivo Excel de T4 PIR6
│       ├── 📄 250114_T5_FondoReserva_PIR6.xlsx                 # Archivo Excel de T5 PIR6
│       ├── 📄 250114_T6_informesSituacionInversion_PIR6.xlsx   # Archivo Excel de T6 PIR6
│       ├── 📄 250114_PAGOS_PIR6.xlsx                           # Archivo Excel de pagos
│       └── 📄 250114_T7_GastoCorriente_PIR6.xlsx               # Archivo Excel de T7 PIR6
```

Se crea una carpeta temporal `tmp` y una vez realizada la subida a la base de datos se borra la carpeta de manera automática. Un ejemplo de la estructura de la carpeta y un archivo `zip` se encuentran en la carpeta `tmp_example`.


## Proceso de despliegue

1. Crear una base de datos vacía en el servidor SQL.

2. Obtener URI de la base de datos de SQL y colocarla en el archivo `.env` (ejemplo en el archivo `.env.template`).

3. Ejecutar el archivo `create_db.py` con el siguiente comando:
    ```bash
    python create_db.py
    ```
    Esto subirá los datos iniciales a SQL y creará las relaciones entre tablas.

4. Conectar el servidor del backend con este repositorio o subir estos archivos al servidor.

5. Instalar dependencias en el servidor. Se puede usar el archivo `uv.lock` con el siguiente comando:
    ```bash
    uv sync
    ```
    También puede usarse el archivo `requirements.txt` usando el siguiente comando:
    ```bash
    pip install -r requirements.txt
    ```
    Existe también un `Dockerfile` para realizar la instalación e inicio del servidor.


6. Levantar el servidor con el siguiente comando:
    ```bash
    uvicorn main:app
    ```
    Con este proceso se completa el despliegue del backend para conectar posteriormente con el frontend.