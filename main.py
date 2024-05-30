# import tkinter
# def add_digit(digit):
#     value=calc.get()
#     if value[0]=='0':
#         value=value[:-1]
#     calc.delete(0,tkinter.END)
#     calc.insert(0,value+digit)
#
# def add_operetion(operetion):
#     value=calc.get()
#     if value[-1] in '-+/*':
#         value=value[:-1]
#     elif '+' in value or '-' in value or '/' in value or '*' in value:
#         calculate()
#         value=calc.get()
#     calc.delete(0,tkinter.END)
#     calc.insert(0,value+operetion)
# def make_digit_batton(digit):
#     return tkinter.Button(text=digit,bd=5,font=('Arial,13'), command=lambda : add_digit(digit))
#
# def make_operetion_batton(operetion):
#     return tkinter.Button(text=operetion,bd=5,font=('Arial,13'), command=lambda : add_operetion(operetion))
# def calculate():
#     value = calc.get()
#     if value[-1] in '-+/*':
#         value=value+value[:-1]
#     calc.delete(0, tkinter.END)
#     calc.insert(0,eval(value))
# def make_calc_batton(operetion):
#     return tkinter.Button(text=operetion,bd=5,font=('Arial,13'), command=calculate)
#
# def clear():
#     value = calc.get()
#     calc.delete(0, tkinter.END)
#     calc.insert(0,0)
# def make_clear_batton(operetion):
#     return tkinter.Button(text=operetion,bd=5,font=('Arial,13'), command=clear)
#
# win=tkinter.Tk()
# win.title('КАЛЬКУЛЯТОР')
# win.geometry("240x270+600+100")
# win.resizable(False,False)
# win.config(background='#A200FF')
#
# calc=tkinter.Entry(win,justify=tkinter.RIGHT,font=('Arial,15'),width=15)
# calc.insert(0,'0')
# calc.grid(row=0,column=0,columnspan=4,stick='we',padx=5)
#
# make_digit_batton('1').grid(row=1,column=0,stick='wens',padx=5,pady=5)
# make_digit_batton('2').grid(row=1,column=1,stick='wens',padx=5,pady=5)
# make_digit_batton('3').grid(row=1,column=2,stick='wens',padx=5,pady=5)
# make_digit_batton('4').grid(row=2,column=0,stick='wens',padx=5,pady=5)
# make_digit_batton('5').grid(row=2,column=1,stick='wens',padx=5,pady=5)
# make_digit_batton('6').grid(row=2,column=2,stick='wens',padx=5,pady=5)
# make_digit_batton('7').grid(row=3,column=0,stick='wens',padx=5,pady=5)
# make_digit_batton('8').grid(row=3,column=1,stick='wens',padx=5,pady=5)
# make_digit_batton('9').grid(row=3,column=2,stick='wens',padx=5,pady=5)
# make_digit_batton('0').grid(row=4,column=0,stick='wens',padx=5,pady=5)
#
# make_operetion_batton('+').grid(row=1,column=3,stick='wens',padx=5,pady=5)
# make_operetion_batton('-').grid(row=2,column=3,stick='wens',padx=5,pady=5)
# make_operetion_batton('/').grid(row=3,column=3,stick='wens',padx=5,pady=5)
# make_operetion_batton('*').grid(row=4,column=3,stick='wens',padx=5,pady=5)
#
# make_calc_batton('=').grid(row=4,column=2,stick='wens',padx=5,pady=5)
# make_clear_batton('C').grid(row=4,column=1,stick='wens',padx=5,pady=5)
#
# win.grid_columnconfigure(0,minsize=60)
# win.grid_columnconfigure(1,minsize=60)
# win.grid_columnconfigure(2,minsize=60)
# win.grid_columnconfigure(3,minsize=60)
#
# win.grid_rowconfigure(1,minsize=60)
# win.grid_rowconfigure(2,minsize=60)
# win.grid_rowconfigure(3,minsize=60)
# win.grid_rowconfigure(4,minsize=60)
#
# win.mainloop()








