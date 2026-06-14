import subprocess
import os
import glob
from time import sleep

class mainwin:
    
    def __init__(self):
        self.text = "&list="
        self.varios = ""
        self.urls = []
        
    def set_varios(self):
        self.varios = input("Varios urls? (y/n)").lower()
 
    def limpiar_consola(self):
        subprocess.run('cls', shell=True)
    
    def limpiar_texto(self, eleccion):
        mp3_en_dir = glob.glob(f"*.{eleccion}")
        for archivo in mp3_en_dir:
            if "[" in archivo:
                index = archivo.find("[")
                punto = archivo.rfind(".")
                nuevo_nombre = archivo[:index].strip() + archivo[punto:]
                os.rename(archivo, nuevo_nombre)
                
    def _descargar_y_limpiar(self, url, ejecutable):
        if self.text in url:
            index = url.find(self.text)
            url = url[:index]
            
        print(f"Url actual: {url}")
        print("Opciones: [mp3/mp4/aac/mkv]")
        eleccion = input("Formato: ").lower().strip()
        
        if eleccion in ["mp3", "aac"]:
            formato = ["-x", "--audio-format", eleccion]
        else:
            formato = ["-t", eleccion]
            
        arg_adicionales = input("Argumentos adicionales: ").strip()
        sleep(0.5)
        self.limpiar_consola()
        
        comando = [ejecutable, url] + formato
        if arg_adicionales:
            comando.extend(arg_adicionales.split())
            
        subprocess.run(comando, shell=True)
        sleep(0.5)
        self.limpiar_consola()
        self.limpiar_texto(eleccion)
    
    def mainfunc(self):
        self.set_varios()
        if self.varios == "y":
            while self.varios:
                print(f"Current urls: {self.urls}")
                entrada = input("Urls (Una por una), escribe 'q' para detener: ")
                self.urls.append(entrada)
                self.limpiar_consola()
                if entrada.lower() == "q":
                    break
            
            for url in self.urls:
                if url == "q":
                    break
                self._descargar_y_limpiar(url, "yt-dlp")
        
        elif self.varios == "n":
            url = input("URL= ")
            self._descargar_y_limpiar(url, "yt-dlp")

if __name__ == "__main__":
    
    main = mainwin()
    main.mainfunc()