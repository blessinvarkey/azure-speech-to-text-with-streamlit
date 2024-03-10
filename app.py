import azure.cognitiveservices.speech as speechsdk
import streamlit as st

speech_key = st.secrets["speech_service"]["key"]
service_region = st.secrets["speech_service"]["region"]

def speech_recognize_once_from_mic():
    # Set up the speech config and audio config
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    audio_config = speechsdk.AudioConfig(use_default_microphone=True)

    # Create a speech recognizer with the given settings
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    st.write("Speak into your microphone.")
    result = speech_recognizer.recognize_once_async().get()

    # Check the result
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        return f"Recognized: {result.text}"
    elif result.reason == speechsdk.ResultReason.NoMatch:
        return "No speech could be recognized"
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        return f"Speech Recognition canceled: {cancellation_details.reason}"
    else:
        return "Unknown error"

st.title("Azure Speech Service with Streamlit")

if st.button('Start speech recognition'):
    recognition_result = speech_recognize_once_from_mic()
    st.write(recognition_result)
