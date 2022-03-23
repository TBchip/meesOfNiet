import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from keras.models import Sequential
from keras.layers import Dense


df = pd.read_csv('data/Mees.csv')

print()
print(df)

x = df.drop(['Mees'], axis=1)
y = df['Mees']

# print()
# print(x)
# print(y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.2)

# print()
# print(x_test)
# print(y_test)
# print()
# print('len total:', len(x))
# print('len test:', len(x_test))
# print('len train:', len(x_train))

model = Sequential()
model.add( Dense(units=128, activation='relu', input_dim=len(x_train.columns)) )
model.add( Dense(units=128, activation='relu') )
model.add( Dense(units=1, activation='sigmoid') )

# print()
# print(model.weights)

model.compile(loss='binary_crossentropy', optimizer='sgd', metrics='accuracy')

model.fit(x_train, y_train, epochs=128, batch_size=64)

# print()
# print(model.weights)

test_predict = model.predict(x_test)
test_predict = [ round(i[0], 3) for i in test_predict ]
test_predict_rounded = [ 0 if i < 0.5 else 1 for i in test_predict ]

print()
print(x_test[0:3])
for i in range(3):
    print(y_test[i:i+1])
    print()
    print(test_predict[i:i+1])
    print(test_predict_rounded[i:i+1])
    print()
    print()

accuracy = accuracy_score(y_test, test_predict_rounded)

print()
print(accuracy)

model.save('tfmodel_mees')