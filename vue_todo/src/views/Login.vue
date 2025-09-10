<template>
  <div style="border: 1px solid red; padding: 20px;">
    <p>{{ thisDoesNotExist }}</p>
    <p>Login Page Loaded</p>
    <h2>登入</h2>
    <form @submit.prevent="login">
      <input v-model="username" placeholder="使用者名稱" required />
      <input v-model="password" type="password" placeholder="密碼" required />
      <button type="submit">登入</button>
    </form>
    <p>還沒有帳號？<router-link to="/register">前往註冊</router-link></p>
    <p v-if="error" style="color: red">{{ error }}</p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'LoginPage',
  data() {
    return {
      username: '',
      password: '',
      error: ''
    }
  },
  methods: {
    async login() {
        try {
            const response = await axios.post("/auth/login", {
            username: this.username,
            password: this.password,
            });

            const token = response.data.access_token;
            localStorage.setItem("token", token); 
            this.$router.push("/tasks");           
        } catch (error) {
            console.error("登入失敗", error);
            this.error = "登入失敗，請檢查帳號密碼";
        }
    }
  },
  
  mounted() {
  console.log("Login component mounted");
  console.log("Login.vue 檔案有成功被載入");
    }
}
</script>

<style scoped>
div {
  background-color: #ffecec;
}
</style>
