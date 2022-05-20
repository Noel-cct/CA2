#!/usr/bin/env python
# coding: utf-8

# In[1]:


##IMPORTING LIBRARIES
import pandas as pd
import statistics as stats
import seaborn as sns #visualisation
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols
from scipy import stats
import scipy as scipy


# In[2]:


df_ire = pd.read_excel('/Users/Noel/Documents/MSc_CA2/ireland-cattle-prices.xlsx')
df_GB = pd.read_excel('/Users/Noel/Documents/MSc_CA2/gt.-britain-cattle-prices.xlsx')
df_NI = pd.read_excel('/Users/Noel/Documents/MSc_CA2/n.ireland-cattle-prices.xlsx')


# In[3]:


print(df_ire.isnull().sum())
print(df_GB.isnull().sum())
print(df_NI.isnull().sum())


# In[4]:


concatenated = pd.concat([df_ire, df_GB], axis=1)
df = pd.concat([concatenated, df_NI], axis=1)


# In[5]:


#dropping columns that are mostly empty
to_drop = ['Cows R2 (lre)','Bulls R3 (GB)','Cows R2 (GB)','Bulls R3 (NI)', 'Cows R2 (NI)' ]
df.drop(to_drop, inplace=True, axis=1)


# In[6]:


df = df.dropna(how='any',axis=0)


# In[8]:


#drop duplicate date columns
df = df.T.drop_duplicates().T


# In[10]:


df.head()


# In[11]:


df.shape


# In[13]:


#line graph of Cows R3
plt.plot(df["Date"], df["Cows R3 (Ire)"], label = "Cows R3 (Ire)")
plt.plot(df["Date"], df["Cows R3 (GB)"], label = "Cows R3 (GB)")
plt.plot(df["Date"], df["Cows R3 (NI)"], label = "Cows R3 (NI)")
plt.xlabel("Date")
plt.ylabel("Price per Kg")
plt.legend()
plt.show()


# In[15]:


#line graph of Cows R4 & R3
plt.plot(df["Date"], df["Cows R4 (Ire)"], label = "Cows R4 (Ire)")
plt.plot(df["Date"], df["Cows R4 (GB)"], label = "Cows R4 (GB)")
plt.plot(df["Date"], df["Cows R4 (NI)"], label = "Cows R4 (NI)")
plt.xlabel("Date")
plt.ylabel("Price per Kg")
plt.legend()
plt.show()


# In[16]:


#line graph of Cows R3
plt.plot(df["Date"], df["Cows O3 (Ire)"], label = "Cows O3 (Ire)")
plt.plot(df["Date"], df["Cows O3 (GB)"], label = "Cows O3 (GB)")
plt.plot(df["Date"], df["Cows O3 (NI)"], label = "Cows O3 (NI)")
plt.xlabel("Date")
plt.ylabel("Price per Kg")
plt.legend()
plt.show()


# In[17]:


#adding month column and year column
df['month'] = pd.DatetimeIndex(df['Date']).month
df['year'] = pd.DatetimeIndex(df['Date']).year


# In[18]:


#creating dataframes to make it easy for data to be graphed by year

df_2019 = df.loc[df['year'].isin([2019])]
df_2018 = df.loc[df['year'].isin([2018])]
df_2017 = df.loc[df['year'].isin([2017])]
df_2016 = df.loc[df['year'].isin([2016])]
df_2015 = df.loc[df['year'].isin([2015])]
df_2014 = df.loc[df['year'].isin([2014])]


# In[20]:


plt.plot(df["Date"], df["Bulls R3 (Ire)"], label = "Bulls R3 (Ire)")
plt.plot(df["Date"], df["Cows R3 (Ire)"], label = "Cows R3 (Ire)")
plt.plot(df["Date"], df["Heifers R3 (Ire)"], label = "Heifers R3 (Ire)")
plt.plot(df["Date"], df["Young Bulls R3 (Ire)"], label = "Young Bulls R3 (Ire)")
plt.plot(df["Date"], df["Steers R3 (Ire)"], label = "Steers R3 (Ire)")

plt.xlabel("Date")
plt.ylabel("Price per Kg")
plt.legend()
plt.show()


# In[43]:


mean_R3cows_Ire= df["Cows R3 (Ire)"].mean()
mean_R3Heifers_Ire= df["Heifers R3 (Ire)"].mean()
mean_R3Steers_Ire= df["Steers R3 (Ire)"].mean()
mean_R3YB_Ire= df["Young Bulls R3 (Ire)"].mean()


sd_R3Cows_Ire = df["Cows R3 (Ire)"].std()
sd_R3Heifers_Ire = df["Heifers R3 (Ire)"].std()
sd_R3Steers_Ire = df["Steers R3 (Ire)"].std()
sd_R3YB_Ire = df["Young Bulls R3 (Ire)"].std()

print('Ire mean price for cows:', mean_R3cows_Ire, 'with sd:', sd_R3Cows_Ire)
print('Ire mean price for Heifers:', mean_R3Steers_Ire, 'with sd:', sd_R3Heifers_Ire)
print('Ire mean price for Steers:', mean_R3Steers_Ire, 'with sd:', sd_R3Steers_Ire)
print('Ire mean price for Young Bulls:', mean_R3cows_Ire, 'with sd:', sd_R3YB_Ire)



# In[23]:


#plt.plot(df["Date"], df["Bulls R2 (GB)"], label = "Bulls R3 (GB)")
plt.plot(df["Date"], df["Cows R3 (GB)"], label = "Cows R3 (GB)")
plt.plot(df["Date"], df["Heifers R3 (GB)"], label = "Heifers R3 (GB)")
plt.plot(df["Date"], df["Young Bulls R3 (GB)"], label = "Young Bulls R3 (GB)")
plt.plot(df["Date"], df["Steers R3 (GB)"], label = "Steers R3 (GB)")

plt.xlabel("Date")
plt.ylabel("Price per Kg")
plt.legend()
plt.show()


# In[44]:


mean_R3cows_GB= df["Cows R3 (GB)"].mean()
mean_R3Heifers_GB= df["Heifers R3 (GB)"].mean()
mean_R3Steers_GB= df["Steers R3 (GB)"].mean()
mean_R3YB_GB= df["Young Bulls R3 (GB)"].mean()


sd_R3Cows_GB = df["Cows R3 (GB)"].std()
sd_R3Heifers_GB = df["Heifers R3 (GB)"].std()
sd_R3Steers_GB = df["Steers R3 (GB)"].std()
sd_R3YB_GB = df["Young Bulls R3 (GB)"].std()

