# # ts에서 모델 불러오기
# # pip install tensorflow
#
# import tensorflow as tf  # 메가 트랜드: AI, LLaMa
#
# def load_model():
#     model = tf.keras.applications.MobileNetV2(weights="imagenet")
#     print("Success to load model")
#     return model
#
# model = load_model()

# 민호님 코드
import tensorflow as tf

def load_model():
    model = tf.keras.applications.MobileNetV2(weights='imagenet')
    print('Success to load model')
    return model

model = load_model()

# 노션 코드 안됨
# import tensorflow as tf
#
# def load_model():
#     model = tf.keras.applications.MobileNetV2(weights="imagenet")
#     print("Model loaded")
#     return model
#
# model = load_model()