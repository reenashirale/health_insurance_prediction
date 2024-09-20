import pickle
import numpy as np
import json
from config import MODEL_FILE_PATH, JSON_FILE_PATH

class HealthInsurance():
    def __init__(self):
        pass

    def load_data(self):
        with open(MODEL_FILE_PATH, 'rb') as f:
            self.model =  pickle.load(f)
        
        with open(JSON_FILE_PATH, 'r') as f:
            self.col_data = json.load(f)


    def predict_insurance_charges(self, age, sex, bmi, children, smoker, region):
        self.load_data()
        test_data = np.zeros(len(self.col_data['columns']))
        test_data[0] = age
        test_data[1] = sex
        test_data[2] = bmi
        test_data[3] = children
        test_data[4] = smoker
        region_index = self.col_data['columns'].index(region)
        test_data[region_index] = 1
        print(test_data)
        predicted_charges = self.model.predict([test_data])
        print(f"Charges for Medical Insurance are : RS. {round(predicted_charges[0], 2)}")
        return round(predicted_charges[0], 2)



if __name__ == "__main__":
    ins = HealthInsurance()
    ins.load_data()
    # print(list(ins.column_data['smoker'].keys()))