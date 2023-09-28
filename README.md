
# Whatsapp-Export-Text-Parser
This Python script provides a versatile text cleaning tool for preprocessing text data. It allows you to perform various text cleaning operations on input text data, such as removing specific regex patterns, sentences, blank lines, emojis, and Arabic stopwords. The cleaned text can then be saved to an output file.

## Overview

The Text Cleaner is a Python script designed to preprocess text data by removing specified patterns, sentences, blank lines, emojis, and Arabic stopwords. This documentation provides step-by-step instructions on how to use the script effectively.

## Getting Started

### Prerequisites

#### Before using the Text Cleaner script, make sure you have the following dependencies installed:

    Python 3.x
    NLTK library (for Arabic stopwords)

You can install NLTK using pip:

    pip install nltk
    pip install pandas

## Setup

    

Clone or download the Text Cleaner repository from GitHub.

 1. Place your input text file (input.txt) in the same directory as the
    script.
 2. Define the patterns you want to remove using regex in a text file named
    patterns.txt.
 3. Each line in this file should contain a regex pattern.
 4. Define the sentences you want to delete in a text file named
    sentences.txt.

Each line in this file should contain a sentence you wish to remove.

## Running the Script

To use the Text Cleaner script, follow these steps:

Run the script using the following command:


    python text_cleaner.py

The script will process the input text according to the specified cleaning operations.
Once the processing is complete, the cleaned text will be saved to an output text file named output.csv the same directory.

## Example Usage

Here's an example of how to use the Text Cleaner:

Suppose you have an input.txt file with the following text:

This is an example text. It contains some unwanted patterns.

    Unwanted sentences should be removed. This is one of them.
    
    Some lines are empty.
    
    😀 This is an emoji. It should be removed.
    
    إنها نصة باللغة العربية.
    
    This text also contains Arabic stopwords that need to be removed.

You have **patterns.txt** with the following regex pattern to remove:

    Unwanted

You have **sentences.txt** with the following sentence to delete

    Unwanted sentences should be removed. This is one of them.

 - The script will perform the following cleaning operations:
           Remove the specified regex pattern: **unwanted**
           Delete the specified sentence: **Unwanted sentences should be removed. This is one of them.
           Remove empty lines**
           Convert the text to lowercase
           Remove emojis
           Remove Arabic stopwords

After running the script, the cleaned text will be saved to **output.txt**:

    this is an example text. it contains some  patterns.
    some lines are empty.
    إنها نصة العربية.
    this text contains arabic stopwords  removed.

## Conclusion

The Text Cleaner script provides a flexible and customizable way to preprocess text data for various natural language processing (NLP) tasks. By defining the patterns, sentences, and cleaning steps, you can tailor it to your specific text cleaning needs.

Feel free to use, modify, and extend the Text Cleaner script to suit your project requirements.


This code is not perfect but it got the job done for me
