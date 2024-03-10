# Azure Speech-to-text with Streamlit

One of the easiest ways to explore Azure AI services for a quick demo is by using Streamlit. Streamlit is an open-source app framework often used as the fastest way to build and share data apps. Integrating Azure AI with Streamlit can make your app (or exploration) more interactive. 
Let's get started. 

# Prerequisites
Before we begin, make sure you have the following:
- An active Azure account. If you don't have one, you can sign up for a free account here.
- You have an IDE and Python installed on your machine.
- You need to install Streamlit. If not, you can install it using pip: ```pip install streamlit```.

# Step 1: Create an Azure AI Service
The first step is to create an Azure AI service that you wish to integrate with your Streamlit app. There are a variety of AI services, including Azure AI Search, Computer Vision, Face API, Speech service, and Language services among others. 
So to get started: 
1. Log in to the Azure Portal.
2. Navigate to "Create a resource" > "AI + Machine Learning" and select the service you want to use. 
3. Follow the on-screen instructions to create your AI service. This will typically involve specifying a name for your service (For example Computer Vision), choosing a subscription, and selecting a resource group.
4. Once your service is set up, you'll need to access its API keys and endpoint information, which are required to interact with the service programmatically.

In the Azure Portal, navigate to your AI service resource.
- Under "Resource Management," on the left, find the "Keys and Endpoint" section.
- Copy the key(s) and endpoint URL. You'll use these in your Streamlit app to authenticate and send requests to the Azure AI service.

# Step 2: Azure AI with Streamlit
Now that you have your Azure AI service ready and have the necessary keys and endpoint, set up the environment. You can refer to the documentation [here](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/get-started-speech-to-text?tabs=linux%2Cterminal&pivots=programming-language-python).  
## For Windows:
```
setx SPEECH_KEY your-key
setx SPEECH_REGION your-region
```
For Linux/Mac: 
```
export SPEECH_KEY=your-key
export SPEECH_REGION=your-region
```
## On the console: 
```
pip install azure-cognitiveservices-speech
```
Create a file named _app.py_. You can get the code from [here](https://github.com/blessinvarkey/azure-speech-to-text-with-streamlit/blob/main/app.py)

# Step 3: Run Your Streamlit App
Run your Streamlit app by running the following line of code on the command line:

```
streamlit run app.py
```
Your Streamlit app should now be running locally.

![speech to text demo](https://raw.githubusercontent.com/blessinvarkey/azure-speech-to-text-with-streamlit/main/speech%20to%20text%20demo.png)

# Host your Streamlit app
You can host your streamlit app on [streamlit.io (community cloud)](https://azure-speech-to-text-with-app-5ybzm4yos9pyybsf5xmfje.streamlit.app) or on [HuggingFace](http://huggingface.co). If you are interested, check [this article](https://medium.com/@contact.blessin/deploying-azure-ai-services-using-streamlit-speech-to-text-295641c5de10)https://medium.com/@contact.blessin/deploying-azure-ai-services-using-streamlit-speech-to-text-295641c5de10 to see how to go about the same.
