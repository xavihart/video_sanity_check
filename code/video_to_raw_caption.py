# function for video raw captioning

MODEL_LIST = [
    'GPT-4o',
    'VILA',
]

def video_to_raw_caption(video_path, model_name, promt_path):
    assert model_name in MODEL_LIST
    pass