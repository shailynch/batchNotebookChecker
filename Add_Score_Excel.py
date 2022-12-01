import pandas as pd
import os
from datetime import datetime

# Score should be a list. Pass either [10,20,30] or [60].
scores = [103]

# datetime object containing current date and time
now = datetime.now()

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

# Add score to excel function
def add_score_excel(score):
    # Combines list of scores
    total_score = sum(score)
    # Data to be added to excel doc
    data = {'Date (dd,mm,YY)': [dt_string], 'Score': [total_score]}
    # Turn data into a dataframe
    df = pd.DataFrame.from_dict(data)
    
    # Check if our excel doc already exist
    if os.path.exists('Score_File.xlsx'):
        print("Adding to file")
        # Read excel file
        df_read = pd.read_excel('Score_File.xlsx')
        # Combine dataframes
        newDF = pd.concat([df_read, df], axis=0)
        # Save file
        newDF.to_excel('Score_File.xlsx', index=False)
        print(newDF)
    else:
        # Create new excel file
        print("Creating file")
        # Save file
        df.to_excel('Score_File.xlsx', index=False)


add_score_excel(scores)