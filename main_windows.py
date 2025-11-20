import os
import glob
import tkinter as tk
import customtkinter as ctk
from time import sleep

# Funciones #
def limpiar_consola():
    _ = os.system("cls")

def limpiar_texto(eleccion):
    mp3_en_dir = glob.glob(f"*.{eleccion}")
    for archivo in mp3_en_dir:
        if "[" in archivo:
            index = archivo.find("[")
            punto = archivo.rfind(".")
            nuevo_nombre = archivo[:index].strip() + archivo[punto:]
            os.rename(archivo, nuevo_nombre)

# Variables #
text = "&list="
varios = input("Varios urls? (y/n)").lower()

if varios == "y":
    # Caso varias #
    print("Caso varias")
    urls = []
    while varios:
        print(f"Current urls: {urls}")
        entrada = (input("Urls (Una por una) 'q' para detener: "))
        urls.append(entrada)
        limpiar_consola()
        if entrada.lower() == "q":
            break
    
    for url in urls:
        
        if url == "q":
            break
        
        if text in url:
            index = url.find(text)
            url = url[:index]

        print(f"Url actual: {url}")
        print("Opciones: (mp3/mp4/aac/mkv)")
        eleccion = input("Formato: ")
        formato = f"-t {eleccion}"
        arg_adicionales = input("Argumentos adicionales: ")
        sleep(0.5)
        limpiar_consola()

        os.system(f"ytdl {url} {formato} {arg_adicionales}")
        sleep(0.5)
        limpiar_consola()
        limpiar_texto(eleccion)
        

elif varios == "n":
    # Caso una #
    print("Caso una")
    url = input("URL= ")
    if text in url:
        index = url.find(text)
        url = url[:index]
    
    print(f"Url actual: {url}")
    print(" Opciones: (mp3/mp4/aac/mkv)")
    eleccion = input("Formato: ")
    formato = f"-t {eleccion}"
    arg_adicionales = input("Argumentos adicionales: ")
    sleep(0.5)
    limpiar_consola()

    os.system(f"ytdl {url} {formato} {arg_adicionales}")
    sleep(0.5)
    limpiar_consola()
    limpiar_texto(eleccion)