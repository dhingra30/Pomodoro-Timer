from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"  # Color for short breaks
RED = "#e7305b"  # Color for long breaks
GREEN = "#9bdeac"  # Color for work periods
YELLOW = "#f7f5dd"  # Background color
FONT_NAME = "Courier"  # Font used in labels
WORK_MIN = 25  # Duration of work session in minutes
SHORT_BREAK_MIN = 5  # Duration of short break in minutes
LONG_BREAK_MIN = 15  # Duration of long break in minutes
reps = 0  # Counter for the number of sessions completed


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    """Resets the timer and UI elements to their initial states."""
    label1.config(text="Timer")  # Reset the label to show "Timer"
    window.after_cancel(timer1)  # Cancel any active timer
    canvas.itemconfig(timer_text, text="00:00")  # Reset countdown display
    label2.config(text="")  # Clear marks for completed sessions
    global reps
    reps = 0  # Reset the reps counter


# ---------------------------- TIMER MECHANISM ------------------------------- #
def timer():
    """Determines the type of session (work/break) and starts the countdown."""
    global reps
    reps += 1  # Increment the session counter

    # Determine the type of session and duration based on the number of reps
    if reps % 8 == 0:
        label1.config(text="LONG BREAK", fg=RED)  # Set label for long break
        time = LONG_BREAK_MIN  # Set time for long break
    elif reps % 2 == 0:
        label1.config(text="SHORT BREAK", fg=PINK)  # Set label for short break
        time = SHORT_BREAK_MIN  # Set time for short break
    else:
        label1.config(text="WORK TIME", fg=GREEN)  # Set label for work
        time = WORK_MIN  # Set time for work session

    count_down(time * 60)  # Start countdown (convert minutes to seconds)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    """Counts down the time and updates the display every second."""
    global timer1
    count_min = math.floor(count / 60)  # Calculate minutes remaining
    count_seconds = count % 60  # Calculate seconds remaining

    # Format seconds to always show two digits
    if count_seconds == 0:
        count_seconds = "00"
    elif count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    # Format minutes to always show two digits
    if count_min < 10:
        count_min = "0" + str(count_min)

    # Update the timer display if time is still remaining
    if count > 0:
        canvas.itemconfig(timer_text, text=f"{count_min}:{count_seconds}")
        timer1 = window.after(1000, count_down, count - 1)  # Schedule next countdown
    else:
        timer()  # Start a new timer when countdown finishes
        mark = ""  # Initialize mark for completed sessions
        for _ in range(math.floor(reps / 2)):
            mark += "✔"  # Add a checkmark for each completed work session
        label2.config(text=mark)  # Update the label with completed marks


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()  # Create the main window
label1 = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 45, "bold"))  # Main timer label
label2 = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))  # Label for completed sessions
button1 = Button(window, text="Start", height=2, width=3, command=timer)  # Start button
button2 = Button(text="Reset", height=2, width=3, command=reset_timer)  # Reset button
window.title("Pomodoro")  # Set the window title
window.config(padx=100, pady=50, bg=YELLOW)  # Configure window padding and background
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)  # Canvas for timer display
tomato_image = PhotoImage(file="tomato.png")  # Load tomato image
canvas.create_image(100, 110, image=tomato_image)  # Place tomato image on canvas
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))  # Timer text
canvas.grid(row=2, column=2)  # Place canvas in the grid
label1.grid(row=1, column=2)  # Place main timer label in the grid
button1.grid(row=3, column=1)  # Place start button in the grid
button2.grid(row=3, column=3)  # Place reset button in the grid
label2.grid(row=3, column=2)  # Place completed sessions label in the grid
window.mainloop()  # Start the GUI event loop
