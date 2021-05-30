import spacy
import random

# Example of training data. For me, I am training a spaCy model to do NER task. 
TRAIN_DATA = 
[
('Amazon co ca', {'entities': [(0, 6, 'BRD')]}),
('AMZNMKTPLACE AMAZON CO', {'entities': [(13, 19, 'BRD')]}),
('APPLE COM BILL', {'entities': [(0, 5, 'BRD')]}),
('BOOKING COM New York City', {'entities': [(0, 7, 'BRD')]}),
('STARBUCKS Vancouver', {'entities': [(0, 9, 'BRD')]}),
('Uber BV', {'entities': [(0, 4, 'BRD')]}),
('Hotel on Booking com Toronto', {'entities': [(9, 16, 'BRD')]}),
('UBER com', {'entities': [(0, 4, 'BRD')]}),
('Netflix com', {'entities': [(0, 7, 'BRD')]})]
]

# Function code is cited from the article: https://manivannan-ai.medium.com/how-to-train-ner-with-custom-training-data-using-spacy-188e0e508c6
def train_spacy(data,iterations):
    TRAIN_DATA = data
    nlp = spacy.blank('en')  # create blank Language class
    # create the built-in pipeline components and add them to the pipeline
    # nlp.create_pipe works for built-ins that are registered with spaCy
    if 'ner' not in nlp.pipe_names:
        ner = nlp.create_pipe('ner')
        nlp.add_pipe(ner, last=True)
       

    # add labels
    for _, annotations in TRAIN_DATA:
         for ent in annotations.get('entities'):
            ner.add_label(ent[2])

    # get names of other pipes to disable them during training
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
    with nlp.disable_pipes(*other_pipes):  # only train NER
        optimizer = nlp.begin_training()
        for itn in range(iterations):
            print("Statring iteration " + str(itn))
            random.shuffle(TRAIN_DATA)
            losses = {}
            for text, annotations in TRAIN_DATA:
                nlp.update(
                    [text],  # batch of texts
                    [annotations],  # batch of annotations
                    drop=0.2,  # dropout - make it harder to memorise data
                    sgd=optimizer,  # callable to update weights
                    losses=losses)
            print(losses)
    return nlp


prdnlp = train_spacy(TRAIN_DATA, 20)

# Save our trained Model
modelfile = input("Enter your Model Name: ")
prdnlp.to_disk(modelfile)

#Test your text
test_text = input("Enter your testing text: ")
doc = prdnlp(test_text)
for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)
