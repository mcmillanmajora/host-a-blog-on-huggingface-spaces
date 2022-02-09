import streamlit as st

title = "Hate Speech Detection in Automatic Content Moderation"
description = "The history and development of hate speech detection as a modeling task"
date = "2022-01-26"
thumbnail = "images/huggingface_logo.png"

def run_article():
  st.markdown("""
  # What is Automatic Content Moderation?

  *This is where the history of automatic content moderation (ACM) will go.*  
  Content moderation is a collection of interventions used by online platforms to partially censor or remove entirely from user-facing view content that is objectionable based on the company's values or community guidelines, which vary from platform to platform. Gillespie (2018) writes that platforms moderate content ``both to protect one user from another, or one group from its antagonists, and to remove the offensive, vile, or illegal.'' While there are a variety of approaches to this problem, we focus on _automated_ content moderation, which is the application of algorithms to the classification of problematic content.

  # The Landscape of ACM

  *This is where the current platforms and approaches with go.*  
  Automated content moderation has relied both on analysis of the contents (e.g. relying on natural language processing and computer vision) as well as user dynamics (e.g. whether the accounts share followers, when the account was created). Within the realm of text-based ACM, approaches vary from wordlist-based approaches to data-driven models. Common datasets used for training and evaluating hatespeech detectors can be found at https://hatespeechdata.com/

  # What kind of content is subject to moderation?
  Different platforms have different guidelines about what content is allowed on the platform. (TODO: brief survey of guidelines?) For example, many US-based platforms prohibit posting threats of violence, nudity, and hate speech. We discuss hate speech below.
  
  # What is hate speech? 
  Hate speech is hard to define, with definitions shifting across time and location. In 2019, the United Nations [defined](https://www.un.org/en/genocideprevention/documents/advising-and-mobilizing/Action_plan_on_hate_speech_EN.pdf) hate speech as "any kind of communication in speech, writing or behaviour, that attacks or uses pejorative or discriminatory language with reference to a person or a group on the basis of who they are, in other words, based on their religion, ethnicity, nationality, race, colour, descent, gender or other identity factor."
  
  
  
  # Current Challenges

  *This is where the discussion of current challenges, examples from media, and value tensions will go.*
  
  A [2021 survey](https://www.adl.org/online-hate-2021) from the Anti-Defamation League found an increase in online hate & harassment directed at LGBTQ+, Asian American, Jewish, and African American individuals.
  Counterspeech vs. hate speech
  
  Example: "Only six percent of Arabic-language hate content was detected on Instagram before it made its way onto the photo-sharing platform owned by Facebook." from https://www.politico.com/news/2021/10/25/facebook-moderate-posts-violent-countries-517050 

  So what does all this mean for conceptualizing this real world problem as a machine learning task? First we'll look at the data, then at the models.
  """)
