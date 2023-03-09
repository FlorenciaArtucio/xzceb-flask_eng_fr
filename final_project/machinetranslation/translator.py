import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

# create Translator instance
authenticator = IAMAuthenticator('LMpaArUkKGDwGcc2f3Kc4tNcDrW9Hn9_vTc969ad6fZV')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator)
language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/c6e47edf-a5e7-4ae5-8b31-ee7791bde6bf')

#except Exception as e:
#print(f'+++ERROR: translator instance creation failed:\n{e}')


# translate english to french

def english_to_french(english_text):
    #write the code here
    french_text = language_translator.translate( text=english_text , model_id='en-fr').get_result()
    return french_text.get("translations")[0].get("translation")

def french_to_english(french_text):
    #write the code here
    english_text = language_translator.translate( text=french_text , model_id='fr-en').get_result()
    return english_text.get("translations")[0].get("translation")
