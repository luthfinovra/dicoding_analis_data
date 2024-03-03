import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

def summary_revenue_line_chart(summary_revenue_df):
   # Line Chart Pendapatan dan Banyak Order dari Tahun ke Tahun
   summary_revenue_df['year_month'] = summary_revenue_df['year'].astype(str) + '-' + summary_revenue_df['month'].astype(str)

   fig = plt.figure(figsize=(12, 6))
   ax = sns.lineplot(x='year_month', y='revenue', data=summary_revenue_df, marker='o', markersize=8, errorbar=None, color='purple')

   # mendapatkan index pendapatan terbesar
   max_revenue_index = summary_revenue_df['revenue'].idxmax()

   # Melakukan anotasi pada pendapatan terbesar
   max_revenue = summary_revenue_df.loc[max_revenue_index, 'revenue']
   max_year_month = summary_revenue_df.loc[max_revenue_index, 'year_month']

# Mengatur Posisi Anotasi
   annotation_y_position = max_revenue + 50000
   annotation_x_position = max_year_month

   # Annotasi Pendaptan terbesar
   ax.annotate(f'Pendapatan Terbesar\n{max_revenue:.2f} (BRL)', xy=(max_year_month, max_revenue), xytext=(annotation_x_position, annotation_y_position),
            arrowprops=dict(facecolor='red', shrink=0.05),
            ha='center', va='bottom'
            )

   # Set Label Chart
   plt.title('Pendapatan dari Tahun ke Tahun')
   plt.xlabel('Tahun-Bulan')
   plt.ylabel('Pendapatan (BRL)')

   plt.xticks(rotation=45, ha='right')

   # Mengubah limit border chart
   ax.set_ylim(0, max_revenue + 200000) 

   return fig

def summary_total_order_line_chart(summary_revenue_df):
   # Line Chart Pendapatan dan Banyak Order dari Tahun ke Tahun
   summary_revenue_df['year_month'] = summary_revenue_df['year'].astype(str) + '-' + summary_revenue_df['month'].astype(str)

   # Line Chart  Banyak Order dari Tahun ke Tahun
   fig = plt.figure(figsize=(12, 6))
   ax = sns.lineplot(x='year_month', y='order_freq', data=summary_revenue_df, marker='o', markersize=8, errorbar=None, color='purple')

   # mendapatkan index order_freq terbesar
   max_order_index = summary_revenue_df['order_freq'].idxmax()

   # Melakukan anotasi pada Banyak Order terbesar
   max_order = summary_revenue_df.loc[max_order_index, 'order_freq']
   max_year_month = summary_revenue_df.loc[max_order_index, 'year_month']

   # Mengatur Posisi Anotasi
   annotation_y_position = max_order + 2000
   annotation_x_position = max_year_month

   # Annotasi Pendaptan terbesar
   ax.annotate(f'Banyak Order Terbesar\n{max_order:.2f}', xy=(max_year_month, max_order), xytext=(annotation_x_position, annotation_y_position),
               arrowprops=dict(facecolor='red', shrink=0.05),
               ha='center', va='bottom'
               )

   # Set Label Chart
   plt.title('Banyak Order dari Tahun ke Tahun')
   plt.xlabel('Tahun-Bulan')
   plt.ylabel('Banyak Order')

   plt.xticks(rotation=45, ha='right')

   # Mengubah limit border chart
   ax.set_ylim(0, max_order + 4000) 

   return fig

