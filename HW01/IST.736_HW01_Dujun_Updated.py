# %%
# ist736 text mining hw_1 - lexicon-based text analysis
# dujun zhai

# task 1 - Use this lexicon to find the top three social relationships mentioned in happy moments

# problem solving logic:
# - use a predefined people dictionary to extract social relationships from happy moments
# - count occurrences of each relationship
# - identify the top 3 relationships mentioned the most


# step 1: import necessary libraries
# ================================

import pandas as pd  # pandas for handling csv data


# step 2: load datasets (local files)
# ================================

# happy moments dataset, contains user-written happy experiences
happydb_path = "cleaned_hm.csv"
happydb = pd.read_csv(happydb_path)

# people dictionary, contains relationship-related words
people_dict_path = "people-dict.csv"
people_dict = pd.read_csv(people_dict_path, header=None)  # ensuring first row is treated as data

# manually rename column for clarity
people_dict.columns = ['relationship']


# step 3: verify data structure
# ================================

# print sample rows, ensure correct format and content
print("happydb sample:", happydb.head(), "\n")  
print("people dictionary sample:", people_dict.head(), "\n")  

# expected structure:
# - happydb should have a column with text-based happy moments
# - people dictionary should have a column with relationship words


# step 4: extract relationship words
# ================================

# get unique relationship words from people dictionary
relationship_words = people_dict['relationship'].unique()  

# expected output:
# - list of relationship-related terms that will be used for searching


# step 5: process text, count mentions
# ================================

# initialize dictionary, store counts of each relationship word
relationship_counts = {word: 0 for word in relationship_words}

# loop through happy moments, count occurrences of relationship words
for moment in happydb['cleaned_hm']:
    moment_lower = moment.lower()  # normalize text, lowercase for matching
    for word in relationship_words:
        if word in moment_lower:  # check if relationship appears in text
            relationship_counts[word] += 1  # update count

# expected outcome:
# - dictionary with counts for each relationship term


# step 6: rank relationships
# ================================

# sort by frequency, highest to lowest
sorted_relationships = sorted(relationship_counts.items(), key=lambda x: x[1], reverse=True)

# extract top 3 relationships
top_3_relationships = sorted_relationships[:3]


# step 7: output results
# ================================

print("top 3 relationships mentioned in happy moments:", top_3_relationships)



# additional notes

# key findings
# ================================
# - top 3: 'friend' (13,419), 'men' (7,038), 'son' (6,274)
# - 'friend' shows up the most, makes sense, social ties matter
# - 'men' is high, kinda unexpected, maybe some context issue
# - family terms pop up a lot, happiness often tied to close people

# data issue & fix
# ================================
# - problem: 'category' column was missing, couldn’t access words
# - fix: renamed it to 'relationship', works fine now
# - double-checked structure before running, avoids errors




# KEY ai-assisted part: accessing csv files from github
# ================================
# ai prompt used:
# "how to load a csv file from github using python?"
# ai provided methods like using pandas' read_csv() with the raw github url.
# also helped me upload the file to the cloud workspace and access it directly via url instead of locally.
# learned how to efficiently manage and process datasets in both local and remote environments




# %%
# ist736 text mining hw_1  
# dujun zhai
# task 2 - assess strengths and weaknesses of the people dictionary

# problem solving logic
# ================================

#  question: does the  dictionary really capture "who people spend happy moments with?"

# "people" means: family, friends, coworkers, social groups
# strengths: structured list, easy for text analysis
# weaknesses(potential): may miss casual words, some terms too vague or broad

#  action plan- 
#  check for missing, duplicate, or misleading words
#  flag vague terms that might distort results
#  suggest better words for accuracy


import pandas as pd  # pandas for handling csv data

# step 2: load people dictionary
# ================================

people_dict_path = "people-dict.csv"
people_dict = pd.read_csv(people_dict_path, header=None)  # ensuring first row is treated as data

# manually rename column for clarity
people_dict.columns = ['relationship']

# step 3: check for duplicates or empty values
# ================================

# find duplicate words
duplicate_words = people_dict['relationship'].duplicated().sum()

# find empty or missing values
missing_values = people_dict['relationship'].isnull().sum()

# print findings
print("duplicate words in dictionary:", duplicate_words)
print("missing values in dictionary:", missing_values)

# reasoning:
# - duplicate words can distort counts, need to track if they exist
# - missing values mean gaps in dictionary coverage, need to be fixed

# step 4: analyze word types
# ================================

# common words that may cause ambiguity
ambiguous_words = ['men', 'women', 'people', 'human', 'kids']

