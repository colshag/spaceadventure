"""
AWS lambda code by end of part 2 of programming alexa series
"""

from __future__ import print_function
import random
from insults import get_insult
from scenarios import scenarios

# --------------- Helpers that build all of the responses ----------------------
def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }

def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def __pass_session_attributes(session):
    """Get the current session attributes and pass them back as a dictionary for the session_attributes dictionary
    to keep the session attributes active"""
    d = {}
    if session.get('attributes', {}):
        d['crew_morale'] = session['attributes']['crew_morale']
        d['ship_strength'] = session['attributes']['ship_strength']
        d['intel'] = session['attributes']['intel']
        d['id'] = session['attributes']['id']
    
    print('pass_session_attributes====>')
    print(d)
    return d

def get_status_response(intent, session):
    """ Give player current status
    """
    print("get_status_response===>")
    print(session)
    session_attributes = __pass_session_attributes(session)
    speech_output = "I'm sorry there has been an error, please contact neurojump forums"
    
    if session.get('attributes', {}):
        speech_output = "Yes Captain, your crew morale is %d, your ship strength is %d, you have %d intelligence on the location of Alrick Von Monico." % (session_attributes['crew_morale'],
                                                                                                                                                          session_attributes['ship_strength'],
                                                                                                                                                          session_attributes['intel'])
        speech_output = speech_output + " Back to the story. " + scenarios[session_attributes['id']]['DIALOG']
        
    card_title = "Status"
    reprompt_text = speech_output
    should_end_session = False
    
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def get_yes_response(intent, session):
    """ A player says Yes to the next choice, give them the next scene accordingly to where they are in the mission
    """
    print("get_yes_response===>")
    print(session)
    session_attributes = __pass_session_attributes(session)
    speech_output = "I'm sorry there has been an error, please contact neurojump forums"
    
    if session.get('attributes', {}):
        # determine where to go based on yes being said
        current_id = session_attributes['id']
        new_id = scenarios[current_id]['YES']
        speech_output = scenarios[new_id]['DIALOG'] # new dialog
        session_attributes['id'] = new_id # send player to next dialog choice
        session_attributes['crew_morale'] = session_attributes['crew_morale'] + scenarios[current_id]['CREW_MORALE'] # update morale
        session_attributes['ship_strength'] = session_attributes['ship_strength'] + scenarios[current_id]['SHIP_STRENGTH'] # update ship strength
        session_attributes['intel'] = session_attributes['intel'] + scenarios[current_id]['INTEL'] # update intel
        
    card_title = "Yes"
    reprompt_text = speech_output
    should_end_session = False

    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
    
def get_no_response(intent, session):
    """ A player says No to the next choice, give them the next scene accordingly to where they are in the mission
    """
    print("get_no_response===>")
    print(session)
    session_attributes = __pass_session_attributes(session)
    speech_output = "I'm sorry there has been an error, please contact neurojump forums"
    
    if session.get('attributes', {}):
        # determine where to go based on yes being said
        current_id = session_attributes['id']
        new_id = scenarios[current_id]['NO']
        speech_output = scenarios[new_id]['DIALOG'] # new dialog
        session_attributes['id'] = new_id # send player to next dialog choice
        session_attributes['crew_morale'] = session_attributes['crew_morale'] + scenarios[current_id]['CREW_MORALE'] # update morale
        session_attributes['ship_strength'] = session_attributes['ship_strength'] + scenarios[current_id]['SHIP_STRENGTH'] # update ship strength
        session_attributes['intel'] = session_attributes['intel'] + scenarios[current_id]['INTEL'] # update intel
        
    card_title = "No"
    reprompt_text = speech_output
    should_end_session = False

    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """
    session_attributes = {'crew_morale':100, 
                          'ship_strength':100,
                          'intel':0,
                          'id':0
                          }

    card_title = "Welcome"
    speech_output = scenarios[0]['DIALOG']
    reprompt_text = speech_output
    should_end_session = False
    
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for trying Cosmica, a space adventure. " \
                    "Have a great day! "
                    
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))

# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts.
        One possible use of this function is to initialize specific 
        variables from a previous state stored in an external database
    """
    # Add additional code here as needed
    pass
    

def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """
    # Dispatch to your skill's launch message
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']


    # Dispatch to your skill's intent handlers
    if intent_name == "AMAZON.YesIntent":
        return get_yes_response(intent, session)
    elif intent_name == "AMAZON.NoIntent":
        return get_no_response(intent, session)
    elif intent_name == "status":
        return get_status_response(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_status_response(intent, session)
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        # raise ValueError("Invalid intent")
        return get_status_response(intent, session)


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.
    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("Incoming request...")

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
