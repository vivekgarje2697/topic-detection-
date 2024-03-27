import tkinter as tk
from textblob import TextBlob

def identify_topic():
    text = text_input.get("1.0", "end-1c")
    blob = TextBlob(text)
    topic = None
    topic_freq = 0
    
    # Count the frequency of each noun and adjective in the text
    word_freq = {}
    for word, pos in blob.pos_tags:
        if pos.startswith('NN') or pos.startswith('JJ'):
            word = word.lower()
            word_freq[word] = word_freq.get(word, 0) + 1
    
    # Find the most frequent noun or adjective
    for word, freq in word_freq.items():
        if freq > topic_freq:
            topic = word
            topic_freq = freq
    
    if topic is not None:
        topic_label.config(text="Topic: " + topic)
    else:
        topic_label.config(text="No topic identified")

root = tk.Tk()
root.title("Topic Detector")

text_label = tk.Label(root, text="Enter your text:")
text_label.pack()

text_input = tk.Text(root, height=10)
text_input.pack()

detect_button = tk.Button(root, text="Detect Topic", command=identify_topic)
detect_button.pack()

topic_label = tk.Label(root, text="")
topic_label.pack()

root.mainloop()