print('GB mean price for cows:', mean_R3cows_GB, 'with sd:', sd_R3Cows_GB)
print('GB mean price for Heifers:', mean_R3Steers_GB, 'with sd:', sd_R3Heifers_GB)
print('GB mean price for Steers:', mean_R3Steers_GB, 'with sd:', sd_R3Steers_GB)
print('GB mean price for Young Bulls:', mean_R3cows_GB, 'with sd:', sd_R3YB_GB)


# In[25]:


#plt.plot(df["Date"], df["Bulls R2 (NI)"], label = "Bulls R3 (NI)")
plt.plot(df["Date"], df["Cows R3 (NI)"], label = "Cows R3 (NI)")
plt.plot(df["Date"], df["Heifers R3 (NI)"], label = "Heifers R3 (NI)")
plt.plot(df["Date"], df["Young Bulls R3 (NI)"], label = "Young Bulls R3 (NI)")
plt.plot(df["Date"], df["Steers R3 (NI)"], label = "Steers R3 (NI)")

plt.xlabel("Date")
plt.ylabel("Price per Kg")
plt.legend()
plt.show()


# In[45]:


mean_R3cows_NI= df["Cows R3 (NI)"].mean()
mean_R3Heifers_NI= df["Heifers R3 (NI)"].mean()
mean_R3Steers_NI= df["Steers R3 (NI)"].mean()
mean_R3YB_NI= df["Young Bulls R3 (NI)"].mean()


sd_R3Cows_NI = df["Cows R3 (NI)"].std()
sd_R3Heifers_NI = df["Heifers R3 (NI)"].std()
sd_R3Steers_NI = df["Steers R3 (NI)"].std()
sd_R3YB_NI = df["Young Bulls R3 (NI)"].std()

print('NI mean price for cows:', mean_R3cows_NI, 'with sd:', sd_R3Cows_NI)
print('NI mean price for Heifers:', mean_R3Steers_NI, 'with sd:', sd_R3Heifers_NI)
print('NI mean price for Steers:', mean_R3Steers_NI, 'with sd:', sd_R3Steers_NI)
print('NI mean price for Young Bulls:', mean_R3cows_NI, 'with sd:', sd_R3YB_NI)


# In[27]:


#line graph of Cows R3
plt.plot(df_2018["Date"], df_2018["Cows O3 (Ire)"], label = "Cows O3 (Ire)")
plt.plot(df_2017["Date"], df_2017["Cows O3 (Ire)"], label = "Cows O3 (Ire)")
plt.plot(df_2016["Date"], df_2016["Cows O3 (Ire)"], label = "Cows O3 (Ire)")
plt.xlabel("Date")
plt.ylabel("Price per Kg")
plt.legend()
plt.show()


# In[28]:


#line graph of Cows R3
plt.plot(df_2018["month"], df_2018["Cows O3 (Ire)"], label = "Cows O3 (Ire)")
plt.plot(df_2017["month"], df_2017["Cows O3 (Ire)"], label = "Cows O3 (Ire)")
plt.plot(df_2016["month"], df_2016["Cows O3 (Ire)"], label = "Cows O3 (Ire)")
plt.xlabel("Date")
plt.ylabel("Price per Kg")
plt.legend()
plt.show()


# In[46]:


#line graph of Cows R3
plt.plot(df_2018["month"], df_2018["Cows O3 (GB)"], label = "Cows O3 2018 (GB)")
plt.plot(df_2017["month"], df_2017["Cows O3 (GB)"], label = "Cows O3 2017 (GB)")
plt.plot(df_2016["month"], df_2016["Cows O3 (GB)"], label = "Cows O3 2016 (GB)")
plt.xlabel("Date")
plt.ylabel("Price per Kg")
plt.legend()
plt.show()


# In[47]:


#line graph of Cows R3
plt.plot(df_2018["month"], df_2018["Cows O3 (NI)"], label = "Cows O3 2018 (NI)")
plt.plot(df_2017["month"], df_2017["Cows O3 (NI)"], label = "Cows O3 2017 (NI)")
plt.plot(df_2016["month"], df_2016["Cows O3 (NI)"], label = "Cows O3 2016 (NI)")
plt.xlabel("Date")
plt.ylabel("Price per Kg")
plt.legend()
plt.show()


# In[31]:


#line graph of Cows R3
plt.plot(df_2018["month"], df_2018["Heifers O3 (Ire)"], label = "Heifers O3 (Ire)")
plt.plot(df_2017["month"], df_2017["Heifers O3 (Ire)"], label = "Heifers O3 (Ire)")
plt.plot(df_2016["month"], df_2016["Heifers O3 (Ire)"], label = "Heifers O3 (Ire)")

plt.xlabel("Month")
plt.ylabel("Price per Kg")
plt.legend()
plt.show()


# In[32]:


#line graph of Cows R3
plt.plot(df_2018["month"], df_2018["Heifers O3 (GB)"], label = "Heifers O3 (GB)")
plt.plot(df_2017["month"], df_2017["Heifers O3 (GB)"], label = "Heifers O3 (GB)")
plt.plot(df_2016["month"], df_2016["Heifers O3 (GB)"], label = "Heifers O3 (GB)")

plt.xlabel("Month")
plt.ylabel("Price per Kg")
plt.legend()
plt.show()


# In[33]:


#line graph of Cows R3
plt.plot(df_2018["month"], df_2018["Steers O3 (Ire)"], label = "Steers O3 (Ire) 2018")
plt.plot(df_2017["month"], df_2017["Steers O3 (Ire)"], label = "Steers O3 (Ire) 2017")
plt.plot(df_2016["month"], df_2016["Steers O3 (Ire)"], label = "Steers O3 (Ire) 2016")

plt.xlabel("Month")
plt.ylabel("Price per Kg")
plt.legend()
plt.show()


# In[34]:


fig1, axs = plt.subplots(2,1, figsize=(18,16))
fig1.suptitle('Cows', fontsize=28, color="#ffffff")
#axs[0].plot(hp.elev, hp.temp, color="#3f48eb", marker="P", zorder=10)
axs[0].plt.plot(df_2018["month"], df_2018["Heifers O3 (GB)"], label = "Heifers O3 (GB)")
axs[0].plt.plot(df_2017["month"], df_2017["Heifers O3 (GB)"], label = "Heifers O3 (GB)")
axs[0].plt.plot(df_2016["month"], df_2016["Heifers O3 (GB)"], label = "Heifers O3 (GB)")

