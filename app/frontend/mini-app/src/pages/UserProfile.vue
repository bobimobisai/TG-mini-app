<template>
  <div class="profile-container">
    <h1>User Profile</h1>
    <div class="profile-info">
      <p><strong>First Name:</strong> {{ userStore.first_name }}</p>
      <p><strong>Last Name:</strong> {{ userStore.last_name }}</p>
      <p><strong>Username:</strong> {{ userStore.username }}</p>
      <p><strong>Date of Birth:</strong> {{ userStore.date_of_birth }}</p>
      <p><strong>Days to Birthday:</strong> {{ daysToBirthday }}</p>
    </div>
    <button class="button-share" @click="shareProfile">Share Profile</button>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import { useUserStore } from '@/stores/UserStore';

const userStore = useUserStore();

const daysToBirthday = computed(() => {
  if (!userStore.date_of_birth) return 'N/A';
  
  const today = new Date();
  const dob = new Date(userStore.date_of_birth);
  const nextBirthday = new Date(today.getFullYear(), dob.getMonth(), dob.getDate());

  if (today > nextBirthday) {
    nextBirthday.setFullYear(nextBirthday.getFullYear() + 1);
  }

  const timeDiff = nextBirthday - today;
  const daysDiff = Math.ceil(timeDiff / (1000 * 60 * 60 * 24));
  return daysDiff;
});

const shareProfile = () => {
  const profileUrl = `${window.location.origin}/?tg_user_id=${userStore.tg_user_id}`;
  navigator.clipboard.writeText(profileUrl)
    .then(() => alert('Profile link copied to clipboard!'))
    .catch(err => console.error('Failed to copy link: ', err));
};
</script>

<style lang="sass">
.profile-container
  max-width: 500px
  margin: 0 auto
  text-align: center
  padding: 20px

.profile-info
  background-color: rgba(255, 255, 255, 0.2)
  padding: 20px
  border-radius: 10px
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3)
  margin-bottom: 20px

h1
  font-size: 2.5rem
  margin-bottom: 20px
  text-align: center

p
  font-size: 1.2rem
  margin: 10px 0
  color: #fff

.button-share
  background-color: #6200ea
  color: #fff
  padding: 10px 20px
  font-size: 1rem
  border: none
  border-radius: 5px
  cursor: pointer
  transition: background-color 0.3s ease
  &:hover
    background-color: #3700b3
</style>
