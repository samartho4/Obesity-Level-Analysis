
def categorize_weight(row):
    bmi = row['Weight'] / (row['Height'] ** 2)
    if bmi < 18.5:
        return 'Underweight'
    elif 18.5 <= bmi < 25:
        return 'Normal'
    elif 25 <= bmi < 30:
        return 'Overweight'
    elif 30 <= bmi < 35:
        return 'Obesity I'
    elif 35 <= bmi < 40:
        return 'Obesity II'
    else:
        return 'Obesity III'

def add_weight_category(df):
    df['Weight_Category'] = df.apply(categorize_weight, axis=1)
    return df
