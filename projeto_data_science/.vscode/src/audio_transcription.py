import speech_recognition as sr

def transcrever_audio(caminho_arquivo):
    # Criar um reconhecedor
    recognizer = sr.Recognizer()

    # Carregar o arquivo de áudio
    with sr.AudioFile(caminho_arquivo) as source:
        # Ler o arquivo de áudio
        audio = recognizer.record(source)

    try:
        # Usar o Google Speech Recognition para transcrever
        texto = recognizer.recognize_google(audio, language="pt-BR")
        return texto
    except sr.UnknownValueError:
        return "Erro: Google Speech Recognition não conseguiu entender o áudio"
    except sr.RequestError as e:
        return f"Erro: Não foi possível requisitar resultados do Google Speech Recognition; {e}"

# Exemplo de uso
if __name__ == "__main__":
    caminho_do_arquivo = "caminho/para/seu/audio.wav"
    resultado = transcrever_audio(caminho_do_arquivo)
    print(f"Transcrição: {resultado}")