axs[0].set_title("Elevation vs. Temperature", fontsize=24, color="#ffffff")
#axs[0].set_xlabel("Elevation (meters)", fontsize= 21, color="#ffffff")
#axs[0].set_ylabel("Temperature (Celsius)", fontsize=21, color="#ffffff")
#axs[0].set_yticks([0, 3, 6, 9, 12, 15])
#axs[0].set_yticklabels([0, 3, 6, 9, 12, 15], fontsize=14, color="#ffffff")
#axs[0].set_xlim(250, 3500)
#axs[0].set_xticks([500, 1000, 1500, 2000, 2500, 3000, 3500])
#axs[0].set_xticklabels(["500 m", "1,000 m", "1,500 m", "2,000 ", "2,500 m", "3,000 m", "3,500 m"], fontsize=14, color="#ffffff")
#axs[0].grid(True, zorder=0)
#axs[1].scatter(hp.elev, hp.per_for, color="#4b871c", marker="d", zorder=10)
axs[1].set_title("Elevation vs. Percent Forest", fontsize=24, color="#ffffff")

axs[1].plt.plot(df_2018["month"], df_2018["Heifers O3 (Ire)"], label = "Heifers O3 (Ire)")
axs[1].plt.plot(df_2017["month"], df_2017["Heifers O3 (Ire)"], label = "Heifers O3 (Ire)")
axs[1].plt.plot(df_2016["month"], df_2016["Heifers O3 (Ire)"], label = "Heifers O3 (Ire)")

#axs[1].set_xlabel("Elevation (meters)", fontsize= 21, color="#ffffff")
#axs[1].set_ylabel("Percent Forest", fontsize=21, color="#ffffff")
#axs[1].set_yticks([0, 10, 20, 30, 40, 50, 60])
#axs[1].set_yticklabels(["0%", "10%", "20%", "30%", "40%", "50%", "60%"], fontsize=14, color="#ffffff")
#axs[1].set_xlim(0, 3500)
#axs[1].set_xticks([500, 1000, 1500, 2000, 2500, 3000, 3500])
#axs[1].set_xticklabels(["500 m", "1,000 m", "1,500 m", "2,000 ", "2,500 m", "3,000 m", "3,500 m"], fontsize=14, color="#ffffff")
#axs[1].grid(True, zorder=0)
fig1.patch.set_facecolor('#515459')
plt.show(fig1)


# In[48]:


#line graph of Different graded Heifers
plt.plot(df["Date"], df["Heifers O2 (Ire)"], label = "Heifer O2 (Ire)")
plt.plot(df["Date"], df["Heifers O3 (Ire)"], label = "Heifers O3 (Ire)")
plt.plot(df["Date"], df["Heifers O4 (Ire)"], label = "Heifers O4 (Ire)")
plt.plot(df["Date"], df["Heifers R2 (Ire)"], label = "Heifers R2 (Ire)")
plt.plot(df["Date"], df["Heifers R3 (Ire)"], label = "Heifers R3 (Ire)")
plt.plot(df["Date"], df["Heifers R4 (Ire)"], label = "Heifers R4 (Ire)")
plt.plot(df["Date"], df["Heifers U2 (Ire)"], label = "Heifers U2 (Ire)")
plt.plot(df["Date"], df["Heifers U3 (Ire)"], label = "Heifers U3 (Ire)")

plt.xlabel("Date")
plt.ylabel("Price")
plt.legend(loc="best")
plt.show()


# In[51]:


mean_O2Heifers_Ire= df["Heifers O2 (Ire)"].mean()
mean_O3Heifers_Ire= df["Heifers O3 (Ire)"].mean()
mean_O4Heifers_Ire= df["Heifers O4 (Ire)"].mean()
mean_R2Heifers_Ire= df["Heifers R2 (Ire)"].mean()
mean_R3Heifers_Ire= df["Heifers R3 (Ire)"].mean()
mean_R4Heifers_Ire= df["Heifers R4 (Ire)"].mean()
mean_U2Heifers_Ire= df["Heifers U2 (Ire)"].mean()
mean_U3Heifers_Ire= df["Heifers U3 (Ire)"].mean()


sd_O2Heifers_Ire = df["Heifers O2 (Ire)"].std()
sd_O3Heifers_Ire = df["Heifers O3 (Ire)"].std()
sd_O4Heifers_Ire = df["Heifers O4 (Ire)"].std()
sd_R2Heifers_Ire = df["Heifers R2 (Ire)"].std()
sd_R3Heifers_Ire = df["Heifers R3 (Ire)"].std()
sd_R4Heifers_Ire = df["Heifers R4 (Ire)"].std()
sd_U2Heifers_Ire = df["Heifers U2 (Ire)"].std()
sd_U3Heifers_Ire = df["Heifers U3 (Ire)"].std()

print('Ire mean price for O2 Heifers:', mean_O2Heifers_Ire, 'with sd:', sd_O2Heifers_Ire)
print('Ire mean price for O3 Heifers:', mean_O3Heifers_Ire, 'with sd:', sd_O3Heifers_Ire)
print('Ire mean price for O4 Heifers:', mean_O4Heifers_Ire, 'with sd:', sd_O4Heifers_Ire)
print('Ire mean price for R2 Heifers:', mean_R2Heifers_Ire, 'with sd:', sd_R2Heifers_Ire)
print('Ire mean price for R3 Heifers:', mean_R3Heifers_Ire, 'with sd:', sd_R3Heifers_Ire)
print('Ire mean price for R4 Heifers:', mean_R4Heifers_Ire, 'with sd:', sd_R4Heifers_Ire)
print('Ire mean price for U2 Heifers:', mean_U2Heifers_Ire, 'with sd:', sd_U2Heifers_Ire)
print('Ire mean price for U3 Heifers:', mean_U3Heifers_Ire, 'with sd:', sd_U3Heifers_Ire)


# In[ ]:





# In[58]:


#mean_O2Steers_Ire= df["Steers O2 (Ire)"].mean()
mean_O3Steers_Ire= df["Steers O3 (Ire)"].mean()
mean_O4Steers_Ire= df["Steers O4 (Ire)"].mean()
#mean_R2Steers_Ire= df["Steers R2 (Ire)"].mean()
mean_R3Steers_Ire= df["Steers R3 (Ire)"].mean()
mean_R4Steers_Ire= df["Steers R4 (Ire)"].mean()
mean_U2Steers_Ire= df["Steers U2 (Ire)"].mean()
mean_U3Steers_Ire= df["Steers U3 (Ire)"].mean()
mean_U4Steers_Ire= df["Steers U4 (Ire)"].mean()


