import pandas as pd
import os
import schedule
import time
from datetime import datetime

# Seems a little obtuse, but was having troubles with the script recognizing the csv file within the scripts folder so here is a solution I found. 
scriptDirectory = os.path.dirname(os.path.abspath(__file__))
inputFile = os.path.join(scriptDirectory, 'data.csv')
outputFile = os.path.join(scriptDirectory, 'metrics.csv')

def monthlyImport():
    '''Imports Data'''
    try:
        data = pd.read_csv(inputFile)
        print(f' Imported {len(data)} rows from {inputFile}')
        return data
    except FileNotFoundError:
        print(f'Error, data.csv was not found in: {scriptDirectory}, please ensure it is within the same folder as the Automatio Project and try again')
        return None
    
def digestData(data):
    '''Data will be handled here and sent forward to be exported.'''
    data['Profit'] = data['Revenue'] - data['Cost']
    
    # Making the metrics dictionary a hash-table is useful for keeping information coherrent and easier for lookups
    metrics = {
        'Timestamp': datetime.now().strftime('%Y-%m-%d %H:%M'),
        'Total Days': len(data),
        'Total Revenue': data['Revenue'].sum(),
        'Total Cost': data['Cost'].sum(),
        'Total Profit': data['Profit'].sum(),
        'Average Profit': data['Profit'].mean(),
        'Max Profit': data['Profit'].max(),
        'Min Profit': data['Profit'].min()
    }
    return metrics, data # I kept getting issues with the data flow, and it was because this function wasn't returning both metrics and data
    
    
def monthlyExport(metrics, data):
    '''metrics and data from monthlyImport() and digestData() to be appended to metrics.csv'''
    
    results = pd.DataFrame([metrics])
    
    # Checks what the DataFrame looks like
    print("DataFrame to export:")
    print(results)
    print(f"Columns: {results.columns.tolist()}")
    
    # Check if file already exists
    fileExists = os.path.exists(outputFile)
    
    if fileExists:
        # Append without headers
        results.to_csv(outputFile, mode='a', header=False, index=False)
    else:
        # Create new file with headers
        results.to_csv(outputFile, mode='w', header=True, index=False)
    
    print(f'File exists: {fileExists}')
    print(f'Exported metrics to {outputFile}')
 
    

def importExport():
    '''This is what will run all three functions'''
    data = monthlyImport()
    
    if data is None:
        print('Skipping export due to import failure')
        return
    
    metrics, data = digestData(data)
    
    if metrics is None:
        print('Skipping export due to data processing failure')
        return
    
    monthlyExport(metrics, data)
    
importExport()

#this schedules this script to run every month, at 0800 in the morningon the same day. Can be furthered refined but this is sufficient for automation.
schedule.every(30).days.at("08:00").do(importExport)

print('script runs every 30 days, this will be reset if device loses power. Presss Ctrl+C to stop within terminal')

while True:
    schedule.run_pending()
    time.sleep(60)
