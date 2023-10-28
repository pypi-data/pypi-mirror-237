import os
import openai
from msgkit import errorlog

openai.api_key = os.getenv("OPENAI_API_KEY")

logger = errorlog.ErrorLog()
