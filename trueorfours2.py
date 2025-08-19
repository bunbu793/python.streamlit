import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
import cv2
import numpy as np
from PIL import Image

class VideoTransformer(VideoTransformerBase):
    def __init__(self):
        self.latest_frame = None

    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")

        # 最新のフレームをそのまま保存（カラー）
        self.latest_frame = img

        return img

def main():
    st.title("カメラで写真を撮ろう！")

    # WebRTCを使ってカメラ映像を表示
    webrtc_ctx = webrtc_streamer(
        key="example",
        video_transformer_factory=VideoTransformer,
        media_stream_constraints={"video": True, "audio": False},
    )

    if webrtc_ctx.video_transformer:
        # 写真を撮るボタン
        if st.button("写真を撮る"):
            img = webrtc_ctx.video_transformer.latest_frame
            if img is not None:
                st.image(img, channels="BGR")
                st.success("写真を撮りました！")

                # 保存ボタン
                if st.button("保存する"):
                    # OpenCVの画像をPILのImageに変換
                    img_pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
                    # 画像を保存
                    img_pil.save("captured_image.jpg")
                    st.success("写真を保存しました！")

if __name__ == "__main__":
    main()