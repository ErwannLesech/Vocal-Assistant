from input import get_audio
# from whisper import get_transcript
from gpt import get_written_response
from output import generate_audio_file
from handler import get_handled_response

def main():
    transcript = get_audio()
    if transcript == None:
        print("Transcript is None")
        return
    # transcript = get_transcript(audio_file)
    print(transcript)
    response = get_handled_response(transcript)
    if response == None:
        print("Finished")
        return
    print(response)
    generate_audio_file(response)
    print("main.py: boucle finished")

if __name__ == "__main__":

    while True:
        try:
            main()
        except KeyboardInterrupt:
            print("main.py: KeyboardInterrupt")
            break
