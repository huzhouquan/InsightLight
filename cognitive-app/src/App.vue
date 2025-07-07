<template>
  <div id="main-container">
    <header>
      <h1>认知能力评估</h1>
      <p v-if="!testCompleted">游戏 {{ currentGameIndex + 1 }} / {{ totalGames }}</p>
    </header>

    <div v-if="!testStarted" class="welcome-screen">
      <h2>欢迎参加测试</h2>
      <p>请完成接下来的一系列小游戏，以评估您的认知能力。</p>
      <button @click="startTest">开始测试</button>
    </div>

    <div v-if="testStarted && !testCompleted">
      <component :is="currentGameComponent" @game-completed="handleGameCompletion" />
    </div>

    <div v-if="testCompleted" class="results-screen">
      <h2>评估结果</h2>
      <p v-if="isLoading">正在生成您的报告...</p>
      <div v-if="!isLoading && finalResults">
        <ResultsChart :results="finalResults" />
        <p class="share-info">您的分享链接是: {{ shareableLink }}</p>
        <button @click="resetTest">重新测试</button>
      </div>
      <div v-if="error">
        <p class="error-message">{{ error }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import axios from 'axios';

// Import all your components
import MazeGame from './components/1_MazeGame.vue';
import MatchingGame from './components/2_MatchingGame.vue';
import MemoryBoard from './components/3_MemoryBoard.vue';
import ConnectGame from './components/4_ConnectGame.vue';
import LanguageGame from './components/5_LanguageGame.vue';
import ClassifyGame from './components/6_ClassifyGame.vue';
import RecallGame from './components/7_RecallGame.vue';
import ResultsChart from './components/ResultsChart.vue';

// App state management
const testStarted = ref(false);
const testCompleted = ref(false);
const isLoading = ref(false);
const error = ref(null);

// Game flow management
const gameComponents = [
  MazeGame, MatchingGame, MemoryBoard, ConnectGame,
  LanguageGame, ClassifyGame, RecallGame
];
const totalGames = gameComponents.length;
const currentGameIndex = ref(0);
const currentGameComponent = computed(() => gameComponents[currentGameIndex.value]);

// Data collection
const assessmentScores = ref({});
const finalResults = ref(null);
const shareableLink = ref('');

// --- METHODS ---

function startTest() {
  testStarted.value = true;
}

function handleGameCompletion(payload) {
  // Store the score from the completed game
  assessmentScores.value[payload.domain] = payload.score;

  // Move to the next game or finish the test
  if (currentGameIndex.value < totalGames - 1) {
    currentGameIndex.value++;
  } else {
    finishTest();
  }
}

async function finishTest() {
  testCompleted.value = true;
  isLoading.value = true;
  error.value = null;

  // Prepare data for the backend
  const dataToSend = {
    visuospatial: assessmentScores.value['视空间'] || 0,
    naming: assessmentScores.value['命名'] || 0,
    memory: assessmentScores.value['记忆'] || 0,
    attention: assessmentScores.value['注意'] || 0,
    language: assessmentScores.value['语言'] || 0,
    abstraction: assessmentScores.value['抽象'] || 0,
    delayed_recall: assessmentScores.value['延迟回忆'] || 0,
    orientation: 0 // This needs its own game or question
  };

  try {
    // Send data to your Django backend
    const response = await axios.post('http://127.0.0.1:8000/api/results/', dataToSend);
    
    // Process the response
    finalResults.value = response.data;
    shareableLink.value = `http://yourapp.com/results/${response.data.id}`;
    
  } catch (e) {
    error.value = '无法连接到服务器，请稍后再试。';
    console.error(e);
  } finally {
    isLoading.value = false;
  }
}

function resetTest() {
  testStarted.value = false;
  testCompleted.value = false;
  currentGameIndex.value = 0;
  assessmentScores.value = {};
  finalResults.value = null;
  shareableLink.value = '';
}
</script>

<style>
/* Add your global styles here */
body {
  font-family: sans-serif;
  background-color: #f4f4f9;
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
}
#main-container {
  width: 90%;
  max-width: 600px;
  background: white;
  padding: 20px 40px;
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.1);
  text-align: center;
}
button {
  padding: 12px 25px;
  font-size: 1.1em;
  color: white;
  background-color: #42b883;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  margin-top: 20px;
  transition: background-color 0.3s;
}
button:hover {
  background-color: #349668;
}
.error-message {
  color: #d9534f;
}
.share-info {
  margin-top: 20px;
  padding: 10px;
  background-color: #eee;
  border-radius: 5px;
  word-wrap: break-word;
}
</style>