# FakeOut - Instagram Account Analysis

## Overview
FakeOut is a tool that allows you to analyze Instagram user accounts to determine if they are legitimate or potentially associated with bot or spam activity. This tool provides insights into user account information, caption analysis, and bio coherence scoring.

## Usage Without Installation
You can also access the FakeOut website online without the need to install anything. Just click [here](https://fakeout-prototype-bjesc3mq6hmhyndxdl4r5t.streamlit.app/) to open the website and start analyzing Instagram accounts.

## Installation
1. Clone this repository to your local machine.
2. Create a virtual environment (recommended) and activate it.
3. Install the required dependencies using `pip` and the `requirements.txt` file: `pip install -r requirements.txt`

## Usage

### Running the Application
1. Ensure you have the necessary dependencies installed as mentioned in the Installation section.

2. Run the Streamlit application with the following command: `streamlit run app.py`

3. The application will open in your web browser. You can enter an Instagram username to analyze.

4. Choose from the following options:
- "Get User Info" to view basic user account information.
- "Bot Detection" to analyze the account for signs of bot or spam activity.
- "Account Type" to determine if the account is a Business, Private, or Verified account.
- "End Application" to exit the program.

## Dependencies

- [instagrapi](https://pypi.org/project/instagrapi/): Instagram Private API client.
- [openai](https://pypi.org/project/openai/): Python client for the OpenAI GPT-3 model.
- [numpy](https://pypi.org/project/numpy/): Numerical computing library.
- [pandas](https://pypi.org/project/pandas/): Data manipulation and analysis library.
- [scikit-learn](https://pypi.org/project/scikit-learn/): Machine learning library for classification.

Make sure to check and install the specific versions mentioned in the `requirements.txt` file.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
