# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


from striprtf.striprtf import rtf_to_text
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Text, Dict, List

class ActionListCountries(Action):
    def name(self) -> Text:
        return "action_list_countries"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Dict[Text, Any],
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Path to your .rtf file
        rtf_path = "/Users/rehanedin/Documents/neo_bank_churn/y/countries.rtf"

        try:
            # Read the .rtf file
            with open(rtf_path, "r") as file:
                rtf_content = file.read()

            # Convert RTF to plain text
            plain_text = rtf_to_text(rtf_content)

            # Extract countries (assume one country per line)
            countries = [line.strip() for line in plain_text.splitlines() if line.strip()]

            if countries:
                country_list = ", ".join(countries)
                response = f"We currently serve the following countries: {country_list}."
            else:
                response = "I'm sorry, the list of countries is empty."

        except Exception as e:
            response = "I couldn't retrieve the list of countries right now."
            print(f"Error reading the .rtf file: {e}")

        dispatcher.utter_message(text=response)
        return []
