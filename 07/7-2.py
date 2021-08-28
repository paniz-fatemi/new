from moviepy import editor
video = editor.VideoFileClip("Kakegurui_xx_OP_Kakegurui_Season_2_Opening_HD_KU3QM1pJffs_247.mp4.mkv")
video.audio.write_audiofile("Kakegurui_xx_OP_Kakegurui_Season_2_Opening_HD_KU3QM1pJffs_247.mp3")