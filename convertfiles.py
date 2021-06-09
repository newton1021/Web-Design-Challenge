#!/usr/bin/env python3

import os
import pandas as pd

filepath = "Resources/output_data/city_temperature.csv"
fileout = "Resources/output_data/city_temperature.html"
df = pd.read_csv(filepath)

df.to_html(fileout, index=False)