#sd_O2Steers_Ire = df["Steers O2 (Ire)"].std()
sd_O3Steers_Ire = df["Steers O3 (Ire)"].std()
sd_O4Steers_Ire = df["Steers O4 (Ire)"].std()
#sd_R2Steers_Ire = df["Steers R2 (Ire)"].std()
sd_R3Steers_Ire = df["Steers R3 (Ire)"].std()
sd_R4Steers_Ire = df["Steers R4 (Ire)"].std()
sd_U2Steers_Ire = df["Steers U2 (Ire)"].std()
sd_U3Steers_Ire = df["Steers U3 (Ire)"].std()
sd_U4Steers_Ire = df["Steers U4 (Ire)"].std()

#print('Ire mean price for O2 Steers:', mean_O2Steers_Ire, 'with sd:', sd_O2Steers_Ire)
print('Ire mean price for O3 Steers:', mean_O3Steers_Ire, 'with sd:', sd_O3Steers_Ire)
print('Ire mean price for O4 Steers:', mean_O4Steers_Ire, 'with sd:', sd_O4Steers_Ire)
#print('Ire mean price for R2 Steers:', mean_R2Steers_Ire, 'with sd:', sd_R2Steers_Ire)
print('Ire mean price for R3 Steers:', mean_R3Steers_Ire, 'with sd:', sd_R3Steers_Ire)
print('Ire mean price for R4 Steers:', mean_R4Steers_Ire, 'with sd:', sd_R4Steers_Ire)
print('Ire mean price for U2 Steers:', mean_U2Steers_Ire, 'with sd:', sd_U2Steers_Ire)
print('Ire mean price for U3 Steers:', mean_U3Steers_Ire, 'with sd:', sd_U3Steers_Ire)
print('Ire mean price for U4 Steers:', mean_U4Steers_Ire, 'with sd:', sd_U4Steers_Ire)


# In[52]:


mean_O2Heifers_GB= df["Heifers O2 (GB)"].mean()
mean_O3Heifers_GB= df["Heifers O3 (GB)"].mean()
mean_O4Heifers_GB= df["Heifers O4 (GB)"].mean()
mean_R2Heifers_GB= df["Heifers R2 (GB)"].mean()
mean_R3Heifers_GB= df["Heifers R3 (GB)"].mean()
mean_R4Heifers_GB= df["Heifers R4 (GB)"].mean()
mean_U2Heifers_GB= df["Heifers U2 (GB)"].mean()
mean_U3Heifers_GB= df["Heifers U3 (GB)"].mean()


sd_O2Heifers_GB = df["Heifers O2 (GB)"].std()
sd_O3Heifers_GB = df["Heifers O3 (GB)"].std()
sd_O4Heifers_GB = df["Heifers O4 (GB)"].std()
sd_R2Heifers_GB = df["Heifers R2 (GB)"].std()
sd_R3Heifers_GB = df["Heifers R3 (GB)"].std()
sd_R4Heifers_GB = df["Heifers R4 (GB)"].std()
sd_U2Heifers_GB = df["Heifers U2 (GB)"].std()
sd_U3Heifers_GB = df["Heifers U3 (GB)"].std()

print('GB mean price for O2 Heifers:', mean_O2Heifers_GB, 'with sd:', sd_O2Heifers_GB)
print('GB mean price for O3 Heifers:', mean_O3Heifers_GB, 'with sd:', sd_O3Heifers_GB)
print('GB mean price for O4 Heifers:', mean_O4Heifers_GB, 'with sd:', sd_O4Heifers_GB)
print('GB mean price for R2 Heifers:', mean_R2Heifers_GB, 'with sd:', sd_R2Heifers_GB)
print('GB mean price for R3 Heifers:', mean_R3Heifers_GB, 'with sd:', sd_R3Heifers_GB)
print('GB mean price for R4 Heifers:', mean_R4Heifers_GB, 'with sd:', sd_R4Heifers_GB)
print('GB mean price for U2 Heifers:', mean_U2Heifers_GB, 'with sd:', sd_U2Heifers_GB)
print('GB mean price for U3 Heifers:', mean_U3Heifers_GB, 'with sd:', sd_U3Heifers_GB)


# In[59]:


#mean_O2Steers_GB= df["Steers O2 (GB)"].mean()
mean_O3Steers_GB= df["Steers O3 (GB)"].mean()
mean_O4Steers_GB= df["Steers O4 (GB)"].mean()
#mean_R2Steers_GB= df["Steers R2 (GB)"].mean()
mean_R3Steers_GB= df["Steers R3 (GB)"].mean()
mean_R4Steers_GB= df["Steers R4 (GB)"].mean()
mean_U2Steers_GB= df["Steers U2 (GB)"].mean()
mean_U3Steers_GB= df["Steers U3 (GB)"].mean()
mean_U4Steers_GB= df["Steers U4 (GB)"].mean()


#sd_O2Steers_GB = df["Steers O2 (GB)"].std()
sd_O3Steers_GB = df["Steers O3 (GB)"].std()
sd_O4Steers_GB = df["Steers O4 (GB)"].std()
#sd_R2Steers_GB = df["Steers R2 (GB)"].std()
sd_R3Steers_GB = df["Steers R3 (GB)"].std()
sd_R4Steers_GB = df["Steers R4 (GB)"].std()
sd_U2Steers_GB = df["Steers U2 (GB)"].std()
sd_U3Steers_GB = df["Steers U3 (GB)"].std()
sd_U4Steers_GB = df["Steers U4 (GB)"].std()

#print('GB mean price for O2 Steers:', mean_O2Steers_GB, 'with sd:', sd_O2Steers_GB)
print('GB mean price for O3 Steers:', mean_O3Steers_GB, 'with sd:', sd_O3Steers_GB)
print('GB mean price for O4 Steers:', mean_O4Steers_GB, 'with sd:', sd_O4Steers_GB)
#print('GB mean price for R2 Steers:', mean_R2Steers_GB, 'with sd:', sd_R2Steers_GB)
print('GB mean price for R3 Steers:', mean_R3Steers_GB, 'with sd:', sd_R3Steers_GB)
print('GB mean price for R4 Steers:', mean_R4Steers_GB, 'with sd:', sd_R4Steers_GB)
print('GB mean price for U2 Steers:', mean_U2Steers_GB, 'with sd:', sd_U2Steers_GB)
print('GB mean price for U3 Steers:', mean_U3Steers_GB, 'with sd:', sd_U3Steers_GB)
print('GB mean price for U4 Steers:', mean_U4Steers_GB, 'with sd:', sd_U4Steers_GB)


