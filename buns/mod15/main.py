# main.py
import json
from flask import Flask, jsonify, request
import service
import model

app = Flask(__name__)


@app.route('/rooms', methods=['GET'])
def get_room():
    check_in_date = request.args.get('checkIn')
    check_out_date = request.args.get('checkOut')
    guests_num = int(request.args.get('guestsNum', 1))
    rooms = service.get_rooms(check_in_date, check_out_date, guests_num)
    return json.dumps({"rooms": rooms}, sort_keys=False)


@app.route('/rooms/add', methods=['POST'])
def add_room():
    if not request.json or 'floor' not in request.json or 'beds' not in request.json \
            or 'guestNum' not in request.json or 'price' not in request.json:
        return jsonify({"error": "Invalid request"}), 400

    floor = request.json['floor']
    beds = request.json['beds']
    guest_num = request.json['guestNum']
    price = request.json['price']

    service.add_room(floor, beds, guest_num, price)
    return jsonify({"message": "Room added successfully"}), 201


@app.route('/rooms/book', methods=['POST'])
def booking():
    if not request.json or 'roomId' not in request.json:
        return jsonify({"error": "Invalid request"}), 400
    room_id = request.json['roomId']
    if not service.book_room(room_id):
        return jsonify({"error": "Room not found"}), 409
    return jsonify({"message": "Room booked successfully"}), 201


if __name__ == '__main__':
    model.initialize_database()
    app.run(debug=True)
