from sklearn.ensemble import RandomForestClassifier

def run_baseline(train_data, test_data):
    features = ['Pipe_Pressure_Low', 'Tank_Level_Low']
    target = 'Pump_Fail'
    
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(train_data[features], train_data[target])
    
    preds = rf.predict(test_data[features])
    return preds