#  how many ambiguous words exist in dictionary
ambiguous_count = people_dict[people_dict['relationship'].isin(ambiguous_words)].shape[0]

#  results
print("potentially ambiguous words:", ambiguous_words)
print("count of ambiguous words found in dictionary:", ambiguous_count)

# reasoning
# - words like "men" or "people" may appear in contexts that are not relationship-based
# - identifying ambiguous words helps refine dictionary accuracy

# step 5: suggest improvements
# ================================

# words to add for better coverage
suggested_additions = ['bestie', 'roommate', 'teammate', 'partner']

# print suggestions
print("suggested additions to improve dictionary:", suggested_additions)

# reasoning
# - missing key social roles like "bestie" (friend), "partner" (modern relationships)
# - adding workplace/social roles like "teammate" improves context coverage




# KEY ai-assisted part: identifying ambiguous words
# ================================
# ai prompt used:
# "find words in the people dictionary that might not clearly represent a relationship."
# ai flagged vague words like 'men' and 'people' that could distort results,
# so i removed them to improve accuracy.
# learned how to refine dictionaries by filtering unclear terms.






# %%
# ist736 text mining hw_1  
# dujun zhai  
# task 3 - improving the people dictionary and redoing task 1  

# step 1: fix issues in the people dictionary  
# =============================================  
# ensure the dictionary captures relevant social relationships, 
# remove vague, duplicate, or misleading terms

# import necessary library
import pandas as pd  

# load the original people dictionary
people_dict_path = "people-dict.csv"  
people_dict = pd.read_csv(people_dict_path, header=None)  # treat first row as data

# rename column for clarity
people_dict.columns = ['relationship']  

# check for duplicates and missing values
duplicate_words = people_dict['relationship'].duplicated().sum()
missing_values = people_dict['relationship'].isnull().sum()

print("duplicate words in dictionary:", duplicate_words)  
print("missing values in dictionary:", missing_values)  

# step 2: identify and remove vague terms  
# =============================================  
# remove words that are broad or contextually unclear
ambiguous_words = ['men', 'women', 'people', 'human', 'kids']  
ambiguous_count = people_dict[people_dict['relationship'].isin(ambiguous_words)].shape[0]

print("potentially ambiguous words:", ambiguous_words)  
print("count of ambiguous words found in dictionary:", ambiguous_count)  

# step 3: improve dictionary by adding better terms  
# ==================================================  
# add missing relationship-specific words
suggested_additions = ['bestie', 'roommate', 'teammate', 'partner']  
print("suggested additions to improve dictionary:", suggested_additions)  

# update dictionary by removing ambiguous words and adding better ones
updated_dict = people_dict[~people_dict['relationship'].isin(ambiguous_words)]  # remove vague terms
updated_dict = pd.concat([updated_dict, pd.DataFrame(suggested_additions, columns=['relationship'])], ignore_index=True)  

# save updated dictionary
updated_dict.to_csv("updated_people_dict.csv", index=False)  
print("updated people dictionary saved as updated_people_dict.csv")  

# step 4: redo task 1 using the improved dictionary  
# ==================================================  
# analyze happy moments with the revised dictionary

# load happy moments data
happy_moments_path = "cleaned_hm.csv"  
happy_moments = pd.read_csv(happy_moments_path)  

# check if required column exists
if 'cleaned_hm' not in happy_moments.columns:  
    print("error: expected column 'cleaned_hm' not found in happy moments data")  
else:  
    # extract relationship words from updated dictionary
    relationship_words = updated_dict['relationship'].tolist()
    
    # count relationship mentions in happy moments
    from collections import Counter  
    word_count = Counter()  
    
    for text in happy_moments['cleaned_hm']:  # process each happy moment
        words = text.lower().split()  # convert to lowercase and split into words
        for word in words:
            if word in relationship_words:  # check if word matches dictionary
                word_count[word] += 1  # increment count
    
    # get top 3 most mentioned relationships
    top_relationships = word_count.most_common(3)  
    print("top 3 relationships mentioned in happy moments:", top_relationships)  
    
    # findings depend on script execution results



# additional notes  
# =========================  
# findings: top relationships in happy moments are ('friend', 4918), ('family', 3546), ('friends', 3338)
# confirming the importance of close personal connections
# coding issue: encountered an 'AttributeError' due to deprecated 'append()' method  
# resolved by replacing it with 'pd.concat()', ensuring compatibility with newer pandas versions

# KEY ai-assisted part: fixing pandas append() issue
# ================================
# ai prompt used:
# "pandas throws an AttributeError when using .append(). What is the correct method?"
# ai suggested using pd.concat() since .append() is deprecated.
# learned how to update pandas methods for better compatibility.


