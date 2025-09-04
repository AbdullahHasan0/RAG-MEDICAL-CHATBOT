from langchain_openai import ChatOpenAI
from app.config.config import OPENAI_API_KEY

from app.common.logger import get_logger
from app.common.custom_exception import CustomException

logger = get_logger(__name__)

def load_llm(openai_api_key: str = OPENAI_API_KEY):
    try:
        logger.info("Initializing our Huggingface LLM model")
        llm = ChatOpenAI(
            model="gpt-4o-mini",    
            api_key=openai_api_key,
            temperature=0.3,
            max_tokens=512
        )
        
        logger.info("OpenAI LLM model loaded successfully")
        return llm

    except Exception as e:
        error_message = CustomException("Error occurred while loading LLM model.", e)
        logger.error(str(error_message))
        raise error_message