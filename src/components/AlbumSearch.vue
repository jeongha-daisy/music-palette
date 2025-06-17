<template>
  <div class="search-container">
    <div class="input-wrapper">
      <input v-model="query" type="text" placeholder="Search by Album Name" />
      <button @click="searchAlbums">go!</button>
    </div>
    <LoadingText v-if="isLoading" />
    <div v-else class="results">
      <div
        class="result-item"
        v-for="(album, index) in results"
        :key="index"
        @click="selectAlbum(album.coverUrl)"
      >
        <img :src="album.coverUrl" />
        <p>{{ album.title }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import LoadingText from './LoadingText.vue'

const query = ref('')
const results = ref([])
const searchIcon = '@/assets/search.png'
const isLoading = ref(false)

async function searchAlbums() {
  isLoading.value = true
  const searchUrl = `https://musicbrainz.org/ws/2/release/?query=release:${encodeURIComponent(query.value)}&fmt=json`
  const res = await fetch(searchUrl)
  const data = await res.json()

  const albums = await Promise.all(
    data.releases.map(async (release) => {
      const id = release.id
      const title = release.title

      try {
        const coverRes = await fetch(`https://coverartarchive.org/release/${id}/front-500`)
        if (coverRes.ok) {
          return { id, title, coverUrl: coverRes.url }
        }
      } catch (e) {}

      return null
    }),
  )

  results.value = albums.filter((album) => album !== null)
  isLoading.value = false
}

const emit = defineEmits(['albumSelected'])

function selectAlbum(url) {
  emit('albumSelected', url)
}
</script>

<style scoped>
.lexend-giga-<uniquifier > {
  font-family: 'Lexend Giga', sans-serif;
  font-optical-sizing: auto;
  font-weight: <weight>;
  font-style: normal;
}

.search-container {
  margin: 20px auto;
  max-width: 400px;
  font-family: 'Lexend Giga', sans-serif;
}

.input-wrapper {
  display: flex;
  align-items: center;
  gap: 10px;
}

input {
  flex: 1;
  padding: 10px 15px;
  border: none;
  background-color: transparent;

  border-style: solid;
  border-width: 10px;
  border-image: url('@/assets/button.svg') 10 stretch;
  color: #6f4e37;

  font-family: 'Lexend Giga', sans-serif;
  font-size: 16px;
  outline: none;
  transition: border-color 0.3s;
}

input::placeholder {
  color: #aaa;
  font-family: 'Lexend Giga', sans-serif;
  font-size: 16px;
}

/* 검색 버튼 스타일 */
button {
  padding: 10px 15px;
  border: none;
  background-color: transparent;
  border-style: solid;
  border-width: 10px;
  border-image: url('@/assets/button.svg') 10 stretch;
  color: #6f4e37;
  font-family: 'Lexend Giga', sans-serif;
  font-size: 18px;
  cursor: pointer;
}

/* 결과 리스트 */
.results {
  display: flex;
  overflow-x: auto;
  gap: 10px;
  padding: 10px;
  scroll-snap-type: x mandatory;
}

.result-item {
  flex: 0 0 auto;
  width: 120px;
  scroll-snap-align: start;
}

.result-item img {
  width: 100%;
  height: 120px;
  object-fit: cover;
  border-radius: 8px;
}
</style>
