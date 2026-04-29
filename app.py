from flask import Flask, request, jsonify, render_template
import json
import os
from datetime import datetime

app = Flask(__name__)
DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
os.makedirs(DATA_DIR, exist_ok=True)

DECKS_FILE = os.path.join(DATA_DIR, 'decks.json')
STATS_FILE = os.path.join(DATA_DIR, 'stats.json')

def load_json(path):
    if not os.path.exists(path):
        return {}
    with open(path, 'r') as f:
        return json.load(f)

def save_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)

# ── Decks ──────────────────────────────────────────────
@app.route('/api/decks', methods=['GET'])
def get_decks():
    decks = load_json(DECKS_FILE)
    return jsonify(list(decks.values()))

@app.route('/api/decks', methods=['POST'])
def save_deck():
    data = request.json
    decks = load_json(DECKS_FILE)
    deck_id = data.get('id') or datetime.utcnow().strftime('%Y%m%d%H%M%S%f')
    deck = {
        'id': deck_id,
        'title': data['title'],
        'cards': data['cards'],
        'created': data.get('created', datetime.utcnow().isoformat()),
        'updated': datetime.utcnow().isoformat()
    }
    decks[deck_id] = deck
    save_json(DECKS_FILE, decks)
    return jsonify(deck)

@app.route('/api/decks/<deck_id>', methods=['DELETE'])
def delete_deck(deck_id):
    decks = load_json(DECKS_FILE)
    if deck_id in decks:
        del decks[deck_id]
        save_json(DECKS_FILE, decks)
    return jsonify({'ok': True})

# ── Stats ──────────────────────────────────────────────
@app.route('/api/stats', methods=['GET'])
def get_stats():
    stats = load_json(STATS_FILE)
    return jsonify(stats)

@app.route('/api/stats', methods=['POST'])
def save_stats():
    data = request.json
    stats = load_json(STATS_FILE)
    deck_id = data['deckId']
    if deck_id not in stats:
        stats[deck_id] = []
    stats[deck_id].append({
        'date': datetime.utcnow().isoformat(),
        'timeTaken': data['timeTaken'],
        'accuracy': data['accuracy'],
        'totalCards': data['totalCards'],
        'correctFirst': data['correctFirst'],
        'skipped': data['skipped'],
        'completed': data['completed']
    })
    save_json(STATS_FILE, stats)
    return jsonify({'ok': True})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
