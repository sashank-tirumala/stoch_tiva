import pandas as pd 
df = pd.read_csv('data.txt')

for i, row in df.iterrows():
    leg1_x = row['leg1_x']
    leg1_y = row['leg1_y']
    leg2_x = row['leg2_x']
    leg2_y = row['leg2_y']
    if(leg1_y > -0.145 or leg1_y < -0.245):
        print('Invalid point (Y): ',leg1_x,leg1_y)
    else:
        if(leg1_x > -1*(leg1_y+0.01276)/1.9737 or leg1_x < 1*(leg1_y+0.01276)/1.9737):
            print('Invalid point (X): ',leg1_x,leg1_y)
    if(leg2_y > -0.145 or leg2_y < -0.245):
        print('Invalid point (Y): ',leg2_x,leg2_y)
    else:
        if(leg2_x > -1*(leg2_y+0.01276)/1.9737 or leg2_x < 1*(leg2_y+0.01276)/1.9737):
            print('Invalid point (X): ',leg2_x,leg2_y)
print("all valid")