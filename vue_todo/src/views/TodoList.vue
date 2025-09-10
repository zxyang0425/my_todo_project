<template>
  <div>
    <h1>待辦清單</h1>
    <form @submit.prevent="addTask">
      <input v-model="newTaskTitle" placeholder="請輸入待辦事項" required />
      <input v-model="newTaskDescription" placeholder="請描述待辦內容" />
      <button type="submit">新增</button>
    </form>
    <ul>
      <li v-for="task in tasks" :key="task.id">
        <label>
          <input type="checkbox" v-model="task.done" @change="updateTask(task)" />
          <span v-if="editingTaskId !== task.id" @click="startEditing(task.id)" :class="{ done: task.done }">
            {{ task.title }}
          </span>
          <input v-else
                v-model="task.title"
                @keyup.enter="finishEditing(task)"
                @blur="finishEditing(task)"
                class="edit-input"
                />
        </label>
        <p v-if="editingTaskId !== task.id" @click="startEditing(task.id)">
          {{ task.description }}
        </p>
        <textarea v-else
                  v-model="task.description"
                  @keyup.enter="finishEditing(task)"
                  @blur="finishEditing(task)"
                  class="edit-textarea"
                  ></textarea> 
        <button @click="deleteTask(task.id)">刪除</button>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      newTaskTitle: '',
      newTaskDescription: '',
      tasks: [],
      editingTaskId: null
    }
  },
  methods: {
    async fetchTasks() {
      const res = await axios.get('http://127.0.0.1:8000/tasks')
      this.tasks = res.data
    },
    async addTask() {
      const newTask = {
        title: this.newTaskTitle,
        description: this.newTaskDescription,
        done: false
      }
      await axios.post('http://127.0.0.1:8000/task', newTask)
      this.newTaskTitle = ''
      this.newTaskDescription = ''
      this.fetchTasks()
    },
    async updateTask(task) {
      // 用 updateTaskPayload 只包含 title / description / done，不改 id
      const updateTaskPayload = {
        title: task.title,
        description: task.description,
        done: task.done
      }
      await axios.put(`http://127.0.0.1:8000/tasks/${task.id}`, updateTaskPayload)
      this.fetchTasks()
    },
    async deleteTask(id) {
      await axios.delete(`http://127.0.0.1:8000/tasks/${id}`)
      this.fetchTasks()
    },
    // 點一下任務標題/描述進入編輯
    startEditing(id) {
      this.editingTaskId = id
    },
    // 編輯完成時更新任務
    async finishEditing(task) {
      this.editingTaskId = null
      await this.updateTask(task)
    }
  },
  mounted() {
    this.fetchTasks()
  }
}
</script>

<style>
/* body {
  font-family: Arial, sans-serif;
  padding: 2rem;
}

#app {
  max-width: 600px;
  margin: 0 auto;
  padding: 2rem;
  background-color: #f9f9f9;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

h1 {
  text-align: center;
  color: #333;
  margin-bottom: 1.5rem;
}

form {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  margin-bottom: 2rem;
}

input[type="text"],
input[type="checkbox"],
input[placeholder] {
  padding: 0.5rem 0.75rem;
  border: 1px solid #ccc;
  border-radius: 8px;
  font-size: 16px;
}

button {
  padding: 0.6rem 1rem;
  font-size: 16px;
  border: none;
  border-radius: 8px;
  background-color: #4CAF50;
  color: white;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

button:hover {
  background-color: #45a049;
}

ul {
  list-style: none;
  padding: 0;
}

li {
  background-color: white;
  border-radius: 10px;
  padding: 1rem;
  margin-bottom: 1rem;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
}

label {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-weight: 500;
}

span {
  font-size: 18px;
}

span.done {
  color: #999;
}

p {
  margin: 0;
  padding-left: 1.5rem;
  color: #555;
}

li button {
  align-self: flex-end;
  background-color: #f44336;
  margin-top: 0.5rem;
}

li button:hover {
  background-color: #d32f2f;
}

.edit-input, .edit-textarea {
  width: 100%;
  padding: 4px 8px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 6px;
  margin-top: 4px;
  box-sizing: border-box;
}
.edit-textarea {
  resize: vertical;
  min-height: 40px;
} */
</style>
