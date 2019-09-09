'''
Scenario Data hardcoded for now
'''
scenarios = []

# scenarios.append({SCENARIO_NAME:'put name of scenario here',
#                   ID:0,
#                   DIALOG:'put dialog here',
#                   YES:if answer is yes goto  id indicated
#                   NO:i fanswer is no goto id indicated
#                   EXIT:'type EXIT here if this dialog then ends the scenario starting a new one',
#                   CREW_MORALE:'place a positive or negative integer if crew morale is affected by this outcome',
#                   SHIP_STRENGTH:'place a positive or negative integer if ship strength is affected by this outcome',
#                   INTEL:'place a positive or negative integer if intel is affected by this outcome'})

scenarios.append({'SCENARIO_NAME':'WELCOME MESSAGE',
                  'ID': 0,
                  'DIALOG':'You are a mixed crew of misfits on your mission to find the illusive and dastardly Aldric Von Monico to stop his evil space pirates and the rumored super weapon they are building at a secret location. As you explore keep track of your ships crew morale, and ship strength, if either goes below zero you will lose your mission. On your adventures try to find secrets of the location of Von Monico and his pirate weapon for the final showdown by gathering intel. Welcome to the adventure captain, adventure awaits you and your misfit crew. Say Yes to proceed or No to give up now.',
                  'YES':1,
                  'NO':0,
                  'EXIT':0,
                  'CREW_MORALE':50,
                  'SHIP_STRENGTH':50,
                  'INTEL':0})

scenarios.append({'SCENARIO_NAME':'DISTRESS CALL 1',
                  'ID': 1,
                  'DIALOG':'Captain, I have picked up a distress call coming from the vega system, would you like for us to respond?',
                  'YES':3,
                  'NO':2,
                  'EXIT':0,
                  'CREW_MORALE':0,
                  'SHIP_STRENGTH':0,
                  'INTEL':0})
scenarios.append({'SCENARIO_NAME':'DISTRESS CALL 1',
                  'ID': 2,
                  'DIALOG':'Aye Aye Captain, we will avoid this beacon. Spock Says, Good thinking Captain, after further analysis, I believe this signal shows a similar pattern to onse that the USS Cole fell victom to as an Alrick Von Monicko decoy. We might have gained some interesting intel though.',
                  'YES':0,
                  'NO':0,
                  'EXIT':1,
                  'CREW_MORALE':0,
                  'SHIP_STRENGTH':0,
                  'INTEL':5})
scenarios.append({'SCENARIO_NAME':'DISTRESS CALL 1',
                  'ID': 3,
                  'DIALOG':'Captain, we are arriving at the coordinates of the distress call. Ohura calls out, Captain we are reading multiple distress calls from a vulcan cruiser, Spock Says, Captain, scans show multiple life forms on the ship, however their signals are weaker than expected. Shall we send a boarding crew to investigate?',
                  'YES':4,
                  'NO':2,
                  'EXIT':0,
                  'CREW_MORALE':0,
                  'SHIP_STRENGTH':0,
                  'INTEL':0})
scenarios.append({'SCENARIO_NAME':'DISTRESS CALL 1',
                  'ID': 4,
                  'DIALOG':'You beam on board the Cruiser and notice a strange acidic smell that burns your nostrils. After placing breathing masks Seargent Oleg calls out, Captain! Over here! I am detecting multiple strange life signals from the room ahead. Scotty also calls out, Captain! I am detecting a strange power surge from what looks like the engine room, this could be trouble, the hyper drive could be going critical soon. Say Yes to stay in the Engine Room Engine Room or Say No to go rescue the Life forms.',
                  'YES':5,
                  'NO':6,
                  'EXIT':0,
                  'CREW_MORALE':0,
                  'SHIP_STRENGTH':0,
                  'INTEL':0})
scenarios.append({'SCENARIO_NAME':'DISTRESS CALL 1',
                  'ID': 5,
                  'DIALOG':'Scotty says, Captain, it looks like the hyper drive is in critical condition and unstable, at most we have minutes before the drive blows. If I focus on this, we will not have enough time to deal with the survivors, say yes to beam off the ship before it explodes, or say no to try and resecue the survivors before it is too late.',
                  'YES':8,
                  'NO':6,
                  'EXIT':'',
                  'CREW_MORALE':'',
                  'SHIP_STRENGTH':'',
                  'INTEL':''})
scenarios.append({'SCENARIO_NAME':'DISTRESS CALL 1',
                  'ID': 6,
                  'DIALOG':'You manage to access the room and your crew discoveres a handful of vulcan aliens tending to their wounded.  Scotty calls out, Captain! I am detecting a dangerous increase in hyperdrive levels from the engine room, we need to beam off this ship! Do you bring the wounded vulcan aliens with your crew?',
                  'YES':7,
                  'NO':8,
                  'EXIT':0,
                  'CREW_MORALE':0,
                  'SHIP_STRENGTH':0,
                  'INTEL':0})
scenarios.append({'SCENARIO_NAME':'DISTRESS CALL 1',
                  'ID': 7,
                  'DIALOG':'The Cruiser explodes at a safe distance and after some time in the medical bay Ohura declares, Captain, we managed to piece together what happened, it is a good thing we saved this crew, we learned some valueable information about Von Monikos pirate fleet from some of the discussions and readings they brought with them as we were leaving the ship.',
                  'YES':0,
                  'NO':0,
                  'EXIT':1,
                  'CREW_MORALE':0,
                  'SHIP_STRENGTH':0,
                  'INTEL':20})
scenarios.append({'SCENARIO_NAME':'DISTRESS CALL 1',
                  'ID': 8,
                  'DIALOG':'The Cruiser explodes at a safe distance and after some time the Scotty says, Captain, we managed to gather some interesting technology which we think will help increase our ships strength, however, the crew is not happy that we abandoned a crew in need.',
                  'YES':0,
                  'NO':0,
                  'EXIT':1,
                  'CREW_MORALE':-20,
                  'SHIP_STRENGTH':30,
                  'INTEL':0})
