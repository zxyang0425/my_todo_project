// // src/router/index.js
// import { createRouter, createWebHistory } from 'vue-router'
// import Login from '../views/Login.vue'
// import Register from '../views/Register.vue'
// import TodoList from '../views/TodoList.vue'

// const routes = [
//   { path: '/', redirect: '/login' },
//   { path: '/login', name: 'Login', component: () => import('../views/login.vue') },
//   { path: '/register', component: () => import('../views/Register.vue') },
//   {
//     path: '/tasks',
//     component: () => import('../views/TodoList.vue'),
//     meta: { requiresAuth: true }
//   }
// ]


// const router = createRouter({
//   history: createWebHistory(),
//   routes
// })

// // 路由守衛：未登入者不能進入 /tasks
// router.beforeEach((to, from, next) => {
//   console.log(`Router navigating to ${to.path}`)
//   const token = localStorage.getItem('token')
//   if (to.meta.requiresAuth && !token) {
//     next('/login')
//   } else {
//     next()
//   }
// })

// export default router
