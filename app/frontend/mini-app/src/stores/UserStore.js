// src/stores/userStore.js
import { defineStore } from 'pinia';

export const useUserStore = defineStore('user', {
  state: () => ({
    tg_user_id: null,
    first_name: '',
    last_name: '',
    username: '',
    date_of_birth: null,
    created_at: null,
    updated_at: null,
  }),
  actions: {
    setUser(data) {
      this.tg_user_id = data.tg_user_id || null;
      this.first_name = data.first_name || '';
      this.last_name = data.last_name || '';
      this.username = data.username || '';
      this.date_of_birth = data.date_of_birth || null;
      this.created_at = data.created_at || null;
      this.updated_at = data.updated_at || null;
    }
  }
});
