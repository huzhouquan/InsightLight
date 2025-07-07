<template>
  <Radar :data="chartData" :options="chartOptions" />
</template>

<script setup>
import { computed } from 'vue';
import { Radar } from 'vue-chartjs';
import { Chart as ChartJS, Title, Tooltip, Legend, PointElement, RadialLinearScale, LineElement } from 'chart.js';

ChartJS.register(Title, Tooltip, Legend, PointElement, RadialLinearScale, LineElement);

const props = defineProps({
  results: {
    type: Object,
    required: true
  }
});

const chartData = computed(() => ({
  labels: [
    '视空间', '命名', '记忆', '注意', '语言', '抽象', '延迟回忆', '定向能力'
  ],
  datasets: [{
    label: '认知能力评估',
    backgroundColor: 'rgba(66, 185, 131, 0.2)',
    borderColor: 'rgba(66, 185, 131, 1)',
    pointBackgroundColor: 'rgba(66, 185, 131, 1)',
    data: [
      props.results.visuospatial || 0,
      props.results.naming || 0,
      props.results.memory || 0,
      props.results.attention || 0,
      props.results.language || 0,
      props.results.abstraction || 0,
      props.results.delayed_recall || 0,
      props.results.orientation || 0,
    ]
  }]
}));

const chartOptions = {
  responsive: true,
  maintainAspectRatio: true,
  scales: {
    r: {
      angleLines: { display: true },
      suggestedMin: 0,
      suggestedMax: 100, // Assuming scores are normalized to 100
      ticks: { backdropColor: 'transparent' }
    }
  },
  plugins: {
    legend: {
      position: 'top',
    },
    tooltip: {
      callbacks: {
        label: function(context) {
          return `${context.label}: ${context.raw}`;
        }
      }
    }
  }
};
</script>