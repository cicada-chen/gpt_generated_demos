## actions.py
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from typing import Any, Text, Dict, List

class ActionHandleInquiries(Action):
    def name(self) -> Text:
        return "action_handle_inquiries"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        inquiry = tracker.get_slot('inquiry')
        # TODO: Use the inquiry to generate a response.
        response = f"Here is the information you requested: {inquiry}"
        dispatcher.utter_message(text=response)
        return [SlotSet("inquiry", inquiry)]

class ActionMakeBooking(Action):
    def name(self) -> Text:
        return "action_make_booking"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        booking_info = tracker.get_slot('booking_info')
        # TODO: Use the booking_info to make a booking.
        response = f"Your booking has been made. Here is your confirmation: {booking_info}"
        dispatcher.utter_message(text=response)
        return [SlotSet("booking_info", booking_info)]

class ActionCheckFlightStatus(Action):
    def name(self) -> Text:
        return "action_check_flight_status"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        flight_number = tracker.get_slot('flight_number')
        # TODO: Use the flight_number to check the flight status.
        response = f"The status of flight {flight_number} is: On time"
        dispatcher.utter_message(text=response)
        return [SlotSet("flight_number", flight_number)]

class ActionAnswerPolicyQuestions(Action):
    def name(self) -> Text:
        return "action_answer_policy_questions"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        question = tracker.get_slot('question')
        # TODO: Use the question to generate a response.
        response = f"Here is the policy information you requested: {question}"
        dispatcher.utter_message(text=response)
        return [SlotSet("question", question)]