# In[53]:


mean_O2Heifers_NI= df["Heifers O2 (NI)"].mean()
mean_O3Heifers_NI= df["Heifers O3 (NI)"].mean()
mean_O4Heifers_NI= df["Heifers O4 (NI)"].mean()
mean_R2Heifers_NI= df["Heifers R2 (NI)"].mean()
mean_R3Heifers_NI= df["Heifers R3 (NI)"].mean()
mean_R4Heifers_NI= df["Heifers R4 (NI)"].mean()
mean_U2Heifers_NI= df["Heifers U2 (NI)"].mean()
mean_U3Heifers_NI= df["Heifers U3 (NI)"].mean()


sd_O2Heifers_NI = df["Heifers O2 (NI)"].std()
sd_O3Heifers_NI = df["Heifers O3 (NI)"].std()
sd_O4Heifers_NI = df["Heifers O4 (NI)"].std()
sd_R2Heifers_NI = df["Heifers R2 (NI)"].std()
sd_R3Heifers_NI = df["Heifers R3 (NI)"].std()
sd_R4Heifers_NI = df["Heifers R4 (NI)"].std()
sd_U2Heifers_NI = df["Heifers U2 (NI)"].std()
sd_U3Heifers_NI = df["Heifers U3 (NI)"].std()

print('NI mean price for O2 Heifers:', mean_O2Heifers_NI, 'with sd:', sd_O2Heifers_NI)
print('NI mean price for O3 Heifers:', mean_O3Heifers_NI, 'with sd:', sd_O3Heifers_NI)
print('NI mean price for O4 Heifers:', mean_O4Heifers_NI, 'with sd:', sd_O4Heifers_NI)
print('NI mean price for R2 Heifers:', mean_R2Heifers_NI, 'with sd:', sd_R2Heifers_NI)
print('NI mean price for R3 Heifers:', mean_R3Heifers_NI, 'with sd:', sd_R3Heifers_NI)
print('NI mean price for R4 Heifers:', mean_R4Heifers_NI, 'with sd:', sd_R4Heifers_NI)
print('NI mean price for U2 Heifers:', mean_U2Heifers_NI, 'with sd:', sd_U2Heifers_NI)
print('NI mean price for U3 Heifers:', mean_U3Heifers_NI, 'with sd:', sd_U3Heifers_NI)


# In[74]:


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
x = ['O2 Heifers', 'O3 Heifers', 'O4 Heifers', 'R2 Heifers', 'R3 Heifers', 'R4 Heifers', 'U2 Heifers', 'U3 Heifers']
mean = [mean_O2Heifers_NI,mean_O3Heifers_NI,mean_O4Heifers_NI,mean_R2Heifers_NI,mean_R3Heifers_NI,mean_R4Heifers_NI,mean_U2Heifers_NI,mean_U3Heifers_NI]
ax.bar(x,mean)
ax.set_title('Mean Price per kg for NI Heifers')

plt.xticks(rotation=45)
plt.show()


# In[ ]:



x = ['O2 Heifers', 'O3 Heifers', 'O4 Heifers', 'R2 Heifers', 'R3 Heifers', 'R4 Heifers', 'U2 Heifers', 'U3 Heifers']
mean_Ire = [mean_O2Heifers_Ire,mean_O3Heifers_Ire,mean_O4Heifers_Ire,mean_R2Heifers_Ire,mean_R3Heifers_Ire,mean_R4Heifers_Ire,mean_U2Heifers_Ire,mean_U3Heifers_Ire]
ax1.bar(x,mean_Ire)

x = ['O2 Heifers', 'O3 Heifers', 'O4 Heifers', 'R2 Heifers', 'R3 Heifers', 'R4 Heifers', 'U2 Heifers', 'U3 Heifers']
mean_GB = [mean_O2Heifers_GB,mean_O3Heifers_GB,mean_O4Heifers_GB,mean_R2Heifers_GB,mean_R3Heifers_GB,mean_R4Heifers_GB,mean_U2Heifers_GB,mean_U3Heifers_GB]
ax2.bar(x,mean_GB)


plt.show()


# In[70]:


x = ['O2 Heifers', 'O3 Heifers', 'O4 Heifers', 'R2 Heifers', 'R3 Heifers', 'R4 Heifers', 'U2 Heifers', 'U3 Heifers']
mean_Ire = [mean_O2Heifers_Ire,mean_O3Heifers_Ire,mean_O4Heifers_Ire,mean_R2Heifers_Ire,mean_R3Heifers_Ire,mean_R4Heifers_Ire,mean_U2Heifers_Ire,mean_U3Heifers_Ire]

x = ['O2 Heifers', 'O3 Heifers', 'O4 Heifers', 'R2 Heifers', 'R3 Heifers', 'R4 Heifers', 'U2 Heifers', 'U3 Heifers']
mean_NI = [mean_O2Heifers_NI,mean_O3Heifers_NI,mean_O4Heifers_NI,mean_R2Heifers_NI,mean_R3Heifers_NI,mean_R4Heifers_NI,mean_U2Heifers_NI,mean_U3Heifers_NI]

x = ['O2 Heifers', 'O3 Heifers', 'O4 Heifers', 'R2 Heifers', 'R3 Heifers', 'R4 Heifers', 'U2 Heifers', 'U3 Heifers']
mean_GB = [mean_O2Heifers_GB,mean_O3Heifers_GB,mean_O4Heifers_GB,mean_R2Heifers_GB,mean_R3Heifers_GB,mean_R4Heifers_GB,mean_U2Heifers_GB,mean_U3Heifers_GB]


# In[80]:


fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
fig.suptitle('Horizontally stacked subplots')
ax1.bar(x, mean_Ire)
plt.xticks(rotation = 45)

ax2.bar(x, mean_NI)
plt.xticks(rotation = 45)

ax3.bar(x, mean_GB)
plt.xticks(rotation = 45)

plt.show()


# In[92]:


