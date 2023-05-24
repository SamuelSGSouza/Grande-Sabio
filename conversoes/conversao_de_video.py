from moviepy.editor import *

def convert_to_mp4(input_path, output_path):
    video = VideoFileClip(input_path)
    video.write_videofile(output_path)

# exemplo de uso
convert_to_mp4("conversoes/video.mkv", "arquivo.mp4")