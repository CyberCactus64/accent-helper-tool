import tkinter as tk
import pyperclip # pip install pyperclip

# cambiare questa riga con il path completo della icona
icon_path = r'C:\Users\edowo\Desktop\Coding Projects\Accent Helper Tool\Graphics\Icon.ico'

# dizionario con tutte le versioni accentate di ogni vocale
VOWELS_DICT = {
	'a': ['à', 'á', 'â', 'ä', 'ã', 'å', 'ā'],
	'A': ['À', 'Á', 'Â', 'Ä', 'Ã', 'Å', 'Ā'],
	'e': ['è', 'é', 'ê', 'ë', 'ē', 'ė', 'ę'],
	'E': ['È', 'É', 'Ê', 'Ë', 'Ē', 'Ė', 'Ę'],
	'i': ['ì', 'í', 'î', 'ï', 'ī', 'į'],
	'I': ['Ì', 'Í', 'Î', 'Ï', 'Ī', 'Į'],
	'o': ['ò', 'ó', 'ô', 'ö', 'õ', 'ø', 'ō'],
	'O': ['Ò', 'Ó', 'Ô', 'Ö', 'Õ', 'Ø', 'Ō'],
	'u': ['ù', 'ú', 'û', 'ü', 'ū'],
	'U': ['Ù', 'Ú', 'Û', 'Ü', 'Ū'],
}

def copy_to_clipboard(accented_vowel):
	pyperclip.copy(accented_vowel)
	# aggiorna messaggio nella label in basso
	status_label.config(text=f"{accented_vowel} copiato negli appunti!", fg="lightgreen")
	status_label.after(3000, lambda: status_label.config(text=""))

def show_accents():
	lettera = vowels_input.get()

	# rimuove i risultati precedenti
	for widget in results_frame.winfo_children():
		widget.destroy()

	if len(lettera) != 1:
		# aggiorna messaggio nella label in basso
		status_label.config(text="Errore: Inserire una sola lettera lettera.", fg="red")
		status_label.after(3000, lambda: status_label.config(text=""))
		return
	if lettera.lower() not in VOWELS_DICT:
		# aggiorna messaggio nella label in basso
		status_label.config(text="Errore: Inserire una vocale valida.", fg="red")
		status_label.after(3000, lambda: status_label.config(text=""))
		return

	acc_vowels = VOWELS_DICT[lettera.lower() if lettera.islower() else lettera.upper()]

	# crea un pulsante per ogni variante accentata
	for acc_vowel in acc_vowels:
		btn = tk.Button(results_frame, text=acc_vowel, font=("Arial", 18), bg="gray20", fg="white", command=lambda v=acc_vowel: copy_to_clipboard(v))
		btn.pack(side=tk.LEFT, padx=5, pady=5)

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

# main window
root = tk.Tk()
root.title("Accent Helper")
root.iconbitmap(icon_path) # vedere variabile dichiarata a inizio script
root.geometry("400x180")
root.minsize(400, 180)
root.maxsize(400, 150)
center_window(root)
root.configure(bg="gray15")

# sezione input della lettera (vocale)
input_frame = tk.Frame(root, bg="gray15")
input_frame.pack(pady=10)

input_vowels_label = tk.Label(input_frame, text="Inserire una vocale:", font=("Arial", 14), bg="gray15", fg="white")
input_vowels_label.pack(side=tk.LEFT, padx=5)

vowels_input = tk.Entry(input_frame, font=("Arial", 14), width=5, bg="gray25", fg="white", insertbackground="white")
vowels_input.pack(side=tk.LEFT, padx=5)

show_button = tk.Button(input_frame, text="Mostra accenti", font=("Arial", 14), bg="gray20", fg="white", command=show_accents)
show_button.pack(side=tk.LEFT, padx=5)

# frame per le versioni accentate
results_frame = tk.Frame(root, bg="gray15")
results_frame.pack(pady=18)

# label di avviso (per quando viene copiata una lettera o quando ne viene inserita una sbagliata)
status_label = tk.Label(root, text="", font=("Arial", 12), bg="gray15", fg="white")
status_label.pack(side=tk.BOTTOM, fill=tk.X, pady=2)

root.mainloop()
