from app import app, db
from flask import request, jsonify
from app.models import Friend

## CRUD Operations
# Get all friends
@app.route('/api/friends', methods=['GET'])
def get_friends():
    friends = Friend.query.all()
    result = [friend.to_json() for friend in friends]
    return jsonify(result), 200

@app.route('/api/friends/<int:id>', methods=['GET'])
def get_friend_details(id):
    friend = Friend.query.get(id)
    if friend is None:
        return jsonify({"error": "Friend not found"}), 404
    return jsonify(friend.to_json()), 200

# Create friends
@app.route("/api/friends", methods=["POST"])
def create_friend():
    try:
        data = request.get_json()

        # Required Fields
        required_fields = ["name", "role", "description", "gender"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing {field} field"}), 400

        name = data.get('name')
        role = data.get('role')
        description = data.get('description')
        gender = data.get("gender")

        # Using API to generate Avatar Image
        # fetch avatar image based on gender:
        match gender:
            case "male":
                img_url = f"https://avatar.iran.liara.run/public/boy?username={name}"
            case "female":
                img_url = f"https://avatar.iran.liara.run/public/girl?username={name}"
            case _:
                img_url = None

        new_friend = Friend(name=name, role=role, description=description, gender=gender, img_url=img_url)

        db.session.add(new_friend)

        db.session.commit()

        return jsonify({"msg": "Friend created successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Delete Friends
@app.route("/api/friends/<int:id>", methods=["DELETE"])
def delete_friend(id):
    try:
        friend = Friend.query.get(id)
        if friend is None:
            return jsonify({"error": "Friend not found"}), 404

        db.session.delete(friend)

        db.session.commit()

        return jsonify({"msg": "Friend deleted successfully"}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Update Friends Profile
@app.route("/api/friends/<int:id>", methods=["PATCH"])
def update_friend(id):
    try:
        friend = Friend.query.get(id)
        if friend is None:
            return jsonify({"error": "Friend not found"}), 404

        data = request.get_json()
        friend.name = data.get("name", friend.name) # if name is not provided, keep the old name
        friend.role = data.get("role", friend.role) # if role is not provided, keep the old role
        friend.description = data.get("description", friend.description) # if description is not provided, keep the old description
        friend.gender = data.get("gender", friend.gender)

        db.session.commit()
        return jsonify({"msg": "Friend updated successfully", "data": friend.to_json()})

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
