'''
Extracts audio from a video file using ffmpeg command line tool
Usage: python extract_audio.py input_file output_file
'''

import argparse
import subprocess
import os
#import ffmpeg # Unecessary to import as it is called directly from the command line

def convert_video_to_audio_ffmpeg(video_file, output_ext="mp3"):
    """Converts video to audio directly using `ffmpeg` command
    with the help of subprocess module"""
    filename, ext = os.path.splitext(video_file)
    subprocess.call(["ffmpeg", "-y", "-i", video_file, f"{filename}.{output_ext}"], 
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.STDOUT)

if __name__ == "__main__":
    # set up argument parser
    parser = argparse.ArgumentParser(description='Extract audio from a video file')
    parser.add_argument('input_file', help='path to input video file')
    parser.add_argument('output_file', help='path to output audio file')

    # parse arguments
    args = parser.parse_args()

    # Check if there are arguments, if not, ask for input
    if not args.input_file:
        print("Please specify an input file")
        input_file = input("Enter the input file path: ")
    else:
        input_file = args.input_file

    if not args.output_file:
        print("Please specify an output file")
        output_file = input("Enter the output file path: ")
    else:
        output_file = args.output_file

    # extract audio
    convert_video_to_audio_ffmpeg(args.input_file, args.output_file)

    # print success message
    print(f'Successfully extracted audio from "{args.input_file}" and saved to "{args.output_file}"')

