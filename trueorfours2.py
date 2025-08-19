import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
import cv2

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
        # ボタンが押されたときに写真を撮る
        if st.button("写真を撮る"):
            img = webrtc_ctx.video_transformer.latest_frame
            if img is not None:
                st.image(img, channels="BGR")
                st.success("写真を撮りました！")

if __name__ == "__main__":
    main()