'''
Downloads the YouTube video
'''

from pytube import YouTube
import argparse

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")

if __name__ == "__main__":
    # set up argument parser
    parser = argparse.ArgumentParser(description='Download a YouTube video')
    parser.add_argument('link', help='link to the YouTube video')

    # parse arguments
    args = parser.parse_args()

    # Check if there are arguments, if not, ask for input
    if not args.link:
        print("Please specify a link")
        link = input("Enter the YouTube video URL: ")
    else:
        link = args.link

    Download(link)