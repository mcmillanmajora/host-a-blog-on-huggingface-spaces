import streamlit as st

# from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import pipeline

title = "Model Exploration"
description = "Comparison of hate speech detection models"
date = "2022-01-26"
thumbnail = "images/huggingface_logo.png"


# Creates the forms for receiving multiple inputs to compare for a single 
# model or one input to compare for two models
def run_article():
    st.markdown("""
    # Making a Hate Speech Detection Model

    Once the data has been collected using the definitions identified for the 
    task, you can start training your model. At training, the model takes in 
    the data with labels and learns the associated context in the input data 
    for each label. Depending on the task design, the labels may be binary like 
    'hateful' and 'non-hateful' or multiclass like 'neutral', 'offensive', and 
    'attack'. 
    
    When presented with a new input string, the model then predicts the 
    likelihood that the input is classified as each of the available labels and
    returns the label with the highest likelihood as well as how confident the 
    model is in its selection using a score from 0 to 1. 
    
    Neural models such as transformers are frequently trained as general 
    language models and then fine-tuned on specific classification tasks.
    These models can vary in their architecture and the optimization 
    algorithms, sometimes resulting in very different output for the same 
    input text. 

    # Model Output Ranking

    For now, here's a link to the [space](https://huggingface.co/spaces/aymm/ModelOutputRankingTool).""")
    with st.expander("Model Output Ranking Tool", expanded=False):     
        with st.form(key='ranking'):
            model_name = st.selectbox("Select a model to test",
                   ["classla/roberta-base-frenk-hate",
                    "cardiffnlp/twitter-roberta-base-hate",
                    "Hate-speech-CNERG/dehatebert-mono-english"],
                    key="rank_model_select"
                    )

            # the placeholder key functionality was added in v1.2 of streamlit
            # and versions on Spaces currently goesup to v1.0
            input_1 = st.text_input("Input 1",
                                    #placeholder="We shouldn't let [IDENTITY] suffer.",
                                    help= "Try a phrase like 'We shouldn't let [IDENTITY] suffer.'",
                                    key="rank_input_1")
            input_2 = st.text_input("Input 2",
                                    #placeholder="I'd rather die than date [IDENTITY].",
                                    help= "Try a phrase like 'I'd rather die than date [IDENTITY].'",
                                    key="rank_input_2")
            input_3 = st.text_input("Input 3",
                                    #placeholder="Good morning.",
                                    help= "Try a phrase like 'Good morning'",
                                    key="rank_input_3")
            inputs = [input_1, input_2, input_3]

            if st.form_submit_button(label="Rank inputs"):
                results = run_ranked(model_name, inputs)
                st.dataframe(results)
        
      
      
    st.markdown("""
    # Model Comparison

    For now, here's a link to the [space](https://huggingface.co/spaces/aymm/ModelComparisonTool).
    """)
    with st.expander("Model Comparison Tool", expanded=False): 
        with st.form(key='comparison'):
            model_name_1 = st.selectbox("Select a model to compare",
                               ["cardiffnlp/twitter-roberta-base-hate",
                                "Hate-speech-CNERG/dehatebert-mono-english",
                                ],
                                key='compare_model_1'
                                )
            model_name_2 = st.selectbox("Select another model to compare",
                               ["cardiffnlp/twitter-roberta-base-hate",
                                "Hate-speech-CNERG/dehatebert-mono-english",
                                ],
                                key='compare_model_2'
                                )
            input_text = st.text_input("Comparison input",
                                       key="compare_input")
            if st.form_submit_button(label="Compare models"):
                results = run_compare(model_name_1, model_name_2, input_text)
                st.dataframe(results)
                
        
# Runs the received input strings through the given model and returns the 
# output ranked by label and score (does not assume binary labels so the 
# highest score for each label is at the top)
def run_ranked(model, input_list):
    classifier = pipeline("text-classification", model=model)
    output = []
    labels = {}
    for inputx in input_list:
        result = classifier(inputx)
        curr = {}
        curr['Input'] = inputx
        label = result[0]['label']
        curr['Label'] = label
        score = result[0]['score']
        curr['Score'] = score
        if label in labels:
            labels[label].append(curr)
        else:
            labels[label] = [curr]
    for label in labels:
        sort_list = sorted(labels[label], key=lambda item:item['Score'], reverse=True)
        output += sort_list
    return output


# Takes in two model names and returns the output of both models for that 
# given input string
def run_compare(name_1, name_2, text):
    classifier_1 = pipeline("text-classification", model=name_1)
    result_1 = classifier_1(text)
    out_1 = {}
    out_1['Model'] = name_1
    out_1['Label'] = result_1[0]['label']
    out_1['Score'] = result_1[0]['score']
    classifier_2 = pipeline("text-classification", model=name_2)
    result_2 = classifier_2(text)
    out_2 = {}
    out_2['Model'] = name_2
    out_2['Label'] = result_2[0]['label']
    out_2['Score'] = result_2[0]['score']
    return [out_1, out_2]
    

def main():
    run_article()
    
main()
    