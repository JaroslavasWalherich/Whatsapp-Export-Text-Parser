# Whatsapp-Export-Text-Parser
This Python script provides a versatile text cleaning tool for preprocessing text data. It allows you to perform various text cleaning operations on input text data, such as removing specific regex patterns, sentences, blank lines, emojis, and Arabic stopwords. The cleaned text can then be saved to an output file.


Text Cleaner Documentation
Overview

The Text Cleaner is a Python script designed to preprocess text data by removing specified patterns, sentences, blank lines, emojis, and Arabic stopwords. This documentation provides step-by-step instructions on how to use the script effectively.
Getting Started
Prerequisites

Before using the Text Cleaner script, make sure you have the following dependencies installed:

    Python 3.x
    NLTK library (for Arabic stopwords)

You can install NLTK using pip:

bash

pip install nltk

Setup

    Clone or download the Text Cleaner repository from GitHub.

    Place your input text file (input.txt) in the same directory as the script.

    Define the patterns you want to remove in a text file named patterns.txt. Each line in this file should contain a regex pattern.

    Define the sentences you want to delete in a text file named sentences.txt. Each line in this file should contain a sentence you wish to remove.

Running the Script

To use the Text Cleaner script, follow these steps:

    Open a terminal or command prompt.

    Navigate to the directory containing the Text Cleaner script and input files.

    Run the script using the following command:

bash

python text_cleaner.py

    The script will process the input text according to the specified cleaning operations.

    Once the processing is complete, the cleaned text will be saved to an output text file named output.txt in the same directory.

Customization

You can customize the cleaning operations by modifying the TextCleaner class methods in the text_cleaner.py script. You can add or remove cleaning steps based on your specific text preprocessing needs.
Example Usage

Here's an example of how to use the Text Cleaner:

Suppose you have an input.txt file with the following text:

sql

This is an example text. It contains some unwanted patterns.

Unwanted sentences should be removed. This is one of them.

Some lines are empty.

😀 This is an emoji. It should be removed.

إنها نصة باللغة العربية.

This text also contains Arabic stopwords that need to be removed.

    You have patterns.txt with the following regex pattern to remove:

unwanted

You have sentences.txt with the following sentence to delete:

csharp

    Unwanted sentences should be removed. This is one of them.

    The script will perform the following cleaning operations:
        Remove the specified regex pattern: unwanted
        Delete the specified sentence: Unwanted sentences should be removed. This is one of them.
        Remove empty lines
        Convert the text to lowercase
        Remove emojis
        Remove Arabic stopwords

After running the script, the cleaned text will be saved to output.txt:

kotlin

this is an example text. it contains some  patterns.
some lines are empty.
إنها نصة العربية.
this text contains arabic stopwords  removed.

Conclusion

The Text Cleaner script provides a flexible and customizable way to preprocess text data for various natural language processing (NLP) tasks. By defining the patterns, sentences, and cleaning steps, you can tailor it to your specific text cleaning needs.

Feel free to use, modify, and extend the Text Cleaner script to suit your project requirements.
