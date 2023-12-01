from input import get_input
from whisper import get_transcript
from gpt import get_written_response
from output import get_vocal_response

audio_file = "input.wav"

def main():
    get_input(audio_file)
    transcript = get_transcript(audio_file)
    print(transcript)
    response = get_written_response(transcript)
    print(response)
    get_vocal_response(response)
    print("Finished")

main()