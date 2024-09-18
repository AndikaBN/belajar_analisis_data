import pandas as pd
 
sample_data = {
    'name': ['John', 'Alia', 'Ananya', 'Steve', 'Ben'],
    'age': [24, 22, 23, 25, 28],  
    'communication_skill_score': [85, 70, 75, 90, 90],
    'quantitative_skill_score': [80, 90, 80, 75, 70]
}
 
df = pd.DataFrame(sample_data)

# corelation
## nampilan semua daata
print(pd.get_dummies(df).corr())
## napilan data numerik saja
print(df.corr(numeric_only=True))

print("==========================================")

# covariance
## nampilin semua data
print(pd.get_dummies(df).cov())
## nampilin numerik saja
print(df.cov(numeric_only=True))