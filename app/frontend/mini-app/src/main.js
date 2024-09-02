// main.js
import './assets/styles/main.sass';
import { createApp } from 'vue';
import { createPinia } from 'pinia';
import ElementPlus from 'element-plus';
import 'element-plus/dist/index.css';
import { useUserStore } from './stores/UserStore'; // Обновленный импорт
import App from './App.vue';
import router from './router';

const app = createApp(App);

app.use(createPinia());
app.use(router);
app.use(ElementPlus);
app.mount('#app');

// Обработка URL параметров и установка данных
const urlParams = new URLSearchParams(window.location.search);
const userData = {
  tg_user_id: urlParams.get('tg_user_id'),
  first_name: urlParams.get('first_name'),
  last_name: urlParams.get('last_name'),
  username: urlParams.get('username'),
  date_of_birth: urlParams.get('date_of_birth'),
  created_at: urlParams.get('created_at'),
  updated_at: urlParams.get('updated_at'),
};

if (userData.tg_user_id) {
  const userStore = useUserStore();
  userStore.setUser(userData);
  console.log('User data set:', userData);
}
