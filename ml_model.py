import json
import random
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import streamlit as st

def train_and_predict_knn(user_information):

    with open("fakeAccountData.json", "r") as f:
        fake_data = json.load(f)

    numeric_fake_data = []
    for entry in fake_data:
        numbers = [value for key, value in entry.items() if isinstance(value, int)]
        numeric_fake_data.append(numbers)

    with open("realAccountData.json", "r") as f:
        real_data = json.load(f)

    numeric_real_data = []
    for entry in real_data:
        numbers = [value for key, value in entry.items() if isinstance(value, int)]
        numeric_real_data.append(numbers)

    database = numeric_real_data + numeric_fake_data
    random.shuffle(database)

    data = np.array(database)

    user_data = pd.DataFrame(data, columns=["Followers", "Following", "biolength", "posts", "isProfilePic", "IsPrivate", "usernameDigitCount", "usernameLength", "isFake"])

    input_data = user_data[["Followers", "Following", "biolength", "posts", "IsPrivate", "usernameDigitCount", "usernameLength"]]
    target = user_data["isFake"]

    # Train the KNN classifier
    classifier = KNeighborsClassifier(n_neighbors=4)
    classifier.fit(input_data, target)

    # Make predictions on the input data
    user_information = user_information.reshape(1, -1)
    predictions = classifier.predict(user_information)
    print(predictions)
    if predictions>=0.5:
        if predictions==1:
            st.text("Fake Account.\n")
        else:
            st.text("Likely Fake.\n")
    elif predictions==0:
        st.text("Legitimate account.\n")
    else:
        st.text("Likely legitimate.\n")

