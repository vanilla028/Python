from flask import Flask, request, jsonify

app = Flask(__name__)

# 간단한 데이터베이스 대신 리스트를 사용합니다.
todos = []

# 할 일 목록 조회 (GET /todos)
@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify({'todos': todos})

# 특정 할 일 조회 (GET /todos/{todo_id})
@app.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    if todo_id < 0 or todo_id >= len(todos):
        return jsonify({'error': '해당 To-Do를 찾을 수 없습니다'}), 404
    return jsonify(todos[todo_id])

# 새 할 일 추가 (POST /todos)
@app.route('/todos', methods=['POST'])
def create_todo():
    data = request.json
    if 'title' not in data:
        return jsonify({'error': '내용이 누락되었습니다'}), 400
    todo = {'title': data['title'], 'completed': False}
    todos.append(todo)
    return jsonify({'message': 'To-Do가 생성되었습니다'}), 201

# 특정 할 일 업데이트 (PUT /todos/{todo_id})
@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    if todo_id < 0 or todo_id >= len(todos):
        return jsonify({'error': '해당 To-Do를 찾을 수 없습니다'}), 404
    data = request.json
    if 'title' not in data:
        return jsonify({'error': '필수 필드 "title"이(가) 누락되었습니다'}), 400
    todos[todo_id]['title'] = data['title']
    return jsonify({'message': 'To-Do가 업데이트되었습니다'})

# 특정 할 일 삭제 (DELETE /todos/{todo_id})
@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    if todo_id < 0 or todo_id >= len(todos):
        return jsonify({'error': '해당 To-Do를 찾을 수 없습니다'}), 404
    del todos[todo_id]
    return jsonify({'message': 'To-Do가 삭제되었습니다'})

if __name__ == '__main__':
    app.run(debug=True)
