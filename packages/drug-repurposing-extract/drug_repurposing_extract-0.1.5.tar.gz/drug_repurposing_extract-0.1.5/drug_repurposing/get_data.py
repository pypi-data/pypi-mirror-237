import requests
import csv
from padelpy import from_smiles
import pandas as pd

def generate_data_from_list(cids=[]):
    results = []
    fails = []
    for cid in cids:
        try:
            resp = requests.get("https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/" + str(cid) + "/property/MolecularWeight,MolecularFormula,IsomericSMILES,IUPACName/JSON")
            content = resp.json()
            desc_fp = from_smiles(content['PropertyTable']['Properties'][0]['IsomericSMILES'], fingerprints=True)
            desc_fp['cid'] = cid
            results.append(desc_fp)
        except Exception as e:
            print(e)
            # print(content)
            fails.append(cid)
    if(len(fails)>0):
        print("Fails CIDS: ", fails)

    if(len(results)>0):
        csv_file = 'complete_data.csv'
        field_names = results[0].keys()
        with open(csv_file, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=field_names)
            writer.writeheader()
            for row in results:
                writer.writerow(row)

def generate_data_from_upload():
    import tkinter as tk
    from tkinter import filedialog
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

    if file_path:
        try:
            df = pd.read_csv(file_path)
            cids = df['CID'].values
            results = []
            fails = []
            for cid in cids:
                try:
                    resp = requests.get("https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/" + str(cid) + "/property/MolecularWeight,MolecularFormula,IsomericSMILES,IUPACName/JSON")
                    content = resp.json()
                    desc_fp = from_smiles(content['PropertyTable']['Properties'][0]['IsomericSMILES'], fingerprints=True)
                    desc_fp['cid'] = cid
                    results.append(desc_fp)
                except Exception as e:
                    print(e)
                    # print(content)
                    fails.append(cid)
            if(len(fails)>0):
                print("Fails CIDS: ", fails)

            if(len(results)>0):
                csv_file = 'complete_data.csv'
                field_names = results[0].keys()
                with open(csv_file, 'w', newline='') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=field_names)
                    writer.writeheader()
                    for row in results:
                        writer.writerow(row)
        except Exception as e:
            print("Error reading CSV file:", e)
    else:
        print("No file selected.")

# generate_data([942])
generate_data_from_upload()