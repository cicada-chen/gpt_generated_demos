from flask import Flask, request, jsonify
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.interfaces import Tracker
from actions import ActionHandleInquiries, ActionMakeBooking, ActionCheckFlightStatus, ActionAnswerPolicyQuestions

class VirtualAgent:
    def __init__(self, name: str, version: str, airline_systems: str):
        self.name = name
        self.version = version
        self.airline_systems = airline_systems

    def handle_inquiries(self, inquiry: str):
        dispatcher = CollectingDispatcher()
        tracker = Tracker(sender_id="sender", slots={"inquiry": inquiry}, latest_message={}, paused=False, events=[], followup_action=None, active_form={}, latest_action_name=None)
        action = ActionHandleInquiries()
        action.run(dispatcher, tracker, {})
        return dispatcher.messages

    def make_booking(self, booking_info: dict):
        dispatcher = CollectingDispatcher()
        tracker = Tracker(sender_id="sender", slots={"booking_info": booking_info}, latest_message={}, paused=False, events=[], followup_action=None, active_form={}, latest_action_name=None)
        action = ActionMakeBooking()
        action.run(dispatcher, tracker, {})
        return dispatcher.messages

    def check_flight_status(self, flight_number: str):
        dispatcher = CollectingDispatcher()
        tracker = Tracker(sender_id="sender", slots={"flight_number": flight_number}, latest_message={}, paused=False, events=[], followup_action=None, active_form={}, latest_action_name=None)
        action = ActionCheckFlightStatus()
        action.run(dispatcher, tracker, {})
        return dispatcher.messages

    def answer_policy_questions(self, question: str):
        dispatcher = CollectingDispatcher()
        tracker = Tracker(sender_id="sender", slots={"question": question}, latest_message={}, paused=False, events=[], followup_action=None, active_form={}, latest_action_name=None)
        action = ActionAnswerPolicyQuestions()
        action.run(dispatcher, tracker, {})
        return dispatcher.messages

app = Flask(__name__)
virtual_agent = VirtualAgent("Airline Virtual Agent", "3.3.0", "Airline Systems")

@app.route('/handle_inquiries', methods=['POST'])
def handle_inquiries():
    inquiry = request.json['inquiry']
    return jsonify(virtual_agent.handle_inquiries(inquiry))

@app.route('/make_booking', methods=['POST'])
def make_booking():
    booking_info = request.json['booking_info']
    return jsonify(virtual_agent.make_booking(booking_info))

@app.route('/check_flight_status', methods=['POST'])
def check_flight_status():
    flight_number = request.json['flight_number']
    return jsonify(virtual_agent.check_flight_status(flight_number))

@app.route('/answer_policy_questions', methods=['POST'])
def answer_policy_questions():
    question = request.json['question']
    return jsonify(virtual_agent.answer_policy_questions(question))

if __name__ == '__main__':
    app.run(debug=True)
