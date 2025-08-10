# LaunchPAD - Unfound Sounds! 🎵

A dynamic music creation application built with Python and Pygame that transforms your keyboard into an interactive launchpad for creating unique musical compositions.

## 📖 Overview

LaunchPAD - Unfound Sounds! is an interactive music application developed as part of my 2022 AP Computer Science Principles project. The application provides users with an intuitive interface to create music by mapping keyboard keys to different musical frequencies, complete with real-time visual feedback and audio synthesis.

## ✨ Features

- **Interactive Keyboard Mapping**: Each keyboard key (A-Z, 1-3) is mapped to a specific musical frequency
- **Real-time Audio Synthesis**: Generate tones dynamically using NumPy and Pygame's audio capabilities
- **Visual Feedback**: Colorful visual indicators that light up when keys are pressed
- **Multiple Screen Navigation**: Clean UI with main menu, game screen, and information screens
- **Continuous Audio Playback**: Hold keys for sustained notes, release to stop
- **State Management**: Prevents accidental audio playback when not on the game screen

## 🎮 How to Use

1. **Main Menu**: Start the application and choose from Start, Info, or Exit options
2. **Game Screen**: Press any letter key (A-Z) or number key (1-3) to play different musical tones
3. **Visual Response**: Watch as the corresponding boxes light up with random colors
4. **Create Music**: Combine multiple keys to create your own unique compositions
5. **Navigation**: Press ESC at any time to return to the main menu

## 🛠️ Technical Implementation

### Technologies Used
- **Python**: Core programming language
- **Pygame**: Graphics rendering, event handling, and audio playback
- **NumPy**: Mathematical operations for audio wave generation
- **Pygame.midi**: MIDI functionality support

### Key Components
- **Audio Synthesis**: Real-time tone generation using sine wave mathematics
- **Event-Driven Architecture**: Responsive keyboard and mouse input handling
- **State Management System**: Prevents unwanted audio playback across different screens
- **Dynamic Visual Rendering**: Color-coded visual feedback system
- **Modular Design**: Organized code structure with separate functions for different features

## 📁 Project Structure

```
LaunchPAD/
├── assets/
│   ├── homeScreenBackground.gif
│   ├── newLogo.png
│   ├── fin.png
│   ├── start_btn.png
│   ├── exit_btn.png
│   ├── fin_question.png
│   ├── music-wave.png
│   ├── question-mark.png
│   └── cityskies.png
├── main.py
└── README.md
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.x
- pip package manager

### Required Dependencies
```bash
pip install -r requirements.txt
```

### Running the Application
```bash
python main.py
```

## 🎹 Key Mappings

The application maps keyboard keys to musical frequencies as follows:

**Letter Keys (A-Z)**: Mapped to various musical notes from C4 to G7
- A = 261.63 Hz (C4)
- F = 440.00 Hz (A4) 
- And many more...

**Number Keys (1-3)**: Mapped to chord-friendly frequencies
- 1 = 261.63 Hz (C4)
- 2 = 329.63 Hz (E4)
- 3 = 392.00 Hz (G4)

## 🎯 Learning Outcomes

This project demonstrates proficiency in:
- **Object-Oriented Programming**: Button class implementation and management
- **Event-Driven Programming**: Real-time user input handling
- **Audio Programming**: Digital signal processing and sound synthesis
- **State Management**: Application flow control and screen navigation
- **Mathematical Applications**: Frequency calculations and wave generation
- **User Interface Design**: Intuitive visual feedback and navigation

## 🤝 Contributing

This was a solo AP CSP project from 2022, but feel free to fork and expand upon it! Some potential improvements:
- Add recording/playback functionality
- Implement different instrument sounds
- Add rhythm patterns and loops
- Create preset musical scales

## 📜 License

This project is open source and available under the MIT License.

## 🎓 Academic Context

**Course**: AP Computer Science Principles  
**Year**: 2022  
**Focus Areas**: Programming, Digital Audio Processing, User Interface Design

---

*Created with ❤️ for music and code*