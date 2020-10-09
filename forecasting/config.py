import datetime

train_cutoff = datetime.date(2017, 3, 14)
model_location_prophet = 'models/prophet_model.json'
model_location_xgb = 'models/xgb_model.pkl'
date_string = datetime.date.today().strftime('%Y%m%d')
