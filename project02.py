import numpy as np


"""
1. **Creativity:**
   - Innovative thinking and generating original ideas.

2. **Communication Skills:**
   - Effectively conveying information verbally, in writing, or non-verbally.

3. **Logical Skills:**
   - Critical thinking, deductive reasoning, and sound judgment.

4. **Analytical Skills:**
   - Ability to analyze information, solve problems, and make logical decisions.

5. **Adaptability:**
   - Flexibility and ability to adjust to new situations or changes.

6. **Repetition (Organizational/Repetitive Skills):**
   - Performing routine task regularly and consistency
"""

# Define vectors for different categories
STEM_vector = np.array([0, 0, 1, 0.5, 1, 0])  
Business_vector = np.array([0, 0, 0, 1, 0, 1])  
Healthcare_vector = np.array([0, 0.5, 1, 0, 0, 1])  
Education_vector = np.array([0.5, 1, 0, 0, 1, 0])  
Social_Services_vector = np.array([1, 1, 0, 0, 0.5, 0.5]) 
Arts_and_Humanities_vector = np.array([1, 1, 1, 0, 0, 0])  
#input_vector = [1, 1, 0, 1, 0, 1]   
# Create a list of all vectors
vectors = [
    STEM_vector,
    Business_vector,
    Healthcare_vector,
    Education_vector,
    Social_Services_vector,
    Arts_and_Humanities_vector
]
vector_names = [
    'STEM',
    'Business',
    'Healthcare',
    'Education',
    'Social Services',
    'Arts and Humanities'
]

# questions = ['Does it often happen that the solution you have found is diffrent from the solutions of everyone else?',
#             'Can you recall a situation where you successfully conveyed a complex idea to someone with different background knowledge, ensuring their understanding?',
#             'When faced with a challenging problem, do you systematically break it down into smaller components to analyze each part rather than working at it as a whole?',
#             'Do you find it easy to work with numbers and statistics rather than words',
#             'Is it easier for you to learn about many skills rather than foucusing and improving on one',
#             'Are you consistent in performing routine tasks, ensuring accuracy and reliability in your work?']
# input_vector = []
# print(' \n \n ANSWER IN (no/yes/idk)')
# for x in range(len(questions)):
#     val = input(questions[x] + ': ')
#     if val == 'yes':
#         input_vector.append(1)
#     elif val == 'no':
#         input_vector.append(0)        
#     else:
#         input_vector.append(0.5)


def career(input_vector):
    product = {}
    for x in range(0, 6):
        dot_product = (np.dot(input_vector, vectors[x]) )
        product[vector_names[x]] = dot_product
        


    max_value = max(product, key=product.get)
    return(max_value)



