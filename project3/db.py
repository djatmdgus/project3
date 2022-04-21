
import pandas as pd
from sqlalchemy import create_engine
df = pd.read_csv('/Users/um_seun/project3/car_csv.csv')

engine = create_engine('postgresql://ggvujchx:or0z4sNzYAyGoDrTfl2SJrSbOLDLYm13@rajje.db.elephantsql.com/ggvujchx')
df.to_sql("car_data", engine,if_exists='replace',index=False)
