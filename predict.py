# # 이미지 예측하기 전에 모델이 필요하다.
# # 모델 -> Tensorflow에서 다운 받아서 불러오도록 하겠다.
# # Tensorflow -> 이미지 모델 불러오기
#
# # 이미지 관련 모듈을 사용해야 한다. Pillow
#
# from PIL.Image import Image  # pip install pillow
# import numpy as np
# from model_loader import model
# import tensorflow as tf
#
# # from tensorflow.keras.applications.imagenet_utils import decode_predictions
#
# # AI가 이해할 수 있는 데이터로 변경을 해줘야 한다. => numpy
# def predict(image: Image):
#     image = np.asarray(Image.resize((224, 224)))[..., :3]  # RGB 값으로만 색을 선택하겠다.
#     image = np.expand_dims(image, 0)  # 차원을 확장 -> 이미지가 2차원 -> 3차원으로 변경
#     image = image / 127.5 - 1.0  # Scaler(정규화) -> 이미지 데이터가 -1 ~ 1 형태의 값으로 정규화 됨.
#
#     results = tf.keras.applications.imagenet_utils.decode_predictions(model.predict(image), 3)[0]
#     print('results:', results)
#
#     result_list = []
#     for i in results:
#         result_list.append({"class": i[1], "confidence": f"{i[2] * 100:0.2f}%"})
#
#     return result_list

# 민호님 코드
from PIL.Image import Image # pip install pillow
import numpy as np
from model_loader import model
import tensorflow as tf
# from tensorflow.keras.applications.imagenet_utils import decode_predictions
# AI가 이해할 수 있는 데이터로 변경을 해줘야 한다. -> numpy로
def predict(image: Image):
    image = np.asarray(image.resize((224, 224)))[..., :3] # RGB 컬러로 사용한다
    image = np.expand_dims(image, 0) # 차원을 확장 -> 이미지가 2차원인데 3차원으로 변경
    image = image / 127.5 - 1.0 # Scaler(정규화) -> 이미지 데이터가 -1 ~ 1 형태의 값으로 정규화 됨

    results = tf.keras.applications.imagenet_utils.decode_predictions(model.predict(image), 3)[0]
    print('results :', results)

    result_list = []
    for i in results:
        result_list.append({'class': i[1], 'confidence': f'{i[2]*100:0.2f}%'})

    return result_list


# 노션 코드 안됨
# from PIL.Image import Image
# import numpy as np
# from tensorflow.keras.applications.imagenet_utils import decode_predictions
# from model_loader import model
#
#
# # 이미지를 예측해서 결과를 알려주는 함수
# def predict(image: Image):
#     image = np.asarray(image.resize((224, 224)))[..., :3] # RGB
#     image = np.expand_dims(image, 0)
#     image = image / 127.5 - 1.0 # -1~1사이의 숫자로 바뀌는데 -> Scaler(정규화)
#     result = decode_predictions(model.predict(image), 3)[0] # 2: 상위 2개의 결과 반환
#
#     result_list = []
#     for res in result:
#         print(res)
#         result_list.append({"class": res[1], "confidence": f"{res[2]*100:0.2f} %"})
#
#     return result_list