def draw_jumlah_pendapatan_kategori():
   pendapatan_kategori_df_sorted = pendapatan_kategori_df.sort_values(by='revenue', ascending=False)

   # Memilih Produk dengan Top 5 Pendapatan dan Bottom 5
   top5_products = pendapatan_kategori_df_sorted.head(5)
   bottom5_products = pendapatan_kategori_df_sorted.tail(5)

   # Mangatur Dua kolom subplot
   fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(16, 6))

   # Membuat Plot untuk Top 5 Produk dengan Revenue Terbesar
   sns.barplot(x='revenue', y='product_category_name', data=top5_products, palette='viridis', ax=axes[0][0])
   axes[0][0].set_title('Top 5 Produk Menghasilkan Pendapatan Terbesar')
   axes[0][0].set_xlabel('Pendapatan (BRL)')
   axes[0][0].set_ylabel('Kategori Produk')

   # Membuat Plot untuk Top Bottom 5 Produk dengan pendapatan terendah
   sns.barplot(x='revenue', y='product_category_name', data=bottom5_products, palette='viridis', ax=axes[0][1], order=bottom5_products['product_category_name'][::-1])
   axes[0][1].set_title('Top 5 Produk Menghasilkan Pendapatan Terkecil')
   axes[0][1].set_xlabel('Pendapatan (BRL)')
   axes[0][1].set_ylabel('Kategori Produk')

   # Membuat Plot Jumlah Order Top 5 Produk dengan pendapatan terbesar
   sns.barplot(x='order_freq', y='product_category_name', data=top5_products, palette='viridis', ax=axes[1][0])
   axes[1][0].set_title('Top 5 Produk Menghasilkan Pendapatan Terbesar')
   axes[1][0].set_xlabel('Jumlah Order')
   axes[1][0].set_ylabel('Kategori Produk')

   # Membuat Plot Jumlah Order Top Bottom 5 Produk dengan pendapatan terendah
   sns.barplot(x='order_freq', y='product_category_name', data=bottom5_products, palette='viridis', ax=axes[1][1], order=bottom5_products['product_category_name'][::-1])
   axes[1][1].set_title('Top 5 Produk Menghasilkan Pendapatan Terkecil')
   axes[1][1].set_xlabel('Jumlah Order')
   axes[1][1].set_ylabel('Kategori Produk')

   plt.tight_layout()

   return fig

def draw_jumlah_pendapatan_seller():
   pendapatan_seller_df_sorted = pendapatan_seller_df.sort_values(by='revenue', ascending=False)

   # Memilih Produk dengan Top 5 Pendapatan dan Bottom 5
   top5_seller = pendapatan_seller_df_sorted.head(5)
   bottom5_seller = pendapatan_seller_df_sorted.tail(5)

   # Mangatur Dua kolom subplot
   fig, axes = plt.subplots(nrows=4, ncols=1, figsize=(16, 32))

   # Membuat Plot untuk Top 5 Seller dengan Revenue Terbesar
   sns.barplot(x='revenue', y='seller_id', data=top5_seller, palette='viridis', ax=axes[0])
   axes[0].set_title('Top 5 Seller Menghasilkan Pendapatan Terbesar')
   axes[0].set_xlabel('Pendapatan (BRL)')
   axes[0].set_ylabel('Seller ID')

   # Membuat Plot untuk Top Bottom 5 Seller dengan pendapatan terendah
   sns.barplot(x='revenue', y='seller_id', data=bottom5_seller, palette='viridis', ax=axes[1], order=bottom5_seller['seller_id'][::-1])
   axes[1].set_title('Top 5 Seller Menghasilkan Pendapatan Terkecil')
   axes[1].set_xlabel('Pendapatan (BRL)')
   axes[1].set_ylabel('Seller ID')

   # Membuat Plot Jumlah Order Top 5 Seller dengan pendapatan terbesar
   sns.barplot(x='order_freq', y='seller_id', data=top5_seller, palette='viridis', ax=axes[2])
   axes[2].set_title('Top 5 seller Menghasilkan Pendapatan Terbesar')
   axes[2].set_xlabel('Jumlah Order')
   axes[2].set_ylabel('Seller ID')

   # Membuat Plot Jumlah Order Top Bottom 5 Seller dengan pendapatan terendah
   sns.barplot(x='order_freq', y='seller_id', data=bottom5_seller, palette='viridis', ax=axes[3], order=bottom5_seller['seller_id'][::-1])
   axes[3].set_title('Top 5 seller Menghasilkan Pendapatan Terkecil')
   axes[3].set_xlabel('Jumlah Order')
   axes[3].set_ylabel('Seller ID')

   return fig

