import numpy as np
from PIL import Image
import onnxruntime as ort

mean=[0.485, 0.456, 0.406]
std=[0.229, 0.224, 0.225]

def get_session(
        model_path: str, 
        use_gpu: bool = False
    ):
    '''
    Get ONNX Runtime InferenceSession
    '''
    session = ort.InferenceSession(model_path)
    
    if use_gpu:
        providers = ['CUDAExecutionProvider']
        options = [{'device_id': '0'}]
        session.set_providers(providers, options)
    else:
        providers = ['CPUExecutionProvider']
        session.set_providers(providers)
    return session

def input_preprocess(
        image: Image.Image, 
        target_size: int
    ):
    '''
    Naive image resize and normalization
    '''
    if isinstance(image, Image.Image):
        pass
    else:
        raise TypeError('image must be PIL Image')
    # 이미지 크기 재조정
    image = image.resize((target_size, target_size))

    # 이미지를 numpy 배열로 변환
    img_array = np.array(image).astype(np.float32) / 255.0

    # 평균과 표준편차로 정규화
    img_array = (img_array - mean) / std

    # ONNX 입력 형식에 맞게 차원 변경 (NCHW format)
    img_array = img_array.transpose((2, 0, 1))
    img_array = np.expand_dims(img_array, axis=0)

    return img_array.astype(np.float32)
