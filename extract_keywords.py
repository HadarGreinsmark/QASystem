# Uses NLTK
import nltk
from nltk.corpus import stopwords

# Extract all the entities


def word_tokenize(tokens):
    return [token.replace("''", '"').replace("``", '"') for token in nltk.word_tokenize(tokens)]

def extract_keywords(mysent='Where was Albert Einstein born?'):
    word_tokenized = word_tokenize(mysent)

    # TODO: need to cache this so it isn't recomputed each time
    mystopwords = set(stopwords.words('english'))
    mystopwords.add(('who', 'what', 'where','when', 'why', 'how'))

    # Extract all named entities --------------------------
    tagged_sentence = nltk.pos_tag(word_tokenized)
    tree = nltk.ne_chunk(tagged_sentence)

    entities_in_sent = {}
    def _tree_iter(t):
        for subtree in t:
            if isinstance(subtree, nltk.tree.Tree):
                ent_name = ' '.join([x[0] for x in subtree.leaves()])
                entities_in_sent[ent_name] = subtree.label()

    _tree_iter(tree)

    entity_words = set()
    for k in entities_in_sent.keys():
        for w in k.split(' '):
            entity_words.add(w.lower())

    word_tokenized = [x.lower() for x in word_tokenized if x.isalpha()]
    nonbgwords = [x for x in word_tokenized if x not in mystopwords and x not in entity_words]

    return nonbgwords, entities_in_sent

if __name__ == '__main__':
    nbgw, entities = extract_keywords()