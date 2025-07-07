<template>
  <div class="game-container">
    <h3>游戏占位符: {{ domainName }}</h3>
    <p>这里是游戏的具体内容。</p>
    <p>完成任务后，点击下方的按钮。</p>
    <button @click="completeGame">我完成了</button>
  </div>
</template>

<script setup>
const emit = defineEmits(['game-completed']);

// CHANGE THESE VALUES FOR EACH GAME
const domainName = '视空间'; // e.g., '记忆', '注意', etc.
const score = Math.floor(Math.random() * 80) + 20; // Generate a random score for now

function completeGame() {
  emit('game-completed', { domain: domainName, score: score });
}
</script>

<style scoped>
.game-container {
  padding: 20px;
  border: 1px dashed #ccc;
  border-radius: 10px;
}
</style>