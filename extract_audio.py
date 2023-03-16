import argparse
import ffmpeg

# set up argument parser
parser = argparse.ArgumentParser(description='Extract audio from a video file')
parser.add_argument('input_file', help='path to input video file')
parser.add_argument('output_file', help='path to output audio file')

# parse arguments
args = parser.parse_args()

# create a stream object for the audio in the input file
stream = ffmpeg.input(args.input_file)

# extract audio from the stream object
audio = stream.audio

# save the audio to the output file
ffmpeg.output(audio, args.output_file).run()

# print success message
print(f'Successfully extracted audio from "{args.input_file}" and saved to "{args.output_file}"')