# import flet as ft
# import requests
# def main(page: ft.Page):
#     page.title = "ПОГОДА"
#     page.vertical_alignment = ft.MainAxisAlignment.CENTER
#
#     user_data = ft.TextField(label='введите город', width=400)
#
#     weather_data=ft.Text('')
#
#     def get_info(e):
#
#         if len(user_data.value)<2:
#             return
#
#         API= '2d8d3cdce881fc74bf54ff7ffe8d0c44'
#         URL=f'https://api.openweathermap.org/data/2.5/weather?q={user_data.value}&appid={API}&units=metric'
#         res= requests.get(URL).json()
#         temp=res['main']['temp']
#         weather_data.value='температура:'+str(temp)
#         page.update()
#
#     page.add(
#         ft.Row([user_data], alignment=ft.MainAxisAlignment.CENTER),
#         ft.Row([weather_data], alignment=ft.MainAxisAlignment.CENTER),
#         ft.Row([ft.ElevatedButton(text='получить', on_click=get_info)], alignment=ft.MainAxisAlignment.CENTER)
#     )
#
# ft.app(target=main)



import tkinter as tk
from tkinter import filedialog
import sounddevice as sd
import numpy as np
import wave

class DictaphoneApp:
    def __init__(self, master):
        self.master = master
        master.title("Dictaphone")


        self.recording = False
        self.duration = 10
        self.fs = 44100
        self.recordings = []


        self.start_button = tk.Button(master, text="начать запись", font=("Arial", 20), bg="#D8BFD8", command=self.start_recording)
        self.start_button.pack(pady=20)

        self.stop_button = tk.Button(master, text="закончить", font=("Arial", 20), bg="#D8BFD8", command=self.stop_recording)
        self.stop_button.pack(pady=20)

        self.save_button = tk.Button(master, text="сохранить звук", font=("Arial", 20), bg="#D8BFD8", command=self.save_recording)
        self.save_button.pack(pady=20)


        self.adjust_window_size()

    def start_recording(self):
        if not self.recording:
            self.recording = True
            self.recordings.append(np.zeros((int(self.duration * self.fs),)))
            with sd.InputStream(samplerate=self.fs, channels=1) as stream:
                print("Recording...")
                for i, sample in enumerate(stream):
                    self.recordings[-1][i] = sample
                self.recording = False
                print("Finished recording.")
        else:
            print("Already recording.")

    def stop_recording(self):
        if self.recording:
            self.recording = False
            print("Stopped recording.")
        else:
            print("Not recording.")

    def save_recording(self):
        if len(self.recordings) > 0:
            filename = filedialog.asksaveasfilename(defaultextension=".wav")
            if filename:
                wf = wave.open(filename, 'wb')
                wf.setnchannels(1)
                wf.setsampwidth(sd.default.samplerate // 2)
                wf.setframerate(self.fs)
                wf.writeframes(self.recordings[0])
                wf.close()
                self.recordings.clear()
                print(f"Saved recording to {filename}")
        else:
            print("No recording to save.")

    def adjust_window_size(self):

        self.master.after_idle(self.calculate_and_set_window_size)

    def calculate_and_set_window_size(self):

        start_button_width = self.start_button.winfo_reqwidth()
        start_button_height = self.start_button.winfo_reqheight()
        stop_button_width = self.stop_button.winfo_reqwidth()
        stop_button_width = self.stop_button.winfo_reqheight()
        save_button_width = self.save_button.winfo_reqwidth()
        save_button_height = self.save_button.winfo_reqheight()


        total_width = max(start_button_width, stop_button_width, save_button_width) + 40
        total_height = start_button_height + stop_button_height + save_button_height + 60


        self.master.geometry(f"{total_width}x{total_height}")

if __name__ == "__main__":
    root = tk.Tk()
    app = DictaphoneApp(root)
    root.mainloop()





