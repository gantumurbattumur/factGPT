with open('documents.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    
print("length of dataset characters:", len(text))