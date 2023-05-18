
columns=["Country","confirmed","deaths","recovered","active","newcases","newdeaths","newrecovered","a","b","c","d","e","f","WHOregion"]
x= pd.read_csv("country_wise_latest.csv",usecols=columns)
print("Contents: ",x)
plt.scatter(x.Country,x.confirmed,x.deaths,x.recovered,x.active,x.newcases,x.newdeaths,x.newrecovered,x.a,x.b,x.c,x.d,x.e,x.f,x.WHOregion)
plt.show()