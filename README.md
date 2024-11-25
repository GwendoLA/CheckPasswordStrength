# Password Strength Checker

A web application to assess password strength and provide suggestions for improvement.

## Overview

This application allows users to evaluate their passwords' strength based on security criteria such as length, use of uppercase letters, special characters, or the presence of common words. \
Additionally, it verifies that the password does not include the user's first or last name, a common security vulnerability. \
The application provides a rating, ranging from 'Very Weak' to 'Very Strong,' along with specific recommendations to strengthen weaker passwords.

## Installation and Setup

### Prerequisites

- Python 3.8 or later
- pip (to manage dependencies)

### Installation Steps

1. Clone this repository
2. Create and activate a virtual environment
3. Install dependencies:
   ``` pip install -r requirements.txt ```
4. Run the application:
   ``` python app.py ```
5. Open the app in your browser: http://127.0.0.1:5000

## Data Sources

The common English and French word lists used in this project are modified version of these lists:

- **English word list**: [https://gist.github.com/cofinley/262765821e4defbc8ff2bdb3356a853b#file-frequency-txt]
- **French word list**: [https://github.com/powerlanguage/word-lists/blob/master/1000-most-common-words.txt]

I removed words with less than three letters to better fit the project's requirements.
