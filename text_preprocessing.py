# Day 2: Basic Text Preprocessing for ML

def clean_text_data(raw_text):
    lowercased_text = raw_text.lower()
    cleaned_text = lowercased_text.strip()
    return cleaned_text


dirty_data = "   HELLO Machine Learning WORLD!   "
ready_data = clean_text_data(dirty_data)

print("Original Data:", dirty_data)
print("Cleaned Data:", ready_data)
