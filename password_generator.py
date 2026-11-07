import customtkinter as ctk
import secrets
import string


# Appearance
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")


# Password generation
def generate_password():
    try:
        length = int(length_entry.get())

        if not 1 <= length <= 128:
            raise ValueError

    except ValueError:
        result_label.configure(text="1〜128の数字を入力してください")
        copy_label.configure(text="")
        return

    characters = string.ascii_letters + string.digits + string.punctuation

    password = "".join(
        secrets.choice(characters) for _ in range(length)
    )

    result_label.configure(text=password)
    copy_label.configure(text="")
    copy_button.configure(state="normal")


# Copy password
def copy_password():
    password = result_label.cget("text")

    if not password or password == "ここにパスワードが表示されます":
        return

    window.clipboard_clear()
    window.clipboard_append(password)

    copy_label.configure(text="Copied successfully!")


# Window
window = ctk.CTk()
window.title("Mob Password Generator")
window.geometry("440x340")
window.resizable(False, False)
window.configure(fg_color="#121212")


# Main frame
main_frame = ctk.CTkFrame(
    window,
    fg_color="transparent"
)
main_frame.pack(expand=True, fill="both", padx=30, pady=20)


# Title
title_label = ctk.CTkLabel(
    main_frame,
    text="Password Generator",
    font=("Arial", 24, "bold"),
    text_color="#FFFFFF"
)
title_label.pack(pady=(10, 25))


# Length input
length_entry = ctk.CTkEntry(
    main_frame,
    placeholder_text="Password Length",
    width=200,
    height=38,
    justify="center",
    font=("Arial", 14)
)
length_entry.insert(0, "16")
length_entry.pack()


# Generate button
generate_button = ctk.CTkButton(
    main_frame,
    text="Generate Password",
    command=generate_password,
    width=200,
    height=40,
    fg_color="#333333",
    hover_color="#555555",
    font=("Arial", 14, "bold")
)
generate_button.pack(pady=20)


# Password result
result_label = ctk.CTkLabel(
    main_frame,
    text="ここにパスワードが表示されます",
    font=("Arial", 13),
    text_color="#FFFFFF",
    wraplength=350
)
result_label.pack(pady=5)


# Copy button
copy_button = ctk.CTkButton(
    main_frame,
    text="Copy Password",
    command=copy_password,
    width=200,
    height=38,
    fg_color="#333333",
    hover_color="#555555",
    state="disabled",
    font=("Arial", 14)
)
copy_button.pack(pady=10)


# Copy confirmation
copy_label = ctk.CTkLabel(
    main_frame,
    text="",
    font=("Arial", 12),
    text_color="#00CC88"
)
copy_label.pack()


# Start application
window.mainloop()