fig, axs = plt.subplots(2, 2, figsize = (15,15))
axs[0, 0].plot(x, mean_Ire)
axs[0, 0].set_title("main")
axs[0,0].tick_params(axis='x', rotation=45)

axs[1, 0].plot(x, mean_NI)
axs[1, 0].set_title("shares x with main")
axs[1, 0].sharex(axs[0, 0])
axs[1,0].tick_params(axis='x', rotation=45)


axs[0, 1].plot(x, mean_GB)
axs[0, 1].set_title("unrelated")
axs[0,1].tick_params(axis='x', rotation=45)

axs[1, 1].plot(x, mean_GB)
axs[1, 1].set_title("also unrelated")
axs[1,1].tick_params(axis='x', rotation=45)


fig.tight_layout()


# In[99]:


fig, axs = plt.subplots(2, 2, figsize = (10,10))
axs[0, 0].bar(x, mean_Ire)
axs[0, 0].set_title("Heifers Ireland")
axs[0,0].tick_params(axis='x', rotation=45)
axs[0,0].set_ylabel('Price (c/kg)')


axs[1, 0].bar(x, mean_NI)
axs[1, 0].set_title("Heifers NI")
axs[1, 0].sharex(axs[0, 0])
axs[1,0].tick_params(axis='x', rotation=45)
axs[1,0].set_ylabel('Price (c/kg)')

axs[0, 1].bar(x, mean_GB)
axs[0, 1].set_title("Heifers GB")
axs[0,1].tick_params(axis='x', rotation=45)
axs[0,1].set_ylabel('Price (c/kg)')

axs[1, 1].bar(x, mean_GB)
axs[1, 1].set_title("also unrelated")
axs[1,1].tick_params(axis='x', rotation=45)
axs[1,1].set_ylabel('Price (c/kg)')


fig.tight_layout()


# In[ ]:


#mean_O2Steers_GB= df["Steers O2 (GB)"].mean()
mean_O3Steers_GB= df["Steers O3 (GB)"].mean()
mean_O4Steers_GB= df["Steers O4 (GB)"].mean()
#mean_R2Steers_GB= df["Steers R2 (GB)"].mean()
mean_R3Steers_GB= df["Steers R3 (GB)"].mean()
mean_R4Steers_GB= df["Steers R4 (GB)"].mean()
mean_U2Steers_GB= df["Steers U2 (GB)"].mean()
mean_U3Steers_GB= df["Steers U3 (GB)"].mean()
mean_U4Steers_GB= df["Steers U4 (GB)"].mean()


#sd_O2Steers_GB = df["Steers O2 (GB)"].std()
sd_O3Steers_GB = df["Steers O3 (GB)"].std()
sd_O4Steers_GB = df["Steers O4 (GB)"].std()
#sd_R2Steers_GB = df["Steers R2 (GB)"].std()
sd_R3Steers_GB = df["Steers R3 (GB)"].std()
sd_R4Steers_GB = df["Steers R4 (GB)"].std()
sd_U2Steers_GB = df["Steers U2 (GB)"].std()
sd_U3Steers_GB = df["Steers U3 (GB)"].std()
sd_U4Steers_GB = df["Steers U4 (GB)"].std()

#print('GB mean price for O2 Steers:', mean_O2Steers_GB, 'with sd:', sd_O2Steers_GB)
print('GB mean price for O3 Steers:', mean_O3Steers_GB, 'with sd:', sd_O3Steers_GB)
print('GB mean price for O4 Steers:', mean_O4Steers_GB, 'with sd:', sd_O4Steers_GB)
#print('GB mean price for R2 Steers:', mean_R2Steers_GB, 'with sd:', sd_R2Steers_GB)
print('GB mean price for R3 Steers:', mean_R3Steers_GB, 'with sd:', sd_R3Steers_GB)
print('GB mean price for R4 Steers:', mean_R4Steers_GB, 'with sd:', sd_R4Steers_GB)
print('GB mean price for U2 Steers:', mean_U2Steers_GB, 'with sd:', sd_U2Steers_GB)
print('GB mean price for U3 Steers:', mean_U3Steers_GB, 'with sd:', sd_U3Steers_GB)
print('GB mean price for U4 Steers:', mean_U4Steers_GB, 'with sd:', sd_U4Steers_GB)


# In[100]:


#line graph of Cows R3
plt.plot(df_2018["month"], df_2018["Cows O3 (Ire)"], label = "Cows O3 (Ire)")
plt.plot(df_2017["month"], df_2017["Cows O3 (Ire)"], label = "Cows O3 (Ire)")
plt.plot(df_2016["month"], df_2016["Cows O3 (Ire)"], label = "Cows O3 (Ire)")
plt.xlabel("Date")
plt.ylabel("Price per Kg")
plt.legend()
plt.show()


# In[107]:


ab = df_2018["Cows O3 (Ire)"].mean()
ac = df_2017["Cows O3 (Ire)"].mean()
ad = df_2016["Cows O3 (Ire)"].mean()
af = df_2015["Cows O3 (Ire)"].mean()

print(ab,ac,ad,af)


# In[113]:


mean_O3Heifers_GB_2019= df_2019["Heifers O3 (GB)"].mean()
mean_O3Heifers_GB_2018= df_2018["Heifers O3 (GB)"].mean()
mean_O3Heifers_GB_2017= df_2017["Heifers O3 (GB)"].mean()
mean_O3Heifers_GB_2016= df_2016["Heifers O3 (GB)"].mean()
mean_O3Heifers_GB_2015= df_2015["Heifers O3 (GB)"].mean()


sd_O3Heifers_GB_2019 = df_2019["Heifers O3 (GB)"].std()
sd_O3Heifers_GB_2018 = df_2018["Heifers O3 (GB)"].std()
sd_O3Heifers_GB_2017 = df_2017["Heifers O3 (GB)"].std()
sd_O3Heifers_GB_2016 = df_2016["Heifers O3 (GB)"].std()
sd_O3Heifers_GB_2015 = df_2015["Heifers O3 (GB)"].std()

print('GB mean price for O3 Heifers 2019:', mean_O3Heifers_GB_2019, 'with sd:', sd_O3Heifers_GB_2019)
print('GB mean price for O3 Heifers 2018:', mean_O3Heifers_GB_2018, 'with sd:', sd_O3Heifers_GB_2018)
print('GB mean price for O3 Heifers 2017:', mean_O3Heifers_GB_2017, 'with sd:', sd_O3Heifers_GB_2017)
print('GB mean price for O3 Heifers 2016:', mean_O3Heifers_GB_2016, 'with sd:', sd_O3Heifers_GB_2016)
print('GB mean price for 03 Heifers 2015:', mean_O3Heifers_GB_2015, 'with sd:', sd_O3Heifers_GB_2015)


