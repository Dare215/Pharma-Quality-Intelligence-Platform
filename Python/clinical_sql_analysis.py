import pandas as pd
from sqlalchemy import create_engine

engine=create_engine("postgresql://user:password@localhost/clinical_trials")
print("Connect and execute advanced SQL queries here.")
