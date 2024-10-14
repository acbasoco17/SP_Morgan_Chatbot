import csv
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

def create_vector_database():
    # Load pre-trained model
    model = SentenceTransformer('all-MiniLM-L6-v2')

    # Read scraped data
    texts = []
    with open('morgan_edu_data2.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            texts.append(row[0])

    # Create embeddings
    embeddings = model.encode(texts)

    # Create FAISS index
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings.astype('float32'))


    # Save index and texts
    faiss.write_index(index, "morgan_edu_index.faiss")
    np.save("morgan_edu_texts.npy", texts)
    print("VectorDB is created")

create_vector_database() 