# In[115]:


mean_O3Heifers_Ire_2019= df_2019["Heifers O3 (Ire)"].mean()
mean_O3Heifers_Ire_2018= df_2018["Heifers O3 (Ire)"].mean()
mean_O3Heifers_Ire_2017= df_2017["Heifers O3 (Ire)"].mean()
mean_O3Heifers_Ire_2016= df_2016["Heifers O3 (Ire)"].mean()
mean_O3Heifers_Ire_2015= df_2015["Heifers O3 (Ire)"].mean()


sd_O3Heifers_Ire_2019 = df_2019["Heifers O3 (Ire)"].std()
sd_O3Heifers_Ire_2018 = df_2018["Heifers O3 (Ire)"].std()
sd_O3Heifers_Ire_2017 = df_2017["Heifers O3 (Ire)"].std()
sd_O3Heifers_Ire_2016 = df_2016["Heifers O3 (Ire)"].std()
sd_O3Heifers_Ire_2015 = df_2015["Heifers O3 (Ire)"].std()

print('Ire mean price for O3 Heifers 2019:', mean_O3Heifers_Ire_2019, 'with sd:', sd_O3Heifers_Ire_2019)
print('Ire mean price for O3 Heifers 2018:', mean_O3Heifers_Ire_2018, 'with sd:', sd_O3Heifers_Ire_2018)
print('Ire mean price for O3 Heifers 2017:', mean_O3Heifers_Ire_2017, 'with sd:', sd_O3Heifers_Ire_2017)
print('Ire mean price for O3 Heifers 2016:', mean_O3Heifers_Ire_2016, 'with sd:', sd_O3Heifers_Ire_2016)
print('Ire mean price for O3 Heifers 2015:', mean_O3Heifers_Ire_2015, 'with sd:', sd_O3Heifers_Ire_2015)


# In[116]:


mean_O3Heifers_NI_2019= df_2019["Heifers O3 (NI)"].mean()
mean_O3Heifers_NI_2018= df_2018["Heifers O3 (NI)"].mean()
mean_O3Heifers_NI_2017= df_2017["Heifers O3 (NI)"].mean()
mean_O3Heifers_NI_2016= df_2016["Heifers O3 (NI)"].mean()
mean_O3Heifers_NI_2015= df_2015["Heifers O3 (NI)"].mean()


sd_O3Heifers_NI_2019 = df_2019["Heifers O3 (NI)"].std()
sd_O3Heifers_NI_2018 = df_2018["Heifers O3 (NI)"].std()
sd_O3Heifers_NI_2017 = df_2017["Heifers O3 (NI)"].std()
sd_O3Heifers_NI_2016 = df_2016["Heifers O3 (NI)"].std()
sd_O3Heifers_NI_2015 = df_2015["Heifers O3 (NI)"].std()

print('NI mean price for O3 Heifers 2019:', mean_O3Heifers_NI_2019, 'with sd:', sd_O3Heifers_NI_2019)
print('NI mean price for O3 Heifers 2018:', mean_O3Heifers_NI_2018, 'with sd:', sd_O3Heifers_NI_2018)
print('NI mean price for O3 Heifers 2017:', mean_O3Heifers_NI_2017, 'with sd:', sd_O3Heifers_NI_2017)
print('NI mean price for O3 Heifers 2016:', mean_O3Heifers_NI_2016, 'with sd:', sd_O3Heifers_NI_2016)
print('NI mean price for O3 Heifers 2015:', mean_O3Heifers_NI_2015, 'with sd:', sd_O3Heifers_NI_2015)


# In[136]:


#https://pypi.org/project/tabulate/

from tabulate import tabulate
table = [['Unit','2019','2018','2017','2016', '2015'],
    ['Mean Price', mean_O3Heifers_NI_2019,mean_O3Heifers_NI_2018, mean_O3Heifers_NI_2017, mean_O3Heifers_NI_2016, mean_O3Heifers_NI_2015],
         ['Std Dev',sd_O3Heifers_NI_2019, sd_O3Heifers_NI_2018, sd_O3Heifers_NI_2017, sd_O3Heifers_NI_2016, sd_O3Heifers_NI_2015]]

print(tabulate(table, headers='firstrow',tablefmt='fancy_grid', numalign='left'))


# In[137]:


from tabulate import tabulate
table = [['Unit','2019','2018','2017','2016', '2015'],
    ['Mean Price', mean_O3Heifers_Ire_2019,mean_O3Heifers_Ire_2018, mean_O3Heifers_Ire_2017, mean_O3Heifers_Ire_2016, mean_O3Heifers_Ire_2015],
         ['Std Dev',sd_O3Heifers_Ire_2019, sd_O3Heifers_Ire_2018, sd_O3Heifers_Ire_2017, sd_O3Heifers_Ire_2016, sd_O3Heifers_Ire_2015]]

print(tabulate(table, headers='firstrow',tablefmt='fancy_grid', numalign='left'))


# In[138]:


from tabulate import tabulate
table = [['Unit','2019','2018','2017','2016', '2015'],
    ['Mean Price', mean_O3Heifers_GB_2019,mean_O3Heifers_GB_2018, mean_O3Heifers_GB_2017, mean_O3Heifers_GB_2016, mean_O3Heifers_GB_2015],
         ['Std Dev',sd_O3Heifers_GB_2019, sd_O3Heifers_GB_2018, sd_O3Heifers_GB_2017, sd_O3Heifers_GB_2016, sd_O3Heifers_GB_2015]]

print(tabulate(table, headers='firstrow',tablefmt='fancy_grid', numalign='left'))


# In[141]:


#checking distribution of the Heifers Price
sns.distplot(df["Heifers O3 (Ire)"])
plt.title('Heifer Price per Kg', fontsize=18)
plt.xlabel('Price (c/kg)', fontsize=16)
plt.ylabel('Frequency', fontsize=16)

plt.show()


# In[143]:


#checking distribution of the Heifers Price 2019
sns.distplot(df_2019["Heifers O3 (Ire)"])
plt.title('Heifer Price per Kg 2019', fontsize=18)
plt.xlabel('Price (c/kg)', fontsize=16)
plt.ylabel('Frequency', fontsize=16)

