# librerias   
import warnings
warnings.filterwarnings('ignore')

from sqlalchemy import create_engine, text

from langchain import SQLDatabase
from langchain_core.prompts import PromptTemplate
from langchain.chains import create_sql_query_chain
from langchain_openai.chat_models import ChatOpenAI   


import os                          
from dotenv import load_dotenv  

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')


URI = os.getenv('URI')



def get_sql_response(prompt: str) -> str:

    """
    Funcion para automatizar queries de SQL.

    Params: prompt , string, nuestra pregunta

    Return: string, respuesta del chat
    """
    

    global OPENAI_API_KEY, URI
    
    # prompt inicial
    input_model = ChatOpenAI(model='gpt-4.1', temperature=0)
        
    
    # conexion a base de datos
    cursor = create_engine(URI).connect()

    tablas = cursor.execute(text('show tables;')).all()
    tablas = [e[0] for e in tablas]

    db = SQLDatabase.from_uri(URI, sample_rows_in_table_info=1, include_tables=tablas)



    # definion del prompt para generar query SQL
    template = '''

    Eres un experto en {dialect}. Dada una pregunta de entrada:

    1. Primero, crea una consulta en {dialect} que sea sintácticamente correcta para ejecutar.  
    2. A menos que el usuario especifique en la pregunta un número específico de ejemplos a obtener, 
    no utilices la cláusula `LIMIT`. Si se pide limitar sin un número específico, utiliza las primera {top_k} filas.  
    3. Nunca consultes todas las columnas de una tabla; solo debes seleccionar las columnas 
    necesarias para responder la pregunta.  
    4. Encierra cada nombre de columna con backticks (`) para identificarlos como identificadores delimitados.  
    5. Usa solo los nombres de columna visibles en las tablas a continuación. No consultes columnas que no existan. 
    Asegúrate de saber en qué tabla se encuentra cada columna.  
    6. Usa la función `CURDATE()` para obtener la fecha actual si la pregunta involucra "hoy".  
    7. Solo usa sentencias `SELECT` para consultar datos.  
    8. La información de las tablas es la siguiente:
    {table_info}  

    ### Pregunta  
    {input}  

    ### Formato de salida  
    ```sql  
    consulta a ejecutar  
    ```  

    Tu respuesta debe ser únicamente la consulta en {dialect}. 
    '''

    
    sql_prompt = PromptTemplate(input_variables=['input', 'table_info', 'top_k', 'dialect'],
                                template=template)
    
    
    # creacion de query SQL
    database_chain = create_sql_query_chain(input_model, db, prompt=sql_prompt)

    sql_query = database_chain.invoke({'question': prompt})

    sql_query = sql_query.split('```sql')[1].replace('`', '')

        
    
    # ejecucion de la query SQL
    contexto = cursor.execute(text(sql_query)).all()
    
    
    
    # respuesta final 
    output_model = ChatOpenAI(model='gpt-4.1')

    final_prompt = f'''Dados el siguiente contexto y query, responde la pregunta: 
                    
                    contexto: {contexto}, 
                    
                    query: {sql_query},
                    
                    pregunta: {prompt}
                    
                    No hables del contexto ni de la query.
                    Devuelve la respuesta lo mas extensa posible.
                    
                    '''
    
    return output_model.invoke(final_prompt).content


