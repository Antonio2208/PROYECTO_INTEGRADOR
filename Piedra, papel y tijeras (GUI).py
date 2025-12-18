import random
import math

def main(input_fn=input, print_fn=print):
    print_fn()
    print_fn("Hola, como estas, en este momento vas a jugar piedra, papel o tijeras, el primer modo el facil es a la primera y el segundo modo es el dificil que es al mejor de 5 juegos")
    print_fn()


    # VALIDACIÓN DEL MODO DE JUEGO

    while True:
        entrada = input_fn("Elige el modo de juego (1) facil,(2) dificil: ")
        print_fn()

        try:
            c = float(entrada)
            if c == 1 or c == 2:
                break
            else:
                print_fn("Porfavor elije solo entre el numero (1) para modo facil y (2) para el modo dificil")
                print_fn()

        except:
            print_fn("Porfavor elije solo entre el numero (1) para modo facil y (2) para el modo dificil")
            print_fn()


    # MODO FÁCIL

    if c == 1:
        print_fn("Has elegido el modo facil, en este modo ganaras si ganas la primera ronda")
        print_fn()


        while True:
            entrada = input_fn("Elige tu jugada (1) piedra,(2) papel,(3) tijeras: ")
            print_fn() 
            try:
                jugador = float(entrada)
                if jugador == 1 or jugador == 2 or jugador == 3:
                    break
                else:
                    print_fn("Porfavor elije solo entre los numeros (1) para piedra,(2) para papel y (3) para tijeras")
                    print_fn()

            except:
                print_fn("Porfavor elije solo entre los numeros (1) para piedra,(2) para papel y (3) para tijeras")
                print_fn()


        if jugador == 1:
            textoju = "Piedra"
        elif jugador == 2:
            textoju = "Papel"
        else:
            textoju = "Tijeras"

        compu = math.floor(random.random() * 3) + 1

        if compu == 1:
            textoco = "Piedra"
        elif compu == 2:
            textoco = "Papel"
        else:
            textoco = "Tijeras"

        print_fn("-Tú elegiste " + textoju + " y la computadora eligió " + textoco)
        print_fn()


        if compu == jugador:
            print_fn("Genial no perdiste, pero tampoco ganaste, tienes un merecido empate")
            print_fn()
            print_fn()
            print_fn()
            print_fn("Fin del juego")

        elif (jugador == 1 and compu == 3) or (jugador == 2 and compu == 1) or (jugador == 3 and compu == 2):
            print_fn("Felicidades, ganaste^^")
            print_fn()
            print_fn()
            print_fn()
            print_fn("Fin del juego")

        else:
            print_fn("Ohhh, lastimosamente perdiste :c")
            print_fn()
            print_fn()
            print_fn()
            print_fn("Fin del juego")




    # MODO DIFÍCIL

    else:
        print_fn("Has elegido el modo dificil, en este modo ganaras si ganas la mayoria de las 5 rondas")  
        print_fn()

        ronda = 1
        puntosj = 0
        puntosc = 0
        empates = 0
        piedra = 0
        papel = 0
        tijeras = 0

        while ronda <= 5:

            while True:
                entrada = input_fn("Elige tu jugada (1) piedra,(2) papel,(3) tijeras: ")
                print_fn()

                try:
                    jujugador = float(entrada)
                    if jujugador == 1 or jujugador == 2 or jujugador == 3:
                        break
                    else:
                        print_fn("Porfavor elije solo entre los numeros (1) para piedra, (2) para papel y (3) para tijeras")
                        print_fn()

                except:
                    print_fn("Porfavor elije solo entre los numeros (1) para piedra, (2) para papel y (3) para tijeras")
                    print_fn()


            if jujugador == 1:
                piedra = piedra + 1
                jutexto = "Piedra"
            elif jujugador == 2:
                papel = papel + 1
                jutexto = "Papel"
            else:
                tijeras = tijeras + 1
                jutexto = "Tijeras"

            if piedra > papel and piedra > tijeras:
                jucompu = 2
            elif papel > piedra and papel > tijeras:
                jucompu = 3
            elif tijeras > piedra and tijeras > papel:
                jucompu = 1
            else:
                jucompu = math.floor(random.random() * 3) + 1

            if jucompu == 1:
                cotexto = "Piedra"
            elif jucompu == 2:
                cotexto = "Papel"
            else:
                cotexto = "Tijeras"

            print_fn("-Tú elegiste " + jutexto + " y la computadora eligió " + cotexto)
            print_fn()


            if jujugador == jucompu:
                empates = empates + 1
                print_fn("Genial no perdiste, pero tampoco ganaste, tienes un merecido empate")
                print_fn()

            elif (jujugador == 1 and jucompu == 3) or (jujugador == 2 and jucompu == 1) or (jujugador == 3 and jucompu == 2):
                puntosj = puntosj + 1
                print_fn("Felicidades, ganaste la ronda ^^")
                print_fn()

            else:
                puntosc = puntosc + 1
                print_fn("Ohhh, lastimosamente perdiste la ronda :c")
                print_fn()


            ronda = ronda + 1

        # Resultados finales de las 5 rondas
        print_fn("-Felicidades de las 5 rondas ganaste", puntosj)
        print_fn()

        print_fn("-Bueno de las 5 rondas te gane", puntosc)
        print_fn()

        print_fn("-Y por ultimo de las 5 rondas empatamos", empates)
        print_fn()


        if puntosj > puntosc:
            print_fn("Congratulations!!!!! eres el ganador")
            print_fn()
            print_fn()
            print_fn()
            print_fn("Fin del juego")

        elif puntosc > puntosj:
            print_fn("Chale hiciste lo mejor que pudiste pero perdiste ya que te gane mas rondas, suerte en la proxima")
            print_fn()
            print_fn()
            print_fn()
            print_fn("Fin del juego")

        else:
            print_fn("Un resultado que no me esperaba, acabamos de empatar, prueba de nuevo a ver si esta vez me ganas")
            print_fn()
            print_fn()
            print_fn()
            print_fn("Fin del juego")



