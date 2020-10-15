import numpy as np
import pandas as pd
from google.cloud import storage
from sklearn import linear_model

BUCKET_NAME = "TODO"
PATH_INSIDE_BUCKET = "TODO"

# Model version (folder name where the *.joblib is soted in the bucket)
MODEL_VERSION = "v1"


def get_data():
    """method to get the training data (or a portion of it) from google cloud bucket"""
    client = storage.Client()
    df = pd.read_csv("gs://{}/{}".format(BUCKET_NAME, PATH_INSIDE_BUCKET), nrows=1000)
    return df


def compute_distance(df,
                     start_lat="pickup_latitude",
                     start_lon="pickup_longitude",
                     end_lat="dropoff_latitude",
                     end_lon="dropoff_longitude"):
    lat_1_rad, lon_1_rad = np.radians(df[start_lat].astype(float)), np.radians(df[start_lon].astype(float))
    lat_2_rad, lon_2_rad = np.radians(df[end_lat].astype(float)), np.radians(df[end_lon].astype(float))
    dlon = lon_2_rad - lon_1_rad
    dlat = lat_2_rad - lat_1_rad

    a = np.sin(dlat / 2.0) ** 2 + np.cos(lat_1_rad) * np.cos(lat_2_rad) * np.sin(dlon / 2.0) ** 2
    c = 2 * np.arcsin(np.sqrt(a))
    return 6371 * c


def preprocess(df):
    """method that pre-process the data"""
    df["distance"] = compute_distance(df)
    X_train = df[["distance"]]
    y_train = df["fare_amount"]
    return X_train, y_train


def train_model(X_train, y_train):
    """method that trains the model"""
    clf = linear_model.Lasso(alpha=0.1)
    clf.fit(X_train, y_train)
    print("trained model")
    return clf


def save_model(reg):
    """Save the model into a .joblib and upload it on Google Storage /models folder
    HINTS : use sklearn.joblib (or jbolib) libraries and google-cloud-storage"""
    from sklearn.externals import joblib
    local_model_name = 'model.joblib'
    joblib.dump(reg, local_model_name)

    client = storage.Client().bucket(BUCKET_NAME)

    storage_location = '{}/{}/{}/{}'.format(
        'models',
        'taxi_fare_model',
        MODEL_VERSION,
        local_model_name)
    blob = client.blob(storage_location)
    blob.upload_from_filename(local_model_name)
    print("uploaded model")


df = get_data()
X_train, y_train = preprocess(df)
reg = train_model(X_train, y_train)
save_model(reg)
