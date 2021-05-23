#!/usr/bin/env python
# coding: utf-8

# # Whoop API
# 
# This will give you an excel files for the stats in whoop api
# 
# You should pip install pandas
# 
# 
# ```pip install pandas```

# In[]:


import json
from datetime import datetime as dt # For turning you inputs to fields

import pandas as pd
from user import whoopUser # The whoop API


# ### Creds

# In[ ]:


email = "email"
password = "password"
user = whoopUser(email, password)


# In[ ]:


params = {
        'start': '2000-01-01T00:00:00.000Z',
        'end': '2030-01-01T00:00:00.000Z'
    }


# In[ ]:


print('You can take the data from certain duration, for example: from yesterday to today. If you dont want to specify the duration you can skip it, If you skip the data will be from 2001 to 2030')
skip = input('Do you want to skip? [y/n]')

if skip == 'n':
    print('From: (You can just skip if you want, default is 2001)')
    from_year = int(input('year: ') or 2001)
    from_month = int(input('month: ') or 1)
    from_day = int(input('day :') or 1)
    from_hour = int(input('hour: (default: 12 am)') or 0)
    from_minute = int(input('minute: (default: 0)') or 0)
    
    print('To: (You can just skip if you want, default is 2030)')
    to_year = int(input('year: ') or 2030)
    to_month = int(input('month (default: January): ') or 1)
    to_day = int(input('day (default: 1):') or 1)
    to_hour = int(input('hour: (default: 12 am)') or 0)
    to_minute = int(input('minute: (default: 0)') or 0)
    
    params = {
        'start' : dt(from_year, from_month, from_day, from_hour, from_minute).isoformat() + 'Z',
        'end' : dt(to_year, to_month, to_day, to_hour, to_minute).isoformat() + 'Z'
    }
    


# In[]:
# Get all the thing and export as csv
user.get_cycles_df(params).to_csv('cycles.csv')
user.get_sleeps_df(params).to_csv('sleeps.csv')
user.get_workouts_df(params).to_csv('workouts.csv')
user.get_heart_rate_df(params).to_csv('heart_rates.csv')
pd.DataFrame(user.get_sports()).to_csv('sports.csv')

