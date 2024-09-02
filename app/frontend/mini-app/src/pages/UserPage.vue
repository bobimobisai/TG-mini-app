<template>
  <div class="screen-container">
    <h1>User Page</h1>
    
    <div v-if="apiResponse || showDateOfBirthForm" class="dob-form-container">
      <p>{{ apiResponse || 'Пожалуйста, введите свою дату рождения:' }}</p>
      <form v-if="showDateOfBirthForm" @submit.prevent="handleSubmit">
        <input 
          type="date"
          v-model="dateOfBirth"
          :min="minDate"
          class="date-picker"
        />
        <button type="submit" class="button-submit">Submit</button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useUserStore } from '@/stores/UserStore';
import axios from 'axios';
import { useRouter } from 'vue-router';

const userStore = useUserStore();
const apiResponse = ref('');
const showDateOfBirthForm = ref(false);
const dateOfBirth = ref('');
const router = useRouter();


const minDate = '1900-01-01';

onMounted(async () => {
  const urlParams = new URLSearchParams(window.location.search);
  userStore.tg_user_id = urlParams.get('tg_user_id');

  if (userStore.tg_user_id) {
    try {
      const response = await axios.get(`/get_user/${userStore.tg_user_id}`);
      if (response.status === 200) {
        userStore.first_name = response.data.first_name;
        userStore.last_name = response.data.last_name;
        userStore.username = response.data.username;
        userStore.date_of_birth = response.data.date_of_birth;
        userStore.created_at = response.data.created_at;
        userStore.updated_at = response.data.updated_at;
        await router.push("/user-profile");
      } else {
        apiResponse.value = `Status: ${response.status}, Data: ${JSON.stringify(response.data)}`;
      }
    } catch (error) {
      if (error.response && error.response.status === 404) {
        apiResponse.value = 'User not found. Please enter your date of birth.';
        showDateOfBirthForm.value = true;
      } else {
        apiResponse.value = `Error: ${error.message}`;
        console.error('Error fetching user data:', error);
      }
    }
  } else {
    apiResponse.value = 'No tg_user_id found in URL.';
  }
});

const handleSubmit = async () => {
  if (!dateOfBirth.value) {
    apiResponse.value = 'Please select a date of birth.';
    return;
  }

  try {
    await axios.post('/create_user', {
      tg_user_id: userStore.tg_user_id,
      first_name: userStore.first_name,
      last_name: userStore.last_name,
      username: userStore.username,
      date_of_birth: dateOfBirth.value,
    });
    
    userStore.date_of_birth = dateOfBirth.value;
    await router.push("/user-profile");
  } catch (error) {
    apiResponse.value = `Error updating user: ${error.message}`;
    console.error('Error updating user:', error);
  }
};
</script>

<style scoped>
.screen-container {
  max-width: 500px;
  margin: 0 auto;
  text-align: center;
  padding: 20px;
}

.dob-form-container {
  background-color: rgba(255, 255, 255, 0.2);
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
}

p {
  font-size: 1.2rem;
  margin: 10px 0;
  color: #fff;
}

.date-picker {
  padding: 10px;
  font-size: 1rem;
  border-radius: 5px;
  border: 1px solid #ccc;
  margin-bottom: 20px;
}

.button-submit {
  background-color: #6200ea;
  color: #fff;
  padding: 10px 20px;
  font-size: 1rem;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin-top: 20px;
  transition: background-color 0.3s ease;
}

.button-submit:hover {
  background-color: #3700b3;
}
</style>
