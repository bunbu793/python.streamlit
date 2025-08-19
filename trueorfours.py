import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
import av

# カメラからの映像を処理するクラス
class VideoTransformer(VideoTransformerBase):
    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")
        # ここで画像処理を行うことができます
        return img

# Streamlitアプリの設定
st.title("カメラストリーミング")

# カメラストリーミングの開始
webrtc_streamer(key="example", video_transformer_factory=VideoTransformer)