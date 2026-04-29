# ⚡ FlashRacer

A fun, fast-paced flashcard racing game to make studying enjoyable.

## Features
- Create & save named flashcard decks
- Race through flashcards with a progress bar + animal avatar
- Skip cards (10s penalty) or answer to advance
- Wrong answers recycle the card back into the queue
- Accuracy & time stats saved per deck
- Full run history per deck

## Setup

### 1. Install Python (3.9+)
https://python.org/downloads

### 2. Install dependencies
```
pip install -r requirements.txt
```

### 3. Run the server
```
python app.py
```

### 4. Open your browser
Go to: http://localhost:5000

## File Structure
```
flashracer/
  app.py              ← Flask backend (API + server)
  requirements.txt    ← Python dependencies
  templates/
    index.html        ← Full frontend (HTML/CSS/JS)
  data/
    decks.json        ← Saved flashcard decks (auto-created)
    stats.json        ← Game history/stats (auto-created)
```

## How to Play
1. Pick your animal racer on the home screen
2. Create a deck using the ✏️ editor — add questions & answers
3. Save the deck, then click Play (or Save & Play)
4. A 3-second countdown starts, then GO!
5. Type answers and press Enter to submit
6. Skip if stuck (10s wait penalty)
7. Finish all cards to see your stats!
