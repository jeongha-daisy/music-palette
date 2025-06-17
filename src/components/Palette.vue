<template>
  <div>
    <AlbumSearch @albumSelected="addAlbumToPalette" />
    <div class="palette-wrapper" ref="paletteRef">
      <img :src="paletteImg" alt="Palette" class="palette-image" />
      <div class="overlay-grid" :style="{ '--col-count': cols, '--row-count': rows }">
        <div
          v-for="(cell, i) in cells"
          :key="i"
          class="overlay-cell"
          :class="{ selected: currentIndex === i }"
          @click="handleCellClick(i)"
        >
          <div class="cell-box" :class="{ filled: cell !== null }">
            <template v-if="cell">
              <img :src="cell" alt="Album Cover" />
            </template>
            <template v-else>
              <span>+</span>
            </template>
          </div>
        </div>
      </div>
    </div>

    <div class="button-group">
      <button class="download-btn" @click="downloadImage">save your palette</button>
    </div>
    <footer class="footer">
      <p>jeongha-daisy@gmail.com</p>
    </footer>
  </div>
</template>

<script setup>
import { ref, defineProps } from 'vue'
import html2canvas from 'html2canvas'
import axios from 'axios'
import AlbumSearch from './AlbumSearch.vue'

import paletteImg from '@/assets/palette.jpeg'

const props = defineProps({
  cols: { type: Number, default: 7 },
  rows: { type: Number, default: 8 },
})
const cells = ref(Array(56).fill(null))

const paletteRef = ref(null)
const currentIndex = ref(null)

function handleCellClick(index) {
  currentIndex.value = index
}
async function convertImageToBase64(imageUrl) {
  const response = await fetch(imageUrl, { mode: 'cors' })
  const blob = await response.blob()

  return new Promise((resolve, reject) => {
    const reader = new FileReader()
    reader.onloadend = () => resolve(reader.result)
    reader.onerror = reject
    reader.readAsDataURL(blob)
  })
}
async function addAlbumToPalette(url) {
  const base64Image = await convertImageToBase64(url)
  cells.value[currentIndex.value] = base64Image
  currentIndex.value = null
}

async function downloadImage() {
  if (!paletteRef.value) return

  const canvas = await html2canvas(paletteRef.value)
  const link = document.createElement('a')
  link.href = canvas.toDataURL('image/png')
  link.download = 'music-palette.png'
  link.click()
}
</script>

<style scoped>
.palette-wrapper {
  position: relative;
  width: 100%;
}

.palette-image {
  display: block;
  width: 100%;
  height: auto;
}
.overlay-grid {
  position: absolute;
  top: 2%;
  left: 3%;
  width: 94%;
  height: 96%;
  display: grid;
  grid-template-columns: repeat(var(--col-count), 1fr);
  grid-template-rows: repeat(var(--row-count), 1fr);
}

.overlay-cell {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
}

.cell-box {
  width: 75%;
  height: 75%;
  background: rgba(255, 255, 255, 0.5);
  border: 3px solid rgb(255, 255, 255);
  border-radius: 4px;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
  overflow: hidden;
  transition: background 0.3s;
}

.cell-box.filled {
  background: transparent;
  border: none;
}

.cell-box img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 4px;
}

.cell-box span {
  font-size: 20px;
  color: #333;
}

.overlay-cell.selected .cell-box {
  background: rgb(255, 255, 255);
  box-shadow: 0 0 8px rgb(0, 0, 0);
  transform: scale(1.05);
  transition: all 0.2s ease;
}

.button-group {
  margin-top: 20px;
  display: flex;
  flex-direction: column;
  gap: 10px;
  align-items: center;
}

.download-btn {
  padding: 10px 10px;
  font-size: 16px;

  border-style: solid;
  border-width: 10px;
  border-image: url('@/assets/button.svg') 10 stretch;

  cursor: pointer;
  width: 200px;
  font-family: 'Lexend Giga', sans-serif;
  color: #6f4e37;
}

.footer {
  text-align: center;
  margin-top: 40px;
  color: #6f4e37;
  font-size: 10px;
  opacity: 0.85;
}
</style>
