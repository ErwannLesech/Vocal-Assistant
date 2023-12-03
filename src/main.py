from input import get_audio
# from whisper import get_transcript
from gpt import get_written_response
from output import get_vocal_response
from handler import get_handled_response

def main():
    transcript = get_audio()
    if transcript == None:
        print("Finished")
        return
    # transcript = get_transcript(audio_file)
    print(transcript)
    response = get_handled_response(transcript)
    if response == None:
        print("Finished")
        return
    print(response)
    get_vocal_response(response)
    print("Finished")

if __name__ == "__main__":

    while True:
        try:
            main()
        except KeyboardInterrupt:
            print("Finished")
            break
