import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

df = pd.read_csv('featured_mall_customer.csv')
# print(df.head())

scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)
# print(df_scaled[:5])

inertia = []

for k in range(1,11):
    kmeans = KMeans(n_clusters=k, random_state=0)
    kmeans.fit(df_scaled)
    inertia.append(kmeans.inertia_)

print("inertia ",inertia)

from sklearn.metrics import silhouette_score

for k in range(2, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    labels = kmeans.fit_predict(df_scaled)
    score = silhouette_score(df_scaled, labels)
    print(f"k = {k}, Silhouette Score = {score}")

plt.figure(figsize=(10,6))
plt.plot(range(1,11), inertia, marker='o')
plt.xlabel('No. of Cluster')
plt.ylabel('Inertia')
plt.title('Elbow Method')
plt.show()

kmeans = KMeans(n_clusters=5)
kmeans.fit(df_scaled)

clusters = kmeans.predict(df_scaled)
df['clusters'] = clusters
# print(df['clusters'].shape)

clus_char = df.groupby('clusters')[['Age','Annual Income (k$)','Spending Score (1-100)']].mean()
print("clus_char\n",clus_char)
print("clus size ", df['clusters'].value_counts())
print(df.head())
plt.figure(figsize=(10,6))
plt.scatter(df['Annual Income (k$)'],
            df['Spending Score (1-100)'],
            c=df['clusters'],
            s=50)
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.title('Customer Segment')
plt.show()