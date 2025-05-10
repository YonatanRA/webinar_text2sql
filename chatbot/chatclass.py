# libreries  
import warnings
warnings.filterwarnings('ignore')
import os                          
from dotenv import load_dotenv  
from operator import itemgetter

from sqlalchemy import create_engine, inspect

from langchain import SQLDatabase
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import create_sql_query_chain
from langchain_openai.chat_models import ChatOpenAI  
from langchain.schema import StrOutputParser
from langchain.schema.runnable import RunnableLambda, RunnablePassthrough
from langchain.memory import ConversationBufferWindowMemory

from .prompts import sql_prompt_template, tone_prompt_template, final_prompt_template
from tools import logger


load_dotenv(override=True)

URI = os.getenv('URI')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')



class Text2SQL:

    def __init__(self):

        logger.info('Iniciar Chat')
        
        self.tables = inspect(create_engine(URI)).get_table_names()
        self.db = SQLDatabase.from_uri(URI, sample_rows_in_table_info=2, include_tables=self.tables)
        self.sql_query = None
        self.last_sql_query = None
        self.context = None
        self.memory = ConversationBufferWindowMemory(k=4, return_messages=True)
    

    def create_sql_query(self, prompt: str) -> str:

        """
        Metodo para crear query de SQL, actualiza el atributo self.sql_query

        Params: prompt, str, consulta del usuario

        Return: None
        """

        logger.info('Creando query...')

        input_model = ChatOpenAI(model='gpt-4.1', temperature=0)

        sql_prompt = PromptTemplate(template=sql_prompt_template)
                
        database_chain = create_sql_query_chain(input_model, self.db, prompt=sql_prompt, k=None)

        sql_query = database_chain.invoke({'question': prompt, 
                                           'last_query': self.last_sql_query,
                                           'table_names': self.tables})

        sql_query = sql_query.split('```sql')[1].replace('`', '')

        DML = ['create', 'drop', 'delete', 'alter', 'insert', 'update']

        for clause in DML:
            if clause in sql_query.lower():
                self.sql_query = 'SELECT "Actua como un asistente, usa la memoria"'
            else:
                self.sql_query = sql_query

        logger.info('Query creada!')
    

    def execute_and_check_query(self, prompt: str) -> None:

        """
        Metodo para ejecutar la query de SQL 

        Params: prompt, str, consulta del usuario

        Return: None, actualiza el atributo contexto
        """

        logger.info('Ejecutando query...')

        done = False
        counter = 0

        while not done:

            counter += 1

            if counter==5:
                logger.info('Saliendo de la ejecución SQL')
                break

            try:
                self.create_sql_query(prompt)
                logger.info(f'SQL query: {self.sql_query}')
                context = self.db.run(self.sql_query)  
            except Exception as e:
                logger.info(e)
                logger.info('Fallo obteniendo resultados, creando query de nuevo...')
                context = ''
                self.create_sql_query(f'''Este prompt {prompt} genera esta query {self.sql_query}, pero da este error {e}. 
                                      Genera correctamente la query para el prompt dado''')
                context = self.db.run(self.sql_query)  
            
            if not context:
                logger.info('Contexto vacio, creando query de nuevo...')
                self.create_sql_query(f'''Este prompt {prompt} genera esta query {self.sql_query}, pero no devuelve resultados. 
                                      Reformula y simplifica la query para que devuelva resultados de la base de datos.''')
                context = self.db.run(self.sql_query) 
            
            else:
                done = True
        
        self.context = context

        logger.info('Contexto creado')
    

    def chain_to_response(self) -> object:

        """
        Metodo para crear la cadena de langchain

        Return: cadena de langchain
        """

        output_model = ChatOpenAI(model='gpt.-4.1', streaming=True, max_retries=1, max_tokens=32768)

        final_prompt = ChatPromptTemplate.from_messages([('system', tone_prompt_template),
                                                         
                                                         MessagesPlaceholder(variable_name='history'),
                                                         
                                                         ('human', final_prompt_template)])


        chain = (RunnablePassthrough.assign(history=RunnableLambda(self.memory.load_memory_variables) 
                                            | itemgetter('history'))) | final_prompt  | output_model | StrOutputParser()

        return chain
    

    def main(self, prompt: str):

        self.execute_and_check_query(prompt)

        chain = self.chain_to_response()

        try:
            logger.info('Generando respuesta...')
            response = ''
            for chunk in chain.stream({'sql_query': self.sql_query, 
                                       'context': self.context,
                                       'prompt': prompt}):
                    
                yield(chunk)
                response += chunk

            self.memory.save_context({'question': prompt}, {'response': response})
        
        except Exception as e:
            try:
                logger.info(f'Recuperando memoria...Error: {e}')
                response = ''
                if self.memory.load_memory_variables({})['history']:
                    last_messages = self.memory.load_memory_variables({})['history'][-2:]
                    self.memory = ConversationBufferWindowMemory(k=4, return_messages=True)
                    self.memory.save_context({'question': last_messages[-2].content}, {'response': last_messages[-1].content})
                else:
                    self.memory = ConversationBufferWindowMemory(k=4, return_messages=True)
                response = ''
                for chunk in chain.stream({'sql_query': self.sql_query, 
                                           'context': self.context,
                                           'prompt': prompt}):
                        
                    yield(chunk)
                    response += chunk
                self.memory.save_context({'question': prompt}, {'response': response})

            except Exception as e:
                logger.info(f'Respuesta por defecto, contexto demasiado grande. Error: {e}')
                response = ''
                self.memory = ConversationBufferWindowMemory(k=4, return_messages=True)
                response = 'El contexto es demasiado grande, por favor realiza una pregunta más específica para poder responderte.'
                for chunk in response:
                        
                    yield(chunk)
                    response += chunk

            self.memory.save_context({'question': prompt}, {'response': response})

        self.last_sql_query = self.sql_query
        self.sql_query = None
        self.context = None
        logger.info('Hecho')
