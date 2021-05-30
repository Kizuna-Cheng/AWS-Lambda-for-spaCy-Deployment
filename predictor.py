def predict(cls, test_data):

    	  # Character cleaning function that replace a certain set of special characters with spaces
        def char_clean(string): 
            new_string = re.sub('[^a-zA-Z0-9&+@ \n\.]', ' ', string)
            new_string = ' '.join(new_string.split())
            return new_string
        
        # Input dataframe as test_data. 
        df = test_data
        Prediction = []
        Source = []
        
        # Loop through each row of the input dataframe. 
        for index, row in df.iterrows(): 
            source = row.test_data_column_name 
            cleaned_source = char_clean(source)
            doc = prdnlp(cleaned_source)
            if doc.ents:  
                prediction = [ent.text for ent in doc.ents]
                Prediction.append(prediction) # An array of predicted merchant names. 
                Source.append(source) # An array of source merchant descriptions.
            else:
                # None entity detected
                Prediction.append(source)
                Source.append(source)
        
        Pred_List = []
        
        for item in Prediction:
            item = ' '.join(item)
            Pred_List.append(item)
            
        # Display results as a pandas dataframe with two columns as Source, Prediction. 
        df = pd.DataFrame({'Source': Source, 'Prediction': Pred_List})
        
        return df