st.header('Analisis Data E-Commerce Public Dataset 🏪')
st.subheader('Project Akhir Belajar Analis Data dengan Pyton - Bangkit 2024')
st.markdown('Berikut merupakan hasil analisis data E-Commerce Dataset untuk memenuhi tugas akhir course Belajar Analis Data dengan Pytho pada platform Dicoding')

# Inisisasi Data yang sudah disimpan pada csv
summary_revenue_df = pd.read_csv('./summary_revenue.csv')
pendapatan_kategori_df = pd.read_csv('./pendapatan_kategori.csv')
pendapatan_seller_df = pd.read_csv('./pendapatan_seller.csv')

with st.sidebar:
   st.image('.\shopping_cart_PNG38.png')
   
   # Get unique years and months
   unique_years = summary_revenue_df['year'].unique()
   unique_months = summary_revenue_df['month'].unique()

   # Pilih Awal Interval Tahun
   selected_start_year = st.selectbox('Pilih Interval Awal Tahun', unique_years)

   # Pilih Awal Interval Bulan
   selected_start_month = st.selectbox('Pilih Interval Awal Bulan', unique_months)

   st.markdown("""---""")

   # Pilih Awal Interval Tahun

   # Ubah interval akhir berdasarkan inputan user pada interval awal
   unique_years = [year for year in unique_years if year >= selected_start_year]
   unique_months = [month for month in unique_months if (month >= selected_start_month and selected_start_year == unique_years[0]) or selected_start_year != unique_years[0]]

   selected_end_year = st.selectbox('Pilih Interval Akhir Tahun', unique_years)
   # Pilih Awal Interval Bulan
   selected_end_month = st.selectbox('Pilih Interval Akhir Bulan', unique_months)

# Filtering the data based on the selected start and end year and month
filtered_data = summary_revenue_df[
    (summary_revenue_df['year'] > selected_start_year) & (summary_revenue_df['year'] < selected_end_year) |
    ((summary_revenue_df['year'] == selected_start_year) & (summary_revenue_df['month'] >= selected_start_month)) |
    ((summary_revenue_df['year'] == selected_end_year) & (summary_revenue_df['month'] <= selected_end_month))
]

st.subheader('Summary Order')
col1, col2 = st.columns(2)

with col1:
   total_order = filtered_data.order_freq.sum()
   st.metric("Jumlah Order", value=total_order)

with col2:
   total_pendapatan = filtered_data.revenue.sum()
   st.metric("Total Pendapatan", value=total_pendapatan)

fig1 = summary_revenue_line_chart(summary_revenue_df = filtered_data)
st.markdown('### Total pendapatan Dari Tahun ke Tahun')
st.pyplot(fig1)

fig2 = summary_total_order_line_chart(summary_revenue_df = filtered_data)
st.markdown('### Total Order Dari Tahun ke Tahun')
st.pyplot(fig2)

col3, col4 = st.columns(2)

with col3:
   best_seller = pendapatan_kategori_df.sort_values(by='revenue', ascending=False).head(1)['product_category_name'].to_string()
   st.metric("Produk dengan Pendapatan Terbanyak", value=best_seller[3:])

with col4:
   worst_seller = pendapatan_kategori_df.sort_values(by='revenue').head(1)['product_category_name'].to_string()
   st.metric("Produk dengan Pendapatan Terendah", value=worst_seller[3:])


fig3 = draw_jumlah_pendapatan_kategori()
st.markdown('### Pendapatan Berdasarkan Kategori Produk')
st.pyplot(fig3)

col5, col6 = st.columns(2)

with col5:
   seller_terlaris = pendapatan_seller_df.sort_values(by='revenue', ascending=False).head(1)['seller_id'].to_string()
   st.metric("Seller Dengan Penddapatan Terbesar", value=seller_terlaris[4:])

with col6:
   seller_tersepi = pendapatan_seller_df.sort_values(by='revenue').head(1)['seller_id'].to_string()
   st.metric("Seller Dengan Penddapatan Terendah", value=seller_tersepi[4:])


fig4 = draw_jumlah_pendapatan_seller()
st.markdown('### Pendapatan Berdasarkan Seller')
st.pyplot(fig4)