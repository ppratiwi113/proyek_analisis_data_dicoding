import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('dark')

def count_total_rents(days_df):
    total_rents_df = days_df.groupby(by="dteday").agg({
        "count": "sum"
    }).reset_index()
    return total_rents_df

def count_daily_register(days_df):
    register_df = days_df.groupby(by="dteday").agg({
        "registered": "sum"
    }).reset_index()
    return register_df

def count_daily_casual(days_df):
    casual_df = days_df.groupby(by="dteday").agg({
        "casual": "sum"
    }).reset_index()
    return casual_df

def weather_counts(hours_df):
    weather_counts_df = hours_df.groupby('weather_situation')['count'].mean().sort_values(ascending=False).reset_index()
    return weather_counts_df

def season_counts(days_df):
    season_counts_df = days_df.groupby('season')['count'].mean().sort_values(ascending=False).reset_index()
    return season_counts_df

def calculate_monthly_counts(days_df):
    # Calculate the total rentals per month
    monthly_counts_df = days_df.groupby(['year', 'month']).agg({'count': 'sum'}).reset_index()
    
    # Convert month abbreviations to numbers
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    monthly_counts_df['month_num'] = monthly_counts_df['month'].apply(lambda x: month_order.index(x) + 1)
    
    # Sort by year and month number
    monthly_counts_df = monthly_counts_df.sort_values(by=['year', 'month_num'])
    return monthly_counts_df


# Load cleaned data
days_df = pd.read_csv("cleaned_day.csv")
hours_df = pd.read_csv("cleaned_hour.csv")

st.dataframe(days_df)
st.dataframe(hours_df)

datetime_columns = ["dteday"]
days_df.sort_values(by="dteday", inplace=True)
days_df.reset_index(inplace=True)   

hours_df.sort_values(by="dteday", inplace=True)
hours_df.reset_index(inplace=True)

for column in datetime_columns:
    days_df[column] = pd.to_datetime(days_df[column])
    hours_df[column] = pd.to_datetime(hours_df[column])

# Filter data
min_date_days = days_df["dteday"].min()
max_date_days = days_df["dteday"].max()

min_date_hours = hours_df["dteday"].min()
max_date_hours = hours_df["dteday"].max()

with st.sidebar:
    st.title("Bike Rental Company :bike:")
    st.image("rentals_logo.jpg")
    
        # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value=min_date_days,
        max_value=max_date_days,
        value=[min_date_days, max_date_days])
  
main_df_days = days_df[(days_df["dteday"] >= str(start_date)) & 
                       (days_df["dteday"] <= str(end_date))]

main_df_hours = hours_df[(hours_df["dteday"] >= str(start_date)) & 
                        (hours_df["dteday"] <= str(end_date))]


# Menyiapkan berbagai dataframe
totals_rent_df = count_total_rents(main_df_days)
weather_counts_df = weather_counts(main_df_hours)
season_counts_df = season_counts(main_df_days)
register_df = count_daily_register(main_df_days)
casual_df = count_daily_casual(main_df_days)
monthly_counts_data = calculate_monthly_counts(days_df)
#Visualization Filter Page


# Antarmuka Dashboard
st.title("Analisis Data Penyewaan Sepeda")
st.caption("Putri Pratiwi | putripratiwi790@gmail.com")
st.write("-----------------------------------------------")


st.header('Daily Sharing')
col1, col2, col3 = st.columns(3)
 
with col1:
    total_rentals = totals_rent_df["count"].sum()
    st.metric("Total Sharing Bike", value=total_rentals)
    
with col2:
    total_sum = register_df["registered"].sum()
    st.metric("Total Registered", value=total_sum)

with col3:
    total_sum = casual_df["casual"].sum()
    st.metric("Total Casual", value=total_sum)


st.subheader(":arrow_right: Cuaca (weather) yang paling mempengaruhi banyaknya penyewaan sepeda")
colors= [ "#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=weather_counts_df, x='weather_situation', y='count', palette=colors)
plt.title('Jumlah Penyewaan Sepeda Berdasarkan Cuaca', pad=10)
plt.ylabel(None)
plt.xlabel(None)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
st.pyplot(fig)

st.subheader(":arrow_right: Musim (season) yang paling mempengaruhi jumlah penyewaan sepeda")
colors= [ "#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
fig, ax = plt.subplots(figsize=(10,6))
sns.barplot(data=season_counts_df, x='season', y='count', palette=colors)
plt.title('Jumlah Penyewaan Sepeda Berdasarkan Musim', pad=10)
plt.xlabel(None)
plt.ylabel(None)
st.pyplot(fig)

st.subheader(":arrow_right: Tren penyewaan sepeda per- bulan selama dua tahun (2011 - 2012)")
plt.figure(figsize=(10, 5))
for year in monthly_counts_data['year'].unique():
    subset = monthly_counts_data[monthly_counts_data['year'] == year]
    plt.plot(subset['month'], subset['count'], marker='o', label=year)

plt.xlabel(None)
plt.ylabel('Jumlah Penyewaan Sepeda')
plt.legend(title='Tahun')
plt.grid(True)
st.pyplot(plt)

st.subheader(":arrow_right: Perbandingan jumlah penyewaan sepeda tehadap pengguna casual dan registered berdasarkan hari kerja dan libur")
colors = ["#D3D3D3", "#72BCD4"] 
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(35, 15))

sns.barplot(data=days_df, x='category_days', y='casual', hue='year', palette=colors, ax=ax[0])
ax[0].set_title('Perbandingan Jumlah Penyewaan Sepeda oleh Pengguna Casual', loc="center", pad=30, fontsize=30)
ax[0].set_xlabel(None)
ax[0].set_ylabel(None)
ax[0].legend(title='Tahun', title_fontsize=30, prop={'size': 30})
ax[0].tick_params(axis='y', labelsize=35)
ax[0].tick_params(axis='x', labelsize=30)

sns.barplot(data=days_df, x='category_days', y='registered', hue='year', palette=colors, ax=ax[1])
ax[1].set_title('Perbandingan Jumlah Penyewaan Sepeda oleh Pengguna Terdaftar', pad=30, fontsize=30)
ax[1].set_xlabel(None)
ax[1].set_ylabel(None)
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].legend(title='Tahun', title_fontsize=30, prop={'size': 30})
ax[1].tick_params(axis='y', labelsize=35)
ax[1].tick_params(axis='x', labelsize=30)

st.pyplot(fig)