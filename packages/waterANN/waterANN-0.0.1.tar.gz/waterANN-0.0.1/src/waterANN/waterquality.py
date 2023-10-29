#라이브러리 임포트
def import_library():
  import pandas as pd 
  import numpy as np 

  import matplotlib.pyplot as plt
  import seaborn as sns

  import plotly.offline as py
  py.init_notebook_mode(connected=True)
  import plotly.graph_objs as go
  import plotly.tools as tls
  import plotly.figure_factory as ff

  from sklearn.model_selection import train_test_split
  from sklearn.preprocessing import MinMaxScaler

  import tensorflow as tf
  from tensorflow.keras.models import Sequential
  from tensorflow.keras.layers import Dense, Activation,Dropout

#heatmap
def heatmap_plot(df):
  import matplotlib.pyplot as plt
  import seaborn as sns
  fig, ax = plt.subplots(figsize = (18,18))
  sns.heatmap(df.corr(), ax = ax, annot = True)

#결측치 처리, train_test split, scaling
def preprocessing(df):
  from sklearn.preprocessing import MinMaxScaler
  from sklearn.model_selection import train_test_split
  df['ph'].fillna(value=df['ph'].median(), inplace=True)
  df['Trihalomethanes'].fillna(value=df['Trihalomethanes'].median(),inplace=True)
  df['Sulfate'].fillna(value=df['Sulfate'].median(), inplace=True)
  print("데이터 전처리 완료")

  X=df.drop('Potability', axis=1).values
  y=df['Potability'].values
  X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3, random_state=40)
  print("train test split 완료")

  scaler=MinMaxScaler()
  scaler.fit(X_train)
  X_train=scaler.transform(X_train)
  X_test=scaler.transform(X_test)
  print("Scaling 완료")
  print()

  print('training shape : ',X_train.shape)
  print('testing shape: ',X_test.shape)
  return X_train, X_test, y_train, y_test

#model 정의
def define_model():
  from tensorflow.keras.models import Sequential
  from tensorflow.keras.layers import Dense, Activation,Dropout
  model = Sequential() # Initialising the ANN
  model.add(Dense(units = 128, kernel_initializer = 'uniform', activation = 'tanh'))
  model.add(Dense(units = 64, kernel_initializer = 'uniform', activation = 'tanh'))
  model.add(Dense(units = 32, kernel_initializer = 'uniform', activation = 'tanh'))
  model.add(Dense(units = 16, kernel_initializer = 'uniform', activation = 'tanh'))
  model.add(Dense(units = 1, kernel_initializer = 'uniform', activation = 'sigmoid'))
  model.compile(optimizer = 'adam', loss = 'binary_crossentropy')
  print("모델 정의 완료")
  return model

#model 훈련
def train_model(model, X_train, y_train, X_test, y_test):
  import pandas as pd
  model.fit(x=X_train, y=y_train, epochs=300, validation_data=(X_test, y_test), verbose=1)
  print("모델 훈련 완료")

  model_loss = pd.DataFrame(model.history.history)
  model_loss.plot()
  return model

#model 평가
def evaluate_model(model, X_test, y_test):
  from sklearn.metrics import classification_report, confusion_matrix
  from sklearn.metrics import confusion_matrix
  y_pred = model.predict(X_test)
  y_pred = [ 1 if y>=0.5 else 0 for y in y_pred ]
  print("classification report: ")
  print(classification_report(y_test,y_pred))
  print()

  cm = confusion_matrix(y_test, y_pred)
  print("confusion matrix: ")
  print(cm)
  print()

  accuracy = (cm[0][0]+cm[1][1])/(cm[0][0]+cm[0][1]+cm[1][0]+cm[1][1])
  print("Accuracy: "+ str(accuracy*100)+"%")