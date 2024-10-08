import os
from moviepy.editor import VideoFileClip, AudioFileClip

def read_file(file_type):
    while True:
        file_path = input(f"Enter the path to the {file_type} file: ")
        if os.path.exists(file_path):
            return file_path
        print(f"File not found. Please enter a valid path to a {file_type} file.")

def convert_video_to_mp3(video_path):
    try:
        video = VideoFileClip(video_path)
        audio = video.audio
        output_path = os.path.splitext(video_path)[0] + ".mp3"
        audio.write_audiofile(output_path)
        audio.close()
        video.close()
        return output_path
    except Exception as e:
        print(f"Error converting video to mp3: {e}")
        return None

def convert_music_to_mp4(music_path):
    try:
        audio = AudioFileClip(music_path)
        output_path = os.path.splitext(music_path)[0] + ".mp4"
        audio.write_videofile(output_path, fps=1)
        audio.close()
        return output_path
    except Exception as e:
        print(f"Error converting music to mp4: {e}")
        return None

def main():
    print("Welcome to the Media Converter!")

    # Read video file
    video_path = read_file("video")

    # Read music file
    music_path = read_file("music")

    # Convert video to mp3
    print("Converting video to mp3...")
    mp3_output = convert_video_to_mp3(video_path)

    # Convert music to mp4
    print("Converting music to mp4...")
    mp4_output = convert_music_to_mp4(music_path)

    # Output converted files
    print("\nConversion Results:")
    if mp3_output:
        print(f"Video converted to MP3: {mp3_output}")
    if mp4_output:
        print(f"Music converted to MP4: {mp4_output}")

    print("Thank you for using the Media Converter!")

if __name__ == "__main__":
    main()
