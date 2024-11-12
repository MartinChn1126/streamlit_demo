import streamlit as st
import cv2
import time


with st.empty():
	start_button = st.button('start sample')

	if start_button:
		camera = cv2.VideoCapture(0)

		with st.container():
			stop_button = st.button('stop')

			with st.empty():
				while not stop_button:
					ret,image = camera.read()
					st.image(image,channels='BGR',use_container_width=True)
					time.sleep(0.02)

				else:
					camera.release()


with st.empty():
	start = st.button('start')
	if start:
		with st.container():
			st.camera_input('Capture image')
			stop = st.button('stop')
			if stop:
				st.write(None)