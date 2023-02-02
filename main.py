import os
import warnings
from ontology_dc8f06af066e4a7880a5938933236037.simple_text import SimpleText

from openfabric_pysdk.context import OpenfabricExecutionRay
from openfabric_pysdk.loader import ConfigClass
from time import time
# Importing Libraries
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


############################################################
# Callback function called on update config
############################################################
def config(configuration: ConfigClass):
    # TODO Add code here
    pass


############################################################
# Callback function called on each execution pass
############################################################
def execute(request: SimpleText, ray: OpenfabricExecutionRay) -> SimpleText:
    chatbot=ChatBot('conversation bot')
    trainer = ChatterBotCorpusTrainer(chatbot)
    trainer.train("chatterbot.corpus.english.greetings",
              "chatterbot.corpus.english.conversations" )
    output = []

    for text in request.text:
        # TODO Add code here
        response = chatbot.get_response(text)
        output.append(response)

    return SimpleText(dict(text=output))
