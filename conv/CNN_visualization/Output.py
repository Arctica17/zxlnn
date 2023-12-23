from moviepy.editor import VideoFileClip, CompositeVideoClip

video1 = VideoFileClip('textscene.mp4')
video2 = VideoFileClip('basicscene.mp4')

video2_resized = video2.resize(video1.size)

composite = CompositeVideoClip([video1, video2_resized.set_position(("center", "center"))])

composite.duration = max(video1.duration, video2.duration)

composite.write_videofile("Output.mp4", codec='libx264', audio_codec='aac')
