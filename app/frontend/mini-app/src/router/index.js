import { createRouter, createWebHistory } from 'vue-router';
import UserProfile from '../pages/UserProfile.vue';
import UserPage from '../pages/UserPage.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'user-page',
      component: UserPage,
    },
    {
      path: '/user-profile',
      name: 'user-profile',
      component: UserProfile,
    }
  ]
});

export default router;
