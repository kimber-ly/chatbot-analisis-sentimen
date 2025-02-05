# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_hello_world"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(text="Hello World!")

#         return []

class ActionCariData(Action):
    def name(self) -> str:
        return "action_cari_data"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        topic = next(tracker.get_latest_entity_values("topic"), None)
        if topic:
            dispatcher.utter_message(text = f"Mencari data untuk topik {topic}...")
        else:
            dispatcher.utter_message(text="Entitas 'topic' tidak dikenali.")
        return [SlotSet("topic", topic)]

class Sentimen(Action):
    def name(self) -> str:
        return "action_analyze_sentiment"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        topic = next(tracker.get_latest_entity_values("topic"), None)

        # dispatcher.utter_message(template="utter_analyze_sentiment")
        dispatcher.utter_message(text = f"Berikut adalah hasil analisis sentimen untuk topik {topic}")
        return [SlotSet("topic", topic), SlotSet("sentiment_analysis", "true")]
    
class Visualisasi(Action):
    def name(self) -> str:
        return "action_visualisasi"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        topic = next(tracker.get_latest_entity_values("topic"), None)
        dispatcher.utter_message(text = f"Melakukan visualisasi untuk hasil analisis sentimen topik {topic}")
        return [SlotSet("topic", topic)]

class Rekomendasi(Action):
    def name(self) -> str:
        return "action_give_recommendations"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        topic = next(tracker.get_latest_entity_values("topic"), None)
        sentiment_analysis = tracker.get_slot("sentiment_analysis")
        dispatcher.utter_message(text = f"Berikut adalah rekomendasi untuk topik {topic}")
        return [SlotSet("topic", topic)]

class SendResponse(Action):
    def name(self) -> str:
        return "action_send_response"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text = "Mengirimkan respons ke anda...")
        return []