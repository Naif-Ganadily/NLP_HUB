import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances
from math import exp

# Jaccard similarity function
def jaccard_similarity(x, y):
    """ Returns the Jaccard similarity between two lists """
    intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
    union_cardinality = len(set.union(*[set(x), set(y)]))
    return intersection_cardinality / float(union_cardinality)

# Distance to similarity function
def distance_to_similarity(distance):
    return 1 / exp(distance)

st.title("Text Similarity with Various Metrics")
st.markdown("""
## Text Similarity Page

This page allows you to input two sentences, select a similarity metric, and view the calculated similarity. The available metrics include Jaccard similarity, Euclidean distance-based similarity, and Cosine similarity. We also provide mathematical explanations for each metric.
""")

# Text input
sentence1 = st.text_area("Enter the first sentence:", "McDonald's is unhealthy because it has processed food.", key="sentence1")
sentence2 = st.text_area("Enter the second sentence:", "Denny's is unhealthy because it has processed food.", key="sentence2")

# Similarity metric selection
metric = st.selectbox("Choose a similarity metric:", ["Jaccard Similarity", "Euclidean Distance-based Similarity", "Cosine Similarity"])

# Submit button
if st.button('Calculate Similarity'):
    if sentence1 and sentence2:
        st.subheader(f"Similarity Calculation using {metric}")
        
        if metric == "Jaccard Similarity":
            # Calculate Jaccard similarity
            tokens1 = sentence1.lower().split()
            tokens2 = sentence2.lower().split()
            similarity = jaccard_similarity(tokens1, tokens2)
            st.write(f"Jaccard Similarity: {similarity:.4f}")
            
            # Mathematical explanation
            st.subheader("Mathematical Explanation")
            st.markdown("""
            ### Jaccard Similarity
            The Jaccard similarity coefficient is defined as the size of the intersection divided by the size of the union of two sets:
            """)
            st.latex(r'''
            J(A, B) = \frac{|A \cap B|}{|A \cup B|}
            ''')
            st.markdown("""
            Where \(A\) and \(B\) are sets of words from the two sentences.
            """)

        elif metric == "Euclidean Distance-based Similarity":
            # Calculate Euclidean distance-based similarity
            vectorizer = TfidfVectorizer().fit_transform([sentence1, sentence2])
            vectors = vectorizer.toarray()
            distance = euclidean_distances(vectors[0].reshape(1, -1), vectors[1].reshape(1, -1))[0][0]
            similarity = distance_to_similarity(distance)
            st.write(f"Euclidean Distance-based Similarity: {similarity:.4f}")
            
            # Mathematical explanation
            st.subheader("Mathematical Explanation")
            st.markdown("""
            ### Euclidean Distance-based Similarity
            The Euclidean distance between two points in space is given by:
            """)
            st.latex(r'''
            d(x, y) = \sqrt{\sum_{i=1}^{n} (x_i - y_i)^2}
            ''')
            st.markdown("""
            We convert this distance to a similarity score using the exponential function:
            """)
            st.latex(r'''
            S = \frac{1}{e^d}
            ''')

        elif metric == "Cosine Similarity":
            # Calculate Cosine similarity
            vectorizer = TfidfVectorizer().fit_transform([sentence1, sentence2])
            vectors = vectorizer.toarray()
            cosine_sim = cosine_similarity(vectors[0].reshape(1, -1), vectors[1].reshape(1, -1))[0][0]
            st.write(f"Cosine Similarity: {cosine_sim:.4f}")
            
            # Mathematical explanation
            st.subheader("Mathematical Explanation")
            st.markdown("""
            ### Cosine Similarity
            The Cosine similarity between two vectors is given by the dot product divided by the product of the magnitudes of the vectors:
            """)
            st.latex(r'''
            \cos(\theta) = \frac{A \cdot B}{\|A\| \|B\|}
            ''')
            st.markdown("""
            Where \(A\) and \(B\) are the vector representations of the sentences.
            """)

st.markdown("""
### Summary
Text similarity measures are essential in NLP for tasks such as document clustering, information retrieval, and more. The metrics showcased here—Jaccard Similarity, Euclidean Distance-based Similarity, and Cosine Similarity—each have unique strengths and mathematical foundations.
""")