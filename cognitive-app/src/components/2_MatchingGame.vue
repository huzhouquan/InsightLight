<template>
  <div class="game-container">
    <h3>命名能力: 匹配图片与名称</h3>
    <div v-if="!isGameDone" class="matching-board">
        <div class="image-zone">
          <div v-for="item in imageOptions" :key="'img-'+item.id" 
               @click="selectImage(item)" 
               :class="{ selected: selectedImage === item, correct: item.matched }">
            <img :src="`/images/${item.name}.png`" :alt="item.name">
          </div>
        </div>
        <div class="text-zone">
          <div v-for="item in textOptions" :key="'text-'+item.id" 
               @click="selectText(item)" 
               :class="{ selected: selectedText === item, correct: item.matched }">
            {{ item.name }}
          </div>
        </div>
    </div>
    <div v-else>
        <p>太棒了！您完成了这个游戏。</p>
        <button @click="completeGame">下一个</button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';

const emit = defineEmits(['game-completed']);

// Game data
const items = ref([
  { id: 1, name: '大象', matched: false },
  { id: 2, name: '狮子', matched: false },
  { id: 3, name: '老虎', matched: false },
]);
const imageOptions = ref([...items.value]);
const textOptions = ref([...items.value].sort(() => Math.random() - 0.5));

// Game state
const score = ref(0);
const selectedImage = ref(null);
const selectedText = ref(null);
const matchesFound = ref(0);

const isGameDone = computed(() => matchesFound.value === items.value.length);

// --- METHODS ---

function selectImage(item) {
  if (item.matched) return;
  selectedImage.value = item;
  checkMatch();
}

function selectText(item) {
  if (item.matched) return;
  selectedText.value = item;
  checkMatch();
}

function checkMatch() {
  if (selectedImage.value && selectedText.value) {
    if (selectedImage.value.id === selectedText.value.id) {
      // Correct match
      score.value += 10;
      // Mark as matched
      const matchedId = selectedImage.value.id;
      items.value.find(i => i.id === matchedId).matched = true;
      matchesFound.value++;
    }
    // Reset selection after a short delay
    setTimeout(() => {
      selectedImage.value = null;
      selectedText.value = null;
    }, 300);
  }
}

function completeGame() {
  emit('game-completed', { domain: '命名', score: score.value });
}
</script>

<style scoped>
/* Add styles for this specific game */
.matching-board { display: flex; justify-content: space-around; }
.image-zone, .text-zone { display: flex; flex-direction: column; gap: 15px; }
.image-zone div, .text-zone div {
  padding: 10px;
  border: 2px solid #ccc;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s;
}
.image-zone div.selected, .text-zone div.selected { border-color: #007bff; }
.image-zone div.correct, .text-zone div.correct {
  border-color: #42b883;
  background-color: #e9f5ee;
  pointer-events: none; /* Can't click anymore */
  opacity: 0.5;
}
img { width: 80px; height: 80px; }
</style>