# KEY ai-assisted part: optimizing filtering process
# ================================
# ai prompt used:
# "how can i efficiently filter out specific words in pandas?"
# ai suggested using .isin() instead of manually looping through rows, making things way faster
# learned how to let pandas do the heavy duty and keep my code clean/efficient


 


# %%
# ist736 text mining hw_1  
# dujun zhai  
# task 4 - extracting and analyzing context words  

 # problem solving logic
# ================================
#  goal - find what words show up around the top mentioned relationships  
#  focus - extract five words before and after each mention   
#  method - count and sort context words to see patterns  
#  outcome - check if certain activities or emotions appear often  

# step 1: import libraries  
# ================================  

import pandas as pd  
from collections import Counter  
import re  

# manually defining stopwords as nltk stopwords are unavailable in this environment  
stop_words = set("i me my myself we our ours ourselves you your yours yourself yourselves he him his himself she her hers herself it its itself they them their theirs themselves what which who whom this that these those am is are was were be been being have has had having do does did doing a an the and but if or because as until while of at by for with about against between into through during before after above below to from up down in out on off over under again further then once here there when where why how all any both each few more most other some such no nor not only own same so than too very s t can will just don should now d ll m o re ve y ain aren couldn didn doesn hadn hasn haven isn mightn mustn needn shan shouldn wasn weren won wouldn".split())  

# step 2: load data  
# ================================  

# happy moments dataset, contains descriptions of happy events  
happy_moments_path = "cleaned_hm.csv"  
happy_moments = pd.read_csv(happy_moments_path)  

# make sure the required column is there  
if 'cleaned_hm' not in happy_moments.columns:  
    print("error: expected column 'cleaned_hm' not found")  
    exit()  

# get the top 3 most mentioned relationships (from task 1)  
top_relationships = ['friend', 'men', 'son']  

# step 3: context words  
# ================================  

# store words appearing before and after relationship mentions  
context_words = []  

# process each happy moment  
for text in happy_moments['cleaned_hm']:  
    words = re.findall(r'\b\w+\b', text.lower())  # split text into words, remove punctuation  
    words = [word for word in words if word not in stop_words]  # removing stopwords manually  
    for i, word in enumerate(words):  
        if word in top_relationships:  # check if word is one of our target relationships  
            before = words[max(0, i-5):i]  # get up to 5 words before  
            after = words[i+1:i+6]  # get up to 5 words after  
            context_words.extend(before + after)  # add to the list  

# reasoning:  
#  checking words before/after shows how people describe these relationships  [correlated] 
#  manually removing stopwords ensures we focus on meaningful context  

# step 4: count and sort context words  
# ================================  

word_freq = Counter(context_words)  # count how often each context word appears  
top_100_words = word_freq.most_common(100)  # get the 100 most common words  

# reasoning
# sorting by frequency helps spot trends  


# step 5: output results  
# ================================  

print("top 100 most frequent context words:", top_100_words)  



# step 6: findings (based on execution results)  
# ================================  
# key insights from the top 100 words:  
#  frequent verbs ('got', 'made', 'went', 'see', 'gave', 'met') suggest shared activities  
#  emotional words ('happy', 'best', 'great', 'love', 'fun', 'enjoyed') suggest positive interactions  
#  event-related words ('birthday', 'party', 'wedding', 'dinner', 'visit', 'game') suggest social occasions  
#  time-related words ('yesterday', 'years', 'months', 'week', 'day', 'night') suggest reflection on past events  


# next steps
# analyze how context words and relationships co-occur
# try word frequency visualizations for deeper analysis

# KEY ai-assisted part: fixing nltk module not found error  
# ================================  
# ai prompt used:  
# "how do i fix ModuleNotFoundError: No module named 'nltk' in python?"  
# ai recommended using a custom stopword list instead of nltk's  
# updated script to remove nltk dependency for stability  
# learned how to handle stopwords manually and avoid external module issues  
# tested to ensure the script runs smoothly without nltk  

# KEY ai-assisted part: improving sorting efficiency  
# ================================  
# ai prompt used:  
# "how do i efficiently count and sort word frequency in python?"  
# ai suggested using collections.Counter instead of manually iterating, making it much faster  
# learned how to leverage built-in libraries for optimized word frequency analysis  

# KEY ai-assisted part: refining text cleaning process  
# ================================  
# ai prompt used:  
# "how can i improve the accuracy of context word extraction in text mining?"  
# ai suggested applying lemmatization to standardize word forms and filtering stopwords to remove noise  
# learned how to manually define stopwords to ensure processing is environment-independent  



