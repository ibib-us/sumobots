# Note frequencies in Hertz
note_frequencies = {
    "A4": 440.00,
    "B4": 493.88,
    "C4": 261.63,
    "D4": 293.66,
    "E4": 329.63,
    "F4": 349.23,
    "G4": 392.00,
    "A5": 880.00,
    "C5": 523.25,
    "P": 0,  # Pause
}

# Duration of each note in seconds
note_durations = {
    "quarter": 0.5,  # 500 milliseconds
    "eighth": 0.25,  # 250 milliseconds
    "half": 1.0,  # 1000 milliseconds or 1 second
}

# Melody for the robot startup
robot_startup_melody = [
    ("C4", "quarter"),
    ("P", "eighth"),
    ("C4", "quarter"),
    ("P", "eighth"),
    ("C4", "quarter"),
    ("P", "eighth"),
    ("C5", "half"),
]


def note_values(note, duration):
    """
    Returns the note frequency in Hz and the note duration in seconds for
    the given note and duration.
    E.g. note_values("C4", "quarter") = 261.63, 0.5
    """
    return note_frequencies[note], note_durations[duration]
