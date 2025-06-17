<template>
  <div class="app-container">
    <div class="logo-wrapper">
      <img src="@/assets/logo.png" alt="Music Palette Logo" class="logo-image" />
    </div>
    <Palette />
  </div>
</template>

<script setup>
import AlbumSearch from './components/AlbumSearch.vue'
import Palette from './components/Palette.vue'
</script>

<style>
* {
  box-sizing: border-box;
}
.lexend-giga-<uniquifier > {
  font-family: 'Lexend Giga', sans-serif;
  font-optical-sizing: auto;
  font-weight: <weight>;
  font-style: normal;
}

html,
body {
  height: 100%;
  margin: 0;
  padding: 3%;
  font-family: 'Lexend Giga', sans-serif;
  background-image: url('@/assets/paper-texture.jpg');
  background-repeat: repeat;
  background-size: cover;
  background-position: center;
  background-blend-mode: multiply;
  overflow-x: hidden;
}

.app-container {
  width: 100%;
  max-width: 800px;
  margin: 0 auto;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 20px 15px;
}

.logo-wrapper {
  text-align: center;
  margin-top: 50px;
  margin-bottom: 30px;
  animation: fadeIn 1.2s ease-out;
}

.logo-image {
  max-width: 280px;
  width: 70%;
  height: auto;
  transition: transform 0.3s ease;
}

.logo-image:hover {
  transform: scale(1.05);
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@media (max-width: 480px) {
  .logo-image {
    max-width: 220px;
  }
}
</style>
