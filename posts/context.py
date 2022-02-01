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

  # Current Challenges

  This is where the discussion of current challenges, examples from media, and value tensions will go.

  So what does all this mean for conceptualizing this real world problem as a machine learning task? First we'll look at the data, then at the models.
  """)
