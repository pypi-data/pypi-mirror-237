import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import demoji
import joblib

nltk.download('stopwords')
nltk.download('punkt')

class TextPreprocessor:
    def __init__(self):
        demoji.download_codes()
    def clean_text(self, text):
        if not isinstance(text, str):
            return text

        # Convert text to lowercase
        text = text.lower()

        # Remove emojis and stickers
        text = demoji.replace(text, '')

        # Remove punctuation and special characters
        text = re.sub(r'[^\w\s]', '', text)

        # Tokenize text
        tokens = word_tokenize(text)

        # Remove stop words
        stop_words = set(stopwords.words('english'))
        tokens = [token for token in tokens if token not in stop_words]

        # Apply stemming
        stemmer = PorterStemmer()
        tokens = [stemmer.stem(token) for token in tokens]

        # Rejoin the tokens into a single string
        text = ' '.join(tokens)

        return text
    
    def preprocess_dataframe(self, df, column_name):
        if column_name not in df.columns:
            raise ValueError(f"Column '{column_name}' not found in the DataFrame.")

        
        df[column_name] = df[column_name].apply(self.clean_text)

        return df