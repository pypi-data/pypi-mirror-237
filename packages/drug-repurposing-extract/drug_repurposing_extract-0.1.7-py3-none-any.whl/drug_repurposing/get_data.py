import requests
import csv
from padelpy import from_smiles
import pandas as pd
import pkgutil
import pickle

data = pkgutil.get_data(__name__, 'rf_model.pkl')

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

import pandas as pd
import pickle

def predict_data(df):
    with open(data, 'rb') as file:
        loaded_rf_model = pickle.load(file)
    cids = df['cid']
    selected_columns = df.filter(like="Pubchem", axis=1)
    additional_columns = df[["ALogp2", "ALogP"]]
    df_filtered = pd.concat([selected_columns, additional_columns], axis=1)
    df_filtered.fillna(df_filtered.mean(), inplace=True)

    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler()
    df_normalized = scaler.fit_transform(df_filtered)
    df_normalized = pd.DataFrame(df_normalized, columns=df_filtered.columns, index=df_filtered.index)
    y_pred = loaded_rf_model.predict(df_normalized)
    result_df = pd.DataFrame({'cid': cids, 'y_pred': y_pred})
    result_df.to_csv('predictions.csv', index=False)



# generate_data([942])
# generate_data_from_upload()