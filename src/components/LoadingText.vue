<template>
  <div class="loading-text">{{ displayedText }}<span class="cursor">|</span></div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const fullText = 'wait a sec ...'
const displayedText = ref('')
const speed = 100 // 타이핑 속도 (ms)
const delayBetweenRepeat = 1000 // 반복 간격 (ms)

function startTyping() {
  displayedText.value = ''
  let index = 0
  const interval = setInterval(() => {
    displayedText.value += fullText[index]
    index++
    if (index >= fullText.length) {
      clearInterval(interval)
      setTimeout(() => startTyping(), delayBetweenRepeat)
    }
  }, speed)
}

onMounted(() => {
  startTyping()
})
</script>

<style scoped>
.loading-text {
  font-family: 'Lexend Giga', sans-serif;
  font-size: 20px;
  color: #6f4e37;
  text-align: center;
  margin-top: 50px;
  margin-bottom: 50px;
}

.cursor {
  display: inline-block;
  margin-left: 5px;
  animation: blink 1s steps(2, start) infinite;
}

@keyframes blink {
  to {
    visibility: hidden;
  }
}
</style>
