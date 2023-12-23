from moviepy.editor import VideoFileClip, CompositeVideoClip

background_video = VideoFileClip('basicscene.mp4')
overlay_video = VideoFileClip('textscene.mp4')

overlay_resized = overlay_video.resize(background_video.size)

composite = CompositeVideoClip([background_video, overlay_resized.set_position(("center", "center"))])

composite.duration = max(background_video.duration, overlay_video.duration)

composite.write_videofile("Output.mp4", codec='libx264', audio_codec='aac')
