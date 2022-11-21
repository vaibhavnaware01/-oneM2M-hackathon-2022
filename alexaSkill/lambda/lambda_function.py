# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput
import requests
from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Welcome to One m. two m. , Please ask for status of node by saying its name"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


def wisunProcess(slot_name):
    OM2M_URL_BASE = "https://onem2m.iiit.ac.in/~/in-cse/in-name/AE-WN/"
    OM2M_HEADERS = {
        'X-M2M-Origin': 'guest:guest',
        'Accept': 'application/json'
    }
    slot_cleanify = slot_name.replace(" dash ","-")
    latest = OM2M_URL_BASE + slot_cleanify + "/Status/la"
    try:
        resp = requests.get(url=latest, headers=OM2M_HEADERS).json()['m2m:cin']['con']
        if("OFF" in resp):
            return "The light is currently turned off"
        elif("ON" in resp):
            return "The light is currently turned on"
        else:
            return "The light is in super quantum entanglement with quasi boson nucleus from Alpha centauri"
    except Exception as e:
        return f"Something went wrong with fetching data from one m. two m"

def wisunSetter(slot_name,status):
    slot_cleanify = slot_name.replace(" dash ","-")
    OM2M_URL_BASE = "https://onem2m.iiit.ac.in/~/in-cse/in-name/AE-WN/"
    value = None
    OM2M_HEADERS = {
        'X-M2M-Origin': 'WisunMon@20:5T&6OnuL1iZ',
        'Content-type': 'application/json;ty=4'
    }
    lamp_code = slot_cleanify.split("-")[1]
    latest = OM2M_URL_BASE + slot_cleanify + "/Data"

    if(status == "on" or status == "true" or status == "ON" or status == "high"):
        value = f".{lamp_code}ON"
    else:
        value = ".{lamp_code}OFF"
        
    DATA = {
        "m2m:cin": {
            "con": str(value),
            "lbl": ["AE-WN",
                   "V1.0.0",
                   "AE-WN-V1.0.0"],
            "cnf": "text"
        }
    }
    response = requests.post(latest, json=DATA, headers=OM2M_HEADERS)
    if(response.status_code < 300):
        return "Changed the lamp status"
    else:
        return f"Something went wrong pushing data to 1 m2m , Got response {response.status_code}"
    return "Something went wrong when processing the quantum state of the universe"

class WisunSetIntentHandler(AbstractRequestHandler):
    "Handling Wisun Lamp checking intent"
    def can_handle(self,handler_input):
        return ask_utils.is_intent_name("WisunSetIntent")(handler_input)
    
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        lampslot = str(handler_input.request_envelope.request.intent.slots['LAMP_ID'].value)
        boolslot = str(handler_input.request_envelope.request.intent.slots['BOOL'].value)
        node_out = wisunSetter(lampslot,boolslot)
        speak_output = node_out

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


class WisunCheckIntentHandler(AbstractRequestHandler):
    "Handling Wisun Lamp checking intent"
    def can_handle(self,handler_input):
        return ask_utils.is_intent_name("WisunCheckIntent")(handler_input)
    
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        slotu = str(handler_input.request_envelope.request.intent.slots['LAMP_ID'].value)
        node_out = wisunProcess(slotu)
        speak_output = node_out

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


class HelloWorldIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("HelloWorldIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "This is a hello world intent shit"

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "You can say hello to me! How can I help?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Goodbye!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class FallbackIntentHandler(AbstractRequestHandler):
    """Single handler for Fallback Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In FallbackIntentHandler")
        speech = "Hmm, I'm not sure. You can say Hello or Help. What would you like to do?"
        reprompt = "I didn't catch that. What can I help you with?"

        return handler_input.response_builder.speak(speech).ask(reprompt).response

class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(HelloWorldIntentHandler())
sb.add_request_handler(WisunCheckIntentHandler()) #WisunSetIntentHandler
sb.add_request_handler(WisunSetIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()