plt.show()


# In[144]:


#checking distribution of the Heifers Price 2019
sns.distplot(df_2018["Heifers O3 (Ire)"])
plt.title('Heifer Price per Kg 2019', fontsize=18)
plt.xlabel('Price (c/kg)', fontsize=16)
plt.ylabel('Frequency', fontsize=16)

plt.show()


# In[148]:


#checking distribution of the Heifers Price
sns.distplot(df["Heifers O3 (GB)"])
plt.title('Heifer Price per Kg', fontsize=18)
plt.xlabel('Price (c/kg)', fontsize=16)
plt.ylabel('Frequency', fontsize=16)

plt.show()


# In[149]:


#checking distribution of the Heifers Price
sns.distplot(df["Heifers O3 (NI)"])
plt.title('Heifer Price per Kg', fontsize=18)
plt.xlabel('Price (c/kg)', fontsize=16)
plt.ylabel('Frequency', fontsize=16)

plt.show()


# In[151]:


#Normality plot. Our variable is "Heifers O3 Ire"
x = df["Heifers O3 (Ire)"].astype(int)

stats.probplot(x , plot=plt)
plt.figure()


# In[152]:


#must chage float to integer to use in shapiro
x = df["Cows R3 (Ire)"].astype(int)
y = x[df.month == 5]

y


# In[153]:


#using shapiro test to check for normaility
stats.shapiro(x)


# In[154]:


#using shapiro test to check for normaility
stats.shapiro(df["Heifers O3 (GB)"].astype(int))


# In[155]:


#using shapiro test to check for normaility
stats.shapiro(df["Heifers R3 (GB)"].astype(int))


# In[156]:


#using shapiro test to check for normaility
stats.shapiro(df_2019["Heifers R3 (GB)"].astype(int))


# In[157]:


#using shapiro test to check for normaility
stats.shapiro(df_2019["Heifers R3 (GB)"].astype(int))


# In[158]:


#This means the avona test will not work as data is not normally distribute. I will try t-test & ANOVA anyway


# In[159]:


#Calculating
a = df["Cows R3 (Ire)"]
mean_cows_r3_Ire= a.mean()

sd = a.std()
print('Mean:',mean_cows_r3_Ire, 'Std Dev:', sd)


# In[160]:



#H0 : u = 320
#H1 : u =! 320

stats.ttest_1samp(x,320)


# In[162]:


#because p>0.05 we would accept H1. There is not enough evidence to say that mean is = 320 c/kg
df["Cows R3 (Ire)"]


# In[163]:


#Suppose that a farmer wants to know if the price is, in average, greater than 320 c/kg. 
#Calculate the test at a 5% significance level.

#H1 : u > 320
stats.t.sf(7.333582654706759, 249) 

#If p value < alpha --> we reject H0
#If p-valye > alpha --> we accept H0


# In[ ]:


#We group the data according to the categories requested by the company

families = dataset.query('Traveler_type == "Families"')['Hotel_stars_given']
business = dataset.query('Traveler_type == "Business"')['Hotel_stars_given']

#We perform the test assuming as H0 that mu1 = mu2 (family rate = business rate)
test = stats.ttest_ind(families, business, 
                      equal_var=True)

display(test)


# In[164]:


#We perform the test assuming as H0 that mu1 = mu2 (Ire = NI)

a = df["Steers R3 (Ire)"]
b = df["Heifers R3 (Ire)"]

test = stats.ttest_ind(a, b, 
                      equal_var=True)

display(test)


# In[ ]:


#pvalue < alpha so reject null hypothesis ie averages not the same


# In[165]:


#We perform the test assuming as H0 that mu1 = mu2 (Ire = NI)

a = df["Heifers R3 (Ire)"]
b = df["Heifers R3 (GB)"]

test = stats.ttest_ind(a, b, 
                      equal_var=True)

display(test)


# In[167]:


test = stats.ttest_ind(a, b, 
                      equal_var=False)

display(test)


# In[173]:


x = df_2019["Heifers R3 (Ire)"]
y = df_2019["Heifers R3 (GB)"]
z = df_2019["Heifers R3 (NI)"]


# In[174]:


#perform Kruskal-Wallis Test 
stats.kruskal(x, y, z)


# In[175]:


x = df_2019["Heifers R3 (Ire)"]
y = df_2019["Steers R3 (GB)"]
z = df_2019["Steers R4 (NI)"]


# In[176]:


#perform Kruskal-Wallis Test 
stats.kruskal(x, y, z)


# In[179]:


x = df_2016["Heifers R3 (Ire)"]
y = df_2017["Heifers R3 (Ire)"]
z = df_2018["Heifers R3 (Ire)"]


# In[180]:


#perform Kruskal-Wallis Test 
stats.kruskal(x, y, z)


# In[182]:


x = df_2017["Heifers R3 (Ire)"]
y = df_2018["Heifers R3 (Ire)"]
z = df_2019["Heifers R3 (Ire)"]
stats.kruskal(x, y, z)


# In[183]:


x = df_2016["Cows R3 (Ire)"]
y = df_2017["Cows R3 (Ire)"]
z = df_2018["Cows R3 (Ire)"]

#perform Kruskal-Wallis Test 
stats.kruskal(x, y, z)


# In[186]:


x = df_2016["Heifers R3 (GB)"]
y = df_2017["Heifers R3 (GB)"]
z = df_2018["Heifers R3 (GB)"]

stats.kruskal(x, y, z)


# In[187]:


x = df_2016["Steers R3 (GB)"]
y = df_2017["Steers R3 (GB)"]
z = df_2018["Steers R3 (GB)"]

stats.kruskal(x, y, z)


# In[189]:


x = df_2016["Heifers O4 (GB)"]
y = df_2017["Heifers O4 (GB)"]
z = df_2018["Heifers O4 (GB)"]

stats.kruskal(x, y, z)


# In[190]:


from scipy.stats import mannwhitneyu

# Carrying out the Wilcoxon–Mann–Whitney test
results = mannwhitneyu(df_2018["Heifers R3 (GB)"], df_2017["Heifers R3 (GB)"])
results


# In[191]:


from scipy.stats import mannwhitneyu

# Carrying out the Wilcoxon–Mann–Whitney test
results = mannwhitneyu(df_2018["Heifers R3 (GB)"], df_2019["Heifers R3 (GB)"])
results


# In[ ]:




