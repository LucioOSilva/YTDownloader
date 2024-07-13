from pytube import YouTube, Stream
import ffmpeg
import re
import os

# HERE YOU CAN ADD THE LIST OF THE VIDEOS THAT YOU WANT TO DOWNLOAD:.
pathsList = []

#example:
# pathsList = [
# 	"https://youtu.be/56Lpuiq3l5Y",
# 	"https://youtu.be/10HuNg1wZBA"
# ]

def download_audio(yt: YouTube):
	streams = yt.streams.filter(only_audio=True)
	sorted_streams = sorted(
			streams,
			key=lambda s: (s.mime_type != 'audio/mp4', -int(s.abr[:-4])),
			reverse=False
	)
	topStream = sorted_streams[0]
	default_filename = topStream.download()
	new_filename = yt.title + '_audio.mp4'
	os.rename(default_filename, new_filename)
	print(f"Downloaded and renamed to: {new_filename}")

def download_video(yt: YouTube):
	streams: list[Stream] = yt.streams.filter(file_extension='mp4')
	valid_streams = [s for s in streams if s.resolution]
	sorted_streams = sorted(valid_streams, key=lambda s: int(s.resolution.split('p')[0]), reverse=True)
	topStream = sorted_streams[0]
	default_filename = topStream.download()
	new_filename = yt.title + '_video.mp4'
	os.rename(default_filename, new_filename)
	print(f"Downloaded and renamed to: {new_filename}")

def unite_video_and_audio(file_name):
	videos_dir = 'videos'
	os.makedirs(videos_dir, exist_ok=True)
	video_file = f'{file_name}_video.mp4'
	audio_file = f'{file_name}_audio.mp4'
	video_stream = ffmpeg.input(video_file)
	audio_stream = ffmpeg.input(audio_file)
	output_path = os.path.join(videos_dir, f'_done_{file_name}.mp4')
	ffmpeg.concat(video_stream, audio_stream, v=1, a=1).output(output_path).run()
	os.remove(video_file)
	os.remove(audio_file)
	print(f"Finished video saved to: {output_path}")
	print(f"Removed temporary files: {video_file} and {audio_file}")


def start():
	totalVideos = len(pathsList)
	totalDone = 0
	successfulDownloads = []

	while totalDone < totalVideos:
		try:
			for path in pathsList:
				if path in successfulDownloads:
					continue  #skip the videos that are already succesfully downloaded
				totalDone += 1
				yt = YouTube(path)
				download_audio(yt)
				download_video(yt)
				unite_video_and_audio(yt.title)
				successfulDownloads.append(path)  #mark the video succesfully downloaded

		except Exception as e:
			totalDone -= 1
			print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
			print("Fail to dowwnload:", yt.title)
			print("url:", path)
			print("error:", e)
			print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
	print("======================================================================")
	print("videos amount:", totalVideos,)
	print("videos converted:", totalDone)
	print("======================================================================")
	print("All downloads finished check the folder 'videos' and enjoy.")

if __name__ == '__main__':
	start()