#------------------------------------------------------------------------------------------
#  GUI integrada (Tkinter)

import sys
import threading
import queue
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

class _GuiIO:
    def __init__(self, write_callback):
        self._in_q = queue.Queue()
        self._out_q = queue.Queue()
        self._write_callback = write_callback


    def print_fn(self, *args, sep=" ", end="\n", **kwargs):
        text = sep.join(str(a) for a in args) + end
        self._out_q.put(text)


    def input_fn(self, prompt=""):
        if prompt:

            self.print_fn(prompt, end="")

        value = self._in_q.get()
        return value

    def push_input(self, value: str):
        self._in_q.put(value)

    def flush_output_to_gui(self):
        try:
            while True:
                chunk = self._out_q.get_nowait()
                self._write_callback(chunk)
        except queue.Empty:
            pass


class RPSApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Piedra, Papel o Tijeras – GUI")
        self.geometry("900x600")

        
        top = ttk.Frame(self)
        top.pack(fill="x", padx=10, pady=10)

        self.btn_start = ttk.Button(top, text="Iniciar (GUI)", command=self.start_game)
        self.btn_start.pack(side="left")

        ttk.Label(top, text="Entrada manual:").pack(side="left", padx=(20, 5))
        self.entry = ttk.Entry(top, width=30)
        self.entry.pack(side="left")
        self.entry.bind("<Return>", lambda e: self.send_entry())

        self.btn_send = ttk.Button(top, text="Enviar", command=self.send_entry)
        self.btn_send.pack(side="left", padx=(10, 0))

        
        quick = ttk.LabelFrame(self, text="Botones rápidos (envían números al programa)")
        quick.pack(fill="x", padx=10, pady=(0, 10))

        row1 = ttk.Frame(quick)
        row1.pack(fill="x", padx=10, pady=6)
        ttk.Label(row1, text="Modo:").pack(side="left")
        ttk.Button(row1, text="Fácil (1)", command=lambda: self.push("1")).pack(side="left", padx=6)
        ttk.Button(row1, text="Difícil (2)", command=lambda: self.push("2")).pack(side="left", padx=6)

        row2 = ttk.Frame(quick)
        row2.pack(fill="x", padx=10, pady=(0, 10))
        ttk.Label(row2, text="Jugada:").pack(side="left")
        ttk.Button(row2, text="Piedra (1)", command=lambda: self.push("1")).pack(side="left", padx=6)
        ttk.Button(row2, text="Papel (2)", command=lambda: self.push("2")).pack(side="left", padx=6)
        ttk.Button(row2, text="Tijeras (3)", command=lambda: self.push("3")).pack(side="left", padx=6)

       
        self.console = ScrolledText(self, wrap="word", font=("Menlo", 12))
        self.console.pack(fill="both", expand=True, padx=10, pady=(0, 10))
        self.console.configure(state="disabled")

        self._io = _GuiIO(self.write_console)
        self._thread = None

        
        self.after(50, self.pump_output)

        self.write_console(
            "Listo. Pulsa “Iniciar (GUI)”\n"
            "Luego usa botones o escribe un número y pulsa Enter para jugar\n\n"
        )

    def write_console(self, text: str):
        self.console.configure(state="normal")
        self.console.insert("end", text)
        self.console.see("end")
        self.console.configure(state="disabled")

    def pump_output(self):
        self._io.flush_output_to_gui()
        self.after(50, self.pump_output)

    def push(self, value: str):
        self.write_console(f">>> {value}\n")
        self._io.push_input(value)

    def send_entry(self):
        v = self.entry.get().strip()
        if not v:
            return
        self.entry.delete(0, "end")
        self.push(v)

    def start_game(self):
        if self._thread and self._thread.is_alive():
            self.write_console("\n El juego ya comenzo\n\n")
            return

        self.write_console("\n      Iniciando juego en la pantalla grafica GUI   q\n\n")

        def runner():
            try:
                main(input_fn=self._io.input_fn, print_fn=self._io.print_fn)
            except Exception as e:
                self._io.print_fn(f"\n[Error en ejecución]: {e}\n")

        self._thread = threading.Thread(target=runner, daemon=True)
        self._thread.start()

def run_gui():
    app = RPSApp()
    app.mainloop()


if __name__ == "__main__":